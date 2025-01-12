import roboflow
import cv2

with open("ROBOFLOW_API_KEY", "r") as file:
    key = file.readline().strip()

rf = roboflow.Roboflow(api_key=key)

# Load the specific model using the provided ID
project = rf.workspace().project("knife-detection-hgvy2")
model = project.version(1).model

# Open the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)


# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Process the live video feed
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Save the current frame as a temporary image
    temp_image_path = "temp_frame.jpg"
    cv2.imwrite(temp_image_path, frame)

    # Use the Roboflow model to predict on the current frame
    result = model.predict(temp_image_path, confidence=40, overlap=30).json()

    # Draw predictions on the frame
    for prediction in result["predictions"]:
        x, y, width, height = prediction["x"], prediction["y"], prediction["width"], prediction["height"]
        label = prediction["class"]
        confidence = prediction["confidence"]

        # Calculate the bounding box coordinates
        start_point = (int(x - width / 2), int(y - height / 2))
        end_point = (int(x + width / 2), int(y + height / 2))

        # Draw the bounding box and label
        color = (0, 0, 255)  # Red bounding box for knife detection
        cv2.rectangle(frame, start_point, end_point, color, 2)
        cv2.putText(frame, f"{label} ({confidence:.1f}%)", (start_point[0], start_point[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Display the frame with predictions
    cv2.imshow("Knife Detection - Live Feed", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
# Load your project and model
project = rf.workspace().project("your-project-name")
model = project.version("version-number").model

# Open the webcam (0 is usually the default camera, adjust if needed)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Process the live video feed
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Save the current frame as a temporary image
    temp_image_path = "temp_frame.jpg"
    cv2.imwrite(temp_image_path, frame)

    # Use Roboflow to predict on the current frame
    result = model.predict(temp_image_path, confidence=40, overlap=30).json()

    # Draw predictions on the frame
    for prediction in result["predictions"]:
        x, y, width, height = prediction["x"], prediction["y"], prediction["width"], prediction["height"]
        label = prediction["class"]
        confidence = prediction["confidence"]

        # Calculate the bounding box coordinates
        start_point = (int(x - width / 2), int(y - height / 2))
        end_point = (int(x + width / 2), int(y + height / 2))

        # Draw the bounding box and label
        color = (0, 255, 0)  # Green
        cv2.rectangle(frame, start_point, end_point, color, 2)
        cv2.putText(frame, f"{label} ({confidence:.1f}%)", (start_point[0], start_point[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Display the frame with predictions
    cv2.imshow("Live Camera - Roboflow Predictions", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
