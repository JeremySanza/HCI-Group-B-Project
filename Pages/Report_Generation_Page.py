import tkinter as tk

def report_generation_page():
    page = tk.Tk()
    page.title("Report Generation Page")
    page.geometry("600x600")

    title_lable = tk.Label(page, text="Report Generation Page", font=("Arial", 20))
    title_lable.pack(pady=20)

    ###

    ###

    page.mainloop()


report_generation_page()