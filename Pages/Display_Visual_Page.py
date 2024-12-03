import tkinter as tk

def create_visual_page(root, selected_courses, selected_student, selected_date):
    visual_window = tk.Toplevel(root)
    visual_window.title("Visualise Data")
    visual_window.geometry("800x600")

    info_label = tk.Label(visual_window, text=f"Visualisation with the following data:\n\n"
                                              f"Selected Courses: {', '.join(selected_courses)}\n"
                                              f"Selected Student: {selected_student}\n"
                                              f"Selected Date: {selected_date}", font=("Helvetica", 14))
    info_label.pack(pady=50)

    def exit_app():
        visual_window.destroy()
        root.quit()
        root.destroy()

    exit_button = tk.Button(visual_window, text="Exit", command=exit_app, font=("Helvetica", 12, "bold"), bg="#FF5733", fg="white")
    exit_button.pack(pady=20)
