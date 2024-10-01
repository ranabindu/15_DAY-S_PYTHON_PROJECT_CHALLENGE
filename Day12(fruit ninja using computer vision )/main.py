import mediapipe as mp
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import time
import win32api
import pyautogui

# Initialize MediaPipe drawing and hands solutions
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Capture video from the webcam
video = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while video.isOpened():
        _, frame = video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)  # Flip the image horizontally

        image_height, image_width, _ = image.shape

        # Process the image to find hand landmarks
        results = hands.process(image)

        # Convert the image back to BGR for OpenCV
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                # Draw hand landmarks
                mp_drawing.draw_landmarks(
                    image, hand, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2)
                )

            for hand_landmarks in results.multi_hand_landmarks:
                for point in range(len(hand_landmarks.landmark)):
                    # Get the normalized and pixel coordinates of the landmark
                    normalized_landmark = hand_landmarks.landmark[point]
                    pixel_coordinates_landmark = mp_drawing._normalized_to_pixel_coordinates(
                        normalized_landmark.x, normalized_landmark.y, image_width, image_height
                    )

                    if point == mp_hands.HandLandmark.INDEX_FINGER_TIP:
                        try:
                            # Draw a circle on the index fingertip
                            cv2.circle(image, (pixel_coordinates_landmark[0], pixel_coordinates_landmark[1]), 25, (0, 200, 0), 5)
                            
                            # Move the mouse cursor to the index fingertip's position and click
                            pyautogui.moveTo(x=pixel_coordinates_landmark[0], y=pixel_coordinates_landmark[1])
                            pyautogui.click(button='left')
                            
                        except Exception as e:
                            print(f"Error: {e}")

        # Display the image
        cv2.imshow("game", image)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Release the video capture and close windows
video.release()
cv2.destroyAllWindows()