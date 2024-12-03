import tkinter as tk
import csv
import matplotlib.pyplot as mp

def courseBarChart(registration, unRegistration):
    courses = list(registration.keys())
    registrations = list(registration.values())
    unregistrations = list(unRegistration.values())

    x = range(len(courses))

    mp.bar([pos - 0.2 for pos in x], registrations, width=0.4, label="Total Registrations", align="center")
    mp.bar([pos + 0.2 for pos in x], unregistrations, width=0.4, label="Total Registrations", align="center")

    mp.xlabel('Course Code')
    mp.ylabel('Student Registrations (blue:registrations, orange:unregistrations)')
    mp.show()


def course_analytics_page():
    page = tk.Tk()
    page.title("Course Analytics Page")
    page.geometry("600x350")

    title_lable = tk.Label(page, text="Course Analytics Page", font=("Arial", 20))
    title_lable.pack(pady=20)

    with open("Data/studentRegistration.csv", mode="r") as file:
        csvFile = csv.DictReader(file)
        courseColumn = "code_module"
        dateColumn = "date_unregistration"
        registration = {"AAA": 0, "BBB": 0, "CCC": 0, "DDD": 0, "EEE": 0, "FFF": 0, "GGG": 0}
        unRegistration = {"AAA": 0, "BBB": 0, "CCC": 0, "DDD": 0, "EEE": 0, "FFF": 0, "GGG": 0}
        count = 0

        row = 1
        for row in csvFile:
            count += 1
            registration[row[courseColumn]] += 1
            if not str(row[dateColumn]) == '':
                unRegistration[row[courseColumn]] += 1
                count -= 1

        title_lable = tk.Label(page, text="Total Students: " + str(count), font=("Arial", 15))
        title_lable.pack(pady=20)

        title_lable = tk.Label(page, text="Courses: " + str(list(registration.keys())), font=("Arial", 15))
        title_lable.pack(pady=10)

        button = tk.Button(page, text="View Course Disengagement", command=lambda: courseBarChart(registration, unRegistration))
        button.pack(pady=10)

        exit = tk.Button(page, text="Close", command=page.destroy)
        exit.pack(pady=20)

    page.mainloop()

course_analytics_page()