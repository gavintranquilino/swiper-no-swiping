# Import the InferencePipeline object
from inference import InferencePipeline

# Import the built in render_boxes sink for visualizing results
from inference.core.interfaces.stream.sinks import render_boxes
from response_functions import *


# main program
with open("ROBOFLOW_API_KEY", "r") as file:
    key = file.readline().strip()

# initialize a pipeline object
pipeline = InferencePipeline.init(
    model_id="knife-detection-hgvy2/1", # Roboflow model to use
    video_reference=0, # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
    on_prediction=foo, # Function to run after each prediction
    api_key=key
)
pipeline.start()
pipeline.join()
