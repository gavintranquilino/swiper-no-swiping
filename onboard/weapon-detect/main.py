import roboflow

with open("ROBOFLOW_API_KEY", "r") as file:
    key = file.readline().strip()

rf = roboflow.Roboflow(api_key=key)