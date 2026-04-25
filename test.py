import cv2
import mediapipe as mp
import pyautogui
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Initialize MediaPipe Hand Landmarker
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)
landmarker = vision.HandLandmarker.create_from_options(options)

# Get screen size
screen_width, screen_height = pyautogui.size()

# Open webcam
cap = cv2.VideoCapture(0)

# Variables to track gestures
smoothed_x = None
smoothed_y = None
alpha = 0.1  # Smoothing factor (lower = smoother)
clicked = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Create MediaPipe Image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

    # Process the image with Hand Landmarker
    result = landmarker.detect(mp_image)

    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:
            # Get landmark positions (normalized 0-1)
            landmarks = hand_landmarks

            # Check finger states
            thumb_up = landmarks[4].y < landmarks[3].y
            index_up = landmarks[8].y < landmarks[6].y
            middle_up = landmarks[12].y < landmarks[10].y
            ring_up = landmarks[16].y < landmarks[14].y
            pinky_up = landmarks[20].y < landmarks[18].y

            # Check if only index finger is up
            index_only = index_up and not thumb_up and not middle_up and not ring_up and not pinky_up

            palm_closed = not index_up and not middle_up and not ring_up  # Click only when index, middle, ring are completely curled

            # Click if palm closed and not already clicked
            if palm_closed and not clicked:
                pyautogui.click()
                clicked = True
                print("Mouse clicked")
            elif not palm_closed:
                clicked = False

            # Move cursor if only index finger is up (virtual cursor follows index finger)
            if index_only:
                index_tip = landmarks[8]
                current_x = index_tip.x * screen_width
                current_y = index_tip.y * screen_height
                
                if smoothed_x is None:
                    smoothed_x = current_x
                    smoothed_y = current_y
                else:
                    smoothed_x = alpha * current_x + (1 - alpha) * smoothed_x
                    smoothed_y = alpha * current_y + (1 - alpha) * smoothed_y
                
                x = int(smoothed_x)
                y = int(smoothed_y)
                pyautogui.moveTo(x, y)
                print(f"Cursor moved to ({x}, {y})")

            # Draw hand landmarks (optional, for visualization)
            # Note: Drawing might need adjustment for new API

    # Display the frame
    cv2.imshow('Hand Gesture Recognition', frame)

    # Break loop on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
landmarker.close()