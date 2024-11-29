import tkinter as tk

def notifications_page():
    page = tk.Tk()
    page.title("Notifications Page")
    page.geometry("600x600")

    title_lable = tk.Label(page, text="Notifications Page", font=("Arial", 20))
    title_lable.pack(pady=20)

    ###

    ###

    page.mainloop()


notifications_page()