import requests

# Import the InferencePipeline object
from inference import InferencePipeline

# Import the built-in render_boxes sink for visualizing results
from inference.core.interfaces.stream.sinks import render_boxes
import json

# with open("package.json", "r") as f:
#     USER_KEY = json.load(f)["USER_KEY"]
#     API_TOKEN = json.load(f)["API_TOKEN"]
API_TOKEN = "a892tzxa63k7fwu4xkzwa3jq9nbsy1"
USER_KEY = "uu21rofynz9dppstoao5kz2qc7smre"

def send_pushover_notification(user_key, api_token, message,
                               title="Notification"):
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
            print(
                f"Failed to send notification: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error while sending notification: {e}")


def on_prediction_with_pushover(predictions, frame):
    print(predictions)
    try:
        if not isinstance(predictions, dict):
            print("Invalid predictions format:", predictions)
            return

        for prediction in predictions.get("predictions", []):
            if prediction.get("class") == "Knife" and prediction.get("confidence") > 0.5:
                # Send Pushover notification
                send_pushover_notification(
                    user_key=USER_KEY,
                    api_token=API_TOKEN,
                    message="A knife was detected in the live feed. Please check immediately!",
                    title="Knife Detection Alert"
                )
                print("Notification sent for knife detection.")
                break
    except Exception as e:
        print(f"Error processing predictions: {e}")


def do(predictions, frame):
    render_boxes(predictions, frame)
    on_prediction_with_pushover(predictions, frame)
