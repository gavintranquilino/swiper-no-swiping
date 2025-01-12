import requests

# Import the InferencePipeline object
from inference import InferencePipeline

# Import the built in render_boxes sink for visualizing results
from inference.core.interfaces.stream.sinks import render_boxes


def foo(predictions, frame):
    print("hi")
    render_boxes(predictions, frame)


def send_pushover_notification(user_key, api_token, message, title="Notification"):
    try:
        # Pushover API endpoint
        url = "https://api.pushover.net/1/messages.json"

        # Data payload
        payload = {
            "token": api_token,
            "user": user_key,
            "message": message,
            "title": title,
        }

        # Send the POST request to Pushover
        response = requests.post(url, data=payload)

        # Check for successful response
        if response.status_code == 200:
            print("Pushover notification sent!")
        else:
            print(f"Failed to send notification: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error while sending notification: {e}")
