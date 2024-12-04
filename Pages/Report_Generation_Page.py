import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

# loading from CSV
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

csv_file_path_courses = "Data/courses.csv"
csv_file_path_students = "Data/studentInfo.csv"
course_list = load_courses(csv_file_path_courses)
student_list = load_students(csv_file_path_students)

# Beginning of page

def report_generation_page():
    page = tk.Tk()
    page.title("Report Generation Page")
    page.geometry("1000x800")

    title_lable = tk.Label(page, text="Generate Report", font=("Helvetica", 24))
    title_lable.pack(pady=20)

    # # Separator object
    # hseparator = ttk.Separator(page, orient='horizontal')
    # hseparator.place(anchor='n')

    frame1 = tk.Frame(page, width=500, height=200, bg="#f0f0f0")
    frame1.pack(side=tk.TOP)

    report_type_label = tk.Label(frame1, text='Report Type: ', font=("Helvetica", 14, "bold"))
    report_type_label.pack(side='left')
    button1 = tk.Button(frame1, text='Individual Student Report')
    button1.pack(side='left')
    button2 = tk.Button(frame1, text='Overall Course Report')
    button2.pack(side='left')
    # button3 = tk.Button(frame1, text='Overall Course Report (Multiple Courses)')
    # button3.pack(side='left')
    # button4 = tk.Button(frame1, text='Predictive Report')
    # button4.pack(side='left')

    frame2 = tk.Frame(page, bg="#ffffff", bd=2, relief="solid", width=500, height=500)
    frame2.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y, expand=True)

    separator = tk.Frame(page, width=2, bg="#d3d3d3", height=500)
    separator.pack(side=tk.LEFT, fill=tk.Y, pady=20)

    frame3 = tk.Frame(page, bg="#ffffff", bd=2, relief="solid", width=500, height=500)
    frame3.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y, expand=True)

# bottom left frame content, Report content options

    content_options_label = tk.Label(frame2, text='Report Content Options', font=("Helvetica", 14, "bold"))
    content_options_label.pack(side='top')
    # button2 = tk.Button(frame2, text='content Button')
    # button2.pack(side='left')

    # co_button_frame = tk.Frame(frame2)
    # co_button_frame.pack(side='top', padx=20, pady=20)
    #
    # co_button1 = tk.Button(co_button_frame, text='Opt1')
    # co_button1.grid(row=0, column=0)
    # co_button2 = tk.Button(co_button_frame, text='Opt2')
    # co_button2.grid(row=0, column=1)
    # co_button3 = tk.Button(co_button_frame, text='Opt3')
    # co_button3.grid(row=0, column=2)


    # filter_frame = tk.Frame(frame2, width=100, height=300)
    # filter_frame.pack(side='left')

    # filter_label = tk.Label(filter_frame, text='Filter By Date', font=("Helvetica", 10, "bold"))
    # filter_label.pack(side='top')



    # filter_listbox = tk.Listbox(filter_frame, selectmode=tk.SINGLE, font=("Helvetica", 10))
    # filter_listbox.pack(pady=10)
    # filter_listbox.insert(tk.END, "Sept 2024", "Oct 2024", "Nov 2024", "Dec 2024")

    # copied code

    filter_dropdown = tk.Label(frame2, text="Filter by Courses", font=("Helvetica", 14, "bold"), bg="#ffffff")
    filter_dropdown.pack(anchor="w", pady=5, padx=20)

    selected_course = tk.StringVar()
    course_dropdown = ttk.Combobox(frame2, textvariable=selected_course, values=course_list, state="readonly")
    course_dropdown.pack(anchor="w", pady=5, padx=20)
    course_dropdown.set("Select a Course")

    student_filter_label = tk.Label(frame2, text="Filter by Students", font=("Helvetica", 14, "bold"), bg="#ffffff")
    student_filter_label.pack(anchor="w", pady=5, padx=20)

    selected_student_id = tk.StringVar()
    student_dropdown = ttk.Combobox(frame2, textvariable=selected_student_id, values=student_list, state="readonly")
    student_dropdown.pack(anchor="w", pady=5, padx=20)
    student_dropdown.set("Select a Student")

    date_filter_label = tk.Label(frame2, text="Filter by Date (yyyy-mm-dd)", font=("Helvetica", 14, "bold"),
                                 bg="#ffffff")
    date_filter_label.pack(anchor="w", pady=5, padx=20)

    selected_date_entry = tk.Entry(frame2, font=("Helvetica", 12), bg="#f0f0f0", bd=1)
    selected_date_entry.pack(anchor="w", pady=5, padx=20)

    # copied code ends

    proto_visual = tk.Label(frame2, text='Prototype Visualization View Selection', font=("Helvetica", 10, "bold"))
    proto_visual.pack(side=tk.TOP, pady=20, padx=20)

    vis_icons_png = tk.PhotoImage(file="visicons2.PNG")
    vis_icons = ttk.Label(frame2, image=vis_icons_png)
    vis_icons.pack(side=tk.TOP,pady=5, padx=20)

# bottom right frame, Custom report options

    custom_options_label = tk.Label(frame3, text='Custom Report Options', font=("Helvetica", 14, "bold"))
    custom_options_label.pack(side='top')
    # button3 = tk.Button(frame3, text='Custom button')
    # button3.pack(side='left')

    cu_button_frame = tk.Frame(frame3)
    cu_button_frame.pack(side='top', padx=20, pady=20)

    # cu_button1 = tk.Button(cu_button_frame, text='Opt1')
    # cu_button1.grid(row=0, column=0)
    # cu_button2 = tk.Button(cu_button_frame, text='Opt2')
    # cu_button2.grid(row=0, column=1)
    # cu_button3 = tk.Button(cu_button_frame, text='Opt3')
    # cu_button3.grid(row=0, column=2)
    # cu_button4 = tk.Button(cu_button_frame, text='Opt4')
    # cu_button4.grid(row=1, column=0)
    # cu_button5 = tk.Button(cu_button_frame, text='Opt5')
    # cu_button5.grid(row=1, column=1)
    # cu_button6 = tk.Button(cu_button_frame, text='Opt6')
    # cu_button6.grid(row=1, column=2)

    format_frame = tk.Frame(frame3)
    format_frame.pack(side=tk.TOP, padx=20, pady=40,)

    format_button1 = tk.Button(format_frame, text='.txt')
    format_button1.grid(row=0, column=0)
    format_button2 = tk.Button(format_frame, text='PDF')
    format_button2.grid(row=0, column=1)
    # format_button3 = tk.Button(format_frame, text='Other')
    # format_button3.grid(row=0, column=2)
    format_button4 = tk.Button(format_frame, text='Generate Report', bg='blue', command=report_generation_confirm)
    format_button4.grid(row=0, column=3)



    ###

    ###

    page.mainloop()

def report_generation_confirm():
    messagebox.showinfo("Attention", f"Report has been generated")


report_generation_page()