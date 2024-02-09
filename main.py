import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

# Start the video capture
cap = cv2.VideoCapture(0)

# Set the video resolution
cap.set(3, 720)
cap.set(4, 420)

# Create a keyboard controller object
keyboard = Controller()

# Initialize the hand detector
detector = HandDetector(detectionCon=0.6, maxHands=2)

# Define a conditions to press and release a keyboard key
# Define a conditions to control the Hill Climb Racing game
# Start the infinite loop
while True:
    
    # Read a frame from the video capture
    success, img = cap.read()
    
    # Detect hands in the frame
    hands, img = detector.findHands(img)
    
    if hands:
        fingers = detector.fingersUp(hands[0])
        if fingers == [0, 0, 0, 0, 0]:
            keyboard.press(Key.left)
            keyboard.release(Key.right)
        elif fingers == [1, 1, 1, 1, 1]:
            keyboard.press(Key.right)
            keyboard.release(Key.left)
            
        # elif fingers == [1, 0, 0, 0, 0]:  
        #      keyboard.press(Key.enter)
        #      keyboard.release(Key.enter)
                          
    else:
        keyboard.release(Key.left)
        keyboard.release(Key.right)
        
     # Display the frame    
    cv2.imshow("Let's Play", img)
    
    # Check if the 'q' key is pressed
    if cv2.waitKey(1) == ord("q"):
     break

   

    














  


