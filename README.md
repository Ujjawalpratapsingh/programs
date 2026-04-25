# Hand Gesture Recognition for Cursor Control

This project uses computer vision to control the mouse cursor and perform clicks using hand gestures detected via webcam.

## Features

- **Cursor Movement**: Extend only your index finger to move the mouse cursor smoothly.
- **Click**: Curl your index, middle, and ring fingers completely to perform a left mouse click.

## Requirements

- Python 3.8+
- Webcam

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/hand-gesture-cursor.git
   cd hand-gesture-cursor
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Download the MediaPipe hand landmarker model (already included as `hand_landmarker.task`).

## Usage

Run the script:
```
python test.py
```

- A webcam window will open.
- Use gestures as described above.
- Press 'q' to quit.

## Dependencies

- opencv-python
- mediapipe
- pyautogui

## License

MIT