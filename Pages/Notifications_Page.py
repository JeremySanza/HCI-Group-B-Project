import tkinter as tk
from tkinter import ttk

notifications = [
    {
        "text": '2 students in the course "Course34" have had a significant drop in engagement. Please see Course34\'s dashboard for more details.',
        "button_text": "Go to dashboard"
    },
    {
        "text": 'The overall engagement for "Course4" has dropped by 5% in the past month. Please see Course4\'s dashboard for more details.',
        "button_text": "Go to dashboard"
    },
    {
        "text": '5 students in the course "Course63" have had a minor drop in engagement in the past 2 months. Please see Course63\'s dashboard for more details.',
        "button_text": "Go to dashboard"
    }
]

def on_button_click(course_name):
    print(f"Opening dashboard for {course_name}...")

root = tk.Tk()
root.title("Notifications")
root.geometry("600x400")
root.configure(bg="#f4f4f9")

container = tk.Frame(root, bg="#f4f4f9")
container.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

title_label = tk.Label(container, text="Notifications", font=("Arial", 16), bg="#f4f4f9")
title_label.pack(anchor="w", pady=(0, 10))

filter_frame = tk.Frame(container, bg="#f4f4f9")
filter_frame.pack(anchor="w", pady=(0, 10))

filter_label = tk.Label(filter_frame, text="Filter by:", font=("Arial", 12), bg="#f4f4f9")
filter_label.pack(side=tk.LEFT, padx=(0, 10))

filter_combobox = ttk.Combobox(filter_frame, values=["Most critical"], state="readonly")
filter_combobox.set("Most critical")
filter_combobox.pack(side=tk.LEFT)

notifications_frame = tk.Frame(container, bg="#f4f4f9")
notifications_frame.pack(fill=tk.BOTH, expand=True)

for notification in notifications:
    notification_frame = tk.Frame(notifications_frame, bg="#fff", relief=tk.RIDGE, borderwidth=1)
    notification_frame.pack(fill=tk.X, pady=5, padx=5)

    text_label = tk.Label(notification_frame, text=notification["text"], font=("Arial", 10), bg="#fff", anchor="w", wraplength=400, justify="left")
    text_label.pack(side=tk.LEFT, padx=10, pady=10, expand=True)

    button = tk.Button(notification_frame, text=notification["button_text"], bg="#007BFF", fg="white", font=("Arial", 10), cursor="hand2",
                       command=lambda course_name=notification["text"].split('"')[1]: on_button_click(course_name))
    button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
