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


def read_csv():
    x_data = []
    y_data = []

    with open('Data/red_studentVLE.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                day_num = row['date']
                x_data.append(day_num)

                sum_click = float(row['sum_click'])
                y_data.append(sum_click)
            except KeyError as e:
                print(f"Missing column: {e}")
            except ValueError as e:
                print(f"Error parsing data: {e}")

    return x_data, y_data


def diseng_plot(x_data, y_data):
    mp.scatter(x_data, y_data, color='blue', marker='o')  # Scatter plot
    mp.xlabel('Date')
    mp.ylabel('Sum of Clicks')
    mp.title('Disengagement Metric')
    mp.xticks(rotation=45)
    mp.grid(True)
    mp.tight_layout()
    mp.show()


# Function to handle button click in Tkinter
def on_button_click():
    x_data, y_data = read_csv()
    diseng_plot(x_data, y_data)


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

        d_button = tk.Button(page, text="Alternative Disengagement Metric", command=on_button_click)
        d_button.pack(pady=10)

        exit = tk.Button(page, text="Close", command=page.destroy)
        exit.pack(pady=20)

    page.mainloop()

course_analytics_page()

#
# ###################################
#
# import tkinter as tk
# import csv
# import matplotlib.pyplot as mp
# # from datetime import datetime
#
#
# def read_csv(file_name):
#     x_data = []
#     y_data = []
#
#     with open('Data/red_studentVLE.csv', mode='r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             try:
#                 day_num = row['date']
#                 x_data.append(day_num)
#
#                 sum_click = float(row['sum_click'])
#                 y_data.append(sum_click)
#             except KeyError as e:
#                 print(f"Missing column: {e}")
#             except ValueError as e:
#                 print(f"Error parsing data: {e}")
#
#     return x_data, y_data
#
#
# def diseng_plot(x_data, y_data):
#     mp.scatter(x_data, y_data, color='blue', marker='o')  # Scatter plot
#     mp.xlabel('Date')
#     mp.ylabel('Sum of Clicks')
#     mp.title('Disengagement Metric')
#     mp.xticks(rotation=45)
#     mp.grid(True)
#     mp.tight_layout()
#     mp.show()
#
#
# # Function to handle button click in Tkinter
# def on_button_click():
#     file_name = 'Data/red_studentVLE.csv'  # Static file path
#     x_data, y_data = read_csv(file_name)
#     diseng_plot(x_data, y_data)
#
# #
# #
# # # Create a label and entry widget to take the CSV file path as input
# # label = tk.Label(root, text="This will use 'Data/red_studentVLE.csv'.")
# # label.pack()
# #
# # # Create a button that triggers the plot when clicked
# #
# #
# # # Start the Tkinter main loop
# # root.mainloop()
# #
#
#
