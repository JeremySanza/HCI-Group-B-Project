import tkinter as tk
import subprocess as sp

def course_analytics_page():
    sp.run(["python", "Pages/Course_Analytics_Page.py"])

def starred_courses_page():
    sp.run(["python", "Pages/Starred_Courses_Page.py"])

def filter_compare_page():
    sp.run(["python", "Pages/Filter_Compare_Page.py"])

def notifications_page():
    sp.run(["python", "Pages/Notifications_Page.py"])

def report_generation_page():
    sp.run(["python", "Pages/Report_Generation_Page.py"])


root = tk.Tk()
root.title("Student Engagement Tool")
root.geometry("250x320")

title_lable = tk.Label(root, text="Main Menu", font=("Arial", 20))
title_lable.pack(pady=20)

tk.Button(root, text="Course Analytics Page", command=course_analytics_page).pack(pady=10)
tk.Button(root, text="Starred Courses Page", command=starred_courses_page).pack(pady=10)
tk.Button(root, text="Filter and Compare Page", command=filter_compare_page).pack(pady=10)
tk.Button(root, text="Notifications Page", command=notifications_page).pack(pady=10)
tk.Button(root, text="Report Generation Page", command=report_generation_page).pack(pady=10)

root.mainloop()