# Import the InferencePipeline object
from inference import InferencePipeline

# Import the built-in render_boxes sink for visualizing results
from inference.core.interfaces.stream.sinks import render_boxes

from response_functions import *
import json

# Load the Roboflow API key from the package.json file
with open("package.json", "r") as f:
    key = json.load(f)["robo_api"]


# initialize a pipeline object
pipeline = InferencePipeline.init(
    model_id="knife-detection-hgvy2/1", # Roboflow model to use
    video_reference=2, # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
    on_prediction=do, # Function to run after each prediction
    api_key=key
)
pipeline.start()
pipeline.join()
