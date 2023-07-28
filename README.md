# Gesture Control for Hill Climb Racing

<img width="960" alt="Screenshot 2023-07-27 122033" src="https://github.com/Sudhanshu1st/gesture_gaming/assets/109865453/1dcd0acb-3095-4fe7-bf05-007773153fb3">

This project allows you to control the popular game "Hill Climb Racing" using hand gestures captured by a webcam. The program utilizes the OpenCV library for hand tracking and gesture recognition, enabling you to steer the in-game vehicle by moving your hand.

## Requirements

Before running the code, make sure you have the following libraries installed:

- OpenCV (cv2)
- CVZone (HandTrackingModule)
- Pynput (keyboard)

You can install these libraries using pip:

```
pip install opencv-python
pip install cvzone
pip install pynput
```

## How to Run

1. Ensure that your webcam is properly connected to your computer.

2. Download or copy the provided Python script to your local environment.

3. Run the Python script:

   ```
   python your_file_name.py
   ```

4. The webcam window will open, and the program will begin detecting your hand.

## Hand Gesture Controls

The hand gestures recognized by the program correspond to the following actions in the game:

1. **Fist Gesture**: Steer Left/ Break 

   When you make a fist with your hand, the in-game vehicle will steer to the left.

2. **Five Fingers Gesture**: Steer Right/ Accelerate 

   When you open your hand with all five fingers extended, the in-game vehicle will steer to the right.

3. **Any Other Gesture or No Hand Detected**: Neutral

   If you show any other hand gesture or if your hand is not detected, the vehicle will maintain a neutral position in the game.

## Exiting the Program

To exit the program, press the "q" key while the webcam window is in focus. This will terminate the script and close the webcam feed.

## Important Notes

- Adjust the `detectionCon` and `maxHands` parameters in the `HandDetector` constructor based on your camera setup and hand recognition accuracy requirements.

- Ensure that your environment has access to the required camera (usually the default webcam) to capture the video feed.

- The success of the gesture control may vary depending on lighting conditions and the position of your hand in front of the camera.

## Disclaimer

This project is intended for educational and personal use. Please make sure to use the gesture control responsibly and avoid any distractions while playing games. The authors of this project are not responsible for any misuse or accidents that may occur while using this code.

**Have fun playing Hill Climb Racing with your hands!**
