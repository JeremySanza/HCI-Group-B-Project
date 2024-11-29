import tkinter as tk

def starred_courses_page():
    page = tk.Tk()
    page.title("Starred Courses Page")
    page.geometry("600x600")

    title_lable = tk.Label(page, text="Starred Courses Page", font=("Arial", 20))
    title_lable.pack(pady=20)

    ###

    ###

    page.mainloop()


starred_courses_page()