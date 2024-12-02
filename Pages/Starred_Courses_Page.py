import tkinter as tk
from tkinter import ttk, messagebox, Listbox
import csv



def read_csv():
    courses = []
    with open('Data/courses.csv',mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            courses.append({
                "module": row["code_module"],
                "presentation": row["code_presentation"],
                "length": row["module_presentation_length"],
                "starred": False  # Default star status is False (unstarred)
            })
    return courses

def write_csv(courses):
    with open('Data/courses.csv', mode='w', newline='') as file:
        fieldnames = ['code_module', 'code_presentation', 'module_presentation_length', 'starred']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for course in courses:
            writer.writerow({
                'code_module': course['module'],
                'code_presentation': course['presentation'],
                'module_presentation_length': course['length'],
                'Starred': 'Yes' if course['starred'] else 'No'
            })


def star_course(course_name, courses):
    for course in courses:
        fcourse_name = f"{course['module']} {course['presentation']}"
        if fcourse_name == course_name:
            course['starred'] = not course['starred']
            update_favs(courses)
            write_csv(courses)
            return

def update_favs(courses):
    listbox.delete(0, tk.END)
    for course in courses:
        fcourse_name = f"{course['module']} {course['presentation']}"
        star = "★" if course['starred'] else "☆"
        listbox.insert(tk.END, f"{star} {fcourse_name} ({course['length']} mins)")

def course_selected(event, courses):
    selected_index = listbox.curselection()
    if selected_index:
        selected_course = listbox.get(selected_index).strip("★☆ ")
        messagebox.showinfo("Course Analytics", f"Displaying analytics for {selected_course}.")



def starred_courses_page():
    courses = read_csv()  # Read courses from the CSV

    # Create the main window
    page = tk.Tk()
    page.title("Starred Courses Page")
    page.geometry("600x600")

    # Title Label
    title_label = tk.Label(page, text="Starred Courses Page", font=("Arial", 20))
    title_label.pack(pady=20)

    # listbox to display courses with star icons
    global listbox
    listbox = tk.Listbox(page, width=40, height=15, selectmode=tk.SINGLE, font=("Arial", 12))
    listbox.pack(pady=10)

    # Bind double-click to open course analytics
    listbox.bind("<Double-1>", lambda event: course_selected(event, courses))

    # Button to toggle the starred status of the selected course
    toggle_button = tk.Button(page, text="Star Course", command=lambda: star_course(listbox.get(tk.ACTIVE).strip("★☆ "), courses))
    toggle_button.pack(pady=10)

    # Update the displayed starred courses
    update_favs(courses)

    # Run the application
    page.mainloop()


starred_courses_page()