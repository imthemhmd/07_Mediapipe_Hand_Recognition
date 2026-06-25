# Welcome To Project Mediapipe
# In this project, we will detect which hand is being displayed.
# Note: This code can only detect two hands at the same time.

# imports
import cv2
import mediapipe as mp


mp_hand = mp.solutions.hands.Hands(max_num_hands=2)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame  = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hand.process(frameRGB)
    
    if result.multi_handedness:
        for hand in result.multi_handedness:
            hand_info = hand.classification[0].label
            if hand_info == "Right":
                cv2.putText(frame, str("Right"), (400, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (220,30,67), 3)
            if hand_info == "Left":
                cv2.putText(frame, str("Left"), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (220,30,67), 3)
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
