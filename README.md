Real-Time Object Detection with YOLOv10
This project demonstrates a simple yet powerful real-time object detection application using the YOLOv10 model. The application captures a video stream from a webcam and identifies objects within the frame, displaying the detected class and confidence score.

Files
main.py: The core Python script that handles webcam access, object detection using the YOLOv10 model, and drawing bounding boxes and labels on the video feed.
yolov10n.pt: The pre-trained YOLOv10 Nano model weights. This file is required for the object detection to work.
ab.jpg: An example image file that was provided for context.

Requirements
To run this project, you need to have the following libraries installed:

ultralytics
cvzone
opencv-python

You can install these dependencies using pip:    pip install ultralytics
                                                 pip install cvzone
                                                 pip install opencv-python

How to Run
1.Clone this repository to your local machine.
2.Make sure you have all the required libraries installed.
3.Place the yolov10n.pt model file in the same directory as the main.py script.
4.Run the main script from your terminal:    python main.py

A window will open, showing a live video feed from your webcam. The application will draw a red bounding box around detected objects and display the object's class name and the detection confidence percentage.

Features
Real-time Object Detection: Uses your webcam to perform live object detection.
YOLOv10 Model: Leverages the high-performance YOLOv10n model for fast and accurate detections.
Confidence Scores: Displays the confidence percentage for each detected object.
Simple UI: Provides a straightforward visual output with bounding boxes and text labels.

How It Works
The main.py script initializes the YOLOv10 model with the yolov10n.pt weights. It then enters a loop that continuously reads frames from the webcam. For each frame, it uses the model to perform object detection. The script then iterates through the detection results, extracting the bounding box coordinates, class, and confidence score for each detected object. Finally, it uses cvzone and cv2 to draw the bounding boxes and text on the frame before displaying it.The loop can be exited by pressing the 'q' key.
