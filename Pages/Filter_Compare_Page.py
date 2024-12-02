import tkinter as tk
from tkinter import ttk
import csv

def load_courses(file_path):
    courses = set()
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                courses.add(row["code_module"])
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return sorted(courses)

def load_students(file_path):
    student_ids = set()
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_ids.add(row["id_student"])
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return sorted(student_ids)

def update_selected_courses_and_students():
    selected_courses = [course for course, var in course_vars.items() if var.get()]
    selected_student = selected_student_id.get()
    selected_date = selected_date_entry.get()
    print("Selected Courses for Comparison:", selected_courses)
    print("Selected Student ID for Comparison:", selected_student)
    print("Selected Date for Filtering:", selected_date)

def apply_filter_and_compare():
    selected_courses = [course for course, var in course_vars.items() if var.get()]
    selected_student = selected_student_id.get()
    selected_date = selected_date_entry.get()
    print("Applying Filter and Comparison with the following options:")
    print("Selected Courses:", selected_courses)
    print("Selected Student ID:", selected_student)
    print("Selected Date:", selected_date)

root = tk.Tk()
root.title("Filter and Compare")
root.geometry("800x600")

root.configure(bg="#f0f0f0")

heading = tk.Label(root, text="Filter and Compare", font=("Helvetica", 24, "bold"), pady=20, bg="#f0f0f0")
heading.pack()

csv_file_path_courses = "Data/courses.csv"
csv_file_path_students = "Data/studentInfo.csv"
course_list = load_courses(csv_file_path_courses)
student_list = load_students(csv_file_path_students)

left_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="solid")
left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y, expand=True)

dropdown_label = tk.Label(left_frame, text="Filter by Courses", font=("Helvetica", 14, "bold"), bg="#ffffff")
dropdown_label.pack(anchor="w", pady=5)

selected_course = tk.StringVar()
course_dropdown = ttk.Combobox(left_frame, textvariable=selected_course, values=course_list, state="readonly")
course_dropdown.pack(anchor="w", pady=5, padx=10)
course_dropdown.set("Select a Course")

student_filter_label = tk.Label(left_frame, text="Filter by Students", font=("Helvetica", 14, "bold"), bg="#ffffff")
student_filter_label.pack(anchor="w", pady=5)

selected_student_id = tk.StringVar()
student_dropdown = ttk.Combobox(left_frame, textvariable=selected_student_id, values=student_list, state="readonly")
student_dropdown.pack(anchor="w", pady=5, padx=10)
student_dropdown.set("Select a Student")

date_filter_label = tk.Label(left_frame, text="Filter by Date (yyyy-mm-dd)", font=("Helvetica", 14, "bold"), bg="#ffffff")
date_filter_label.pack(anchor="w", pady=5)

selected_date_entry = tk.Entry(left_frame, font=("Helvetica", 12), bg="#f0f0f0", bd=1)
selected_date_entry.pack(anchor="w", pady=5, padx=10)

separator = tk.Frame(root, width=2, bg="#d3d3d3", height=500)
separator.pack(side=tk.LEFT, fill=tk.Y)

right_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="solid")
right_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y, expand=True)

compare_label = tk.Label(right_frame, text="Compare Courses", font=("Helvetica", 14, "bold"), bg="#ffffff")
compare_label.pack(anchor="w", pady=5)

course_vars = {}
for course in course_list:
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(right_frame, text=course, variable=var, font=("Helvetica", 12), bg="#ffffff")
    checkbox.pack(anchor="w", pady=2)
    course_vars[course] = var

compare_button = tk.Button(right_frame, text="Compare Selected Courses", command=update_selected_courses_and_students, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", relief="raised")
compare_button.pack(pady=10, padx=10)

apply_filter_button = tk.Button(right_frame, text="Apply Filter and Compare options", command=apply_filter_and_compare, font=("Helvetica", 12, "bold"), bg="#2196F3", fg="white", relief="raised")
apply_filter_button.pack(pady=10, padx=10)

root.mainloop()