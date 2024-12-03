from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def notifications():
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

    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Notifications</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f4f4f9;
            }
            .container {
                width: 50%;
                margin: auto;
            }
            .notification {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 15px;
                margin-bottom: 15px;
                background-color: #fff;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .notification p {
                margin: 0;
                font-size: 14px;
            }
            .button {
                padding: 10px 20px;
                background-color: #007BFF;
                color: #fff;
                text-decoration: none;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .button:hover {
                background-color: #0056b3;
            }
            .filter {
                margin-bottom: 20px;
                display: flex;
                align-items: center;
            }
            .filter label {
                font-weight: bold;
                margin-right: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Notifications</h1>
            <div class="filter">
                <label for="filter">Filter by:</label>
                <select id="filter">
                    <option>Most critical</option>
                </select>
            </div>
            {% for notification in notifications %}
            <div class="notification">
                <p>{{ notification.text }}</p>
                <button class="button">{{ notification.button_text }}</button>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """
    return render_template_string(template, notifications=notifications)

if __name__ == '__main__':
    app.run(debug=True)
