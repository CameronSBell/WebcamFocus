import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
min_focus = 600       # Focal value for the camera.
neutral_focus = 215
last_set_focus = neutral_focus

while True:
    # ret, frame = cap.read()

    # Throw the frame onto a window - note that the name here matters and associated with an already open window
#     cv2.imshow("Stream Video",frame)
    cv2.imshow("Stream Video", np.zeros([200,250,1],dtype="uint8"))

    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        break

    if key == ord('m'): 
        increment = 1 if last_set_focus <= min_focus else -1
        for transition_focus_level in range(last_set_focus, min_focus + increment, increment*5):
            print(transition_focus_level)
            cap.set(cv2.CAP_PROP_FOCUS, transition_focus_level)  # Focus
            time.sleep(1 / 1000)
        last_set_focus = min_focus

    if key == ord('g'):
        focus_amount = cap.get(cv2.CAP_PROP_FOCUS)  # Focus
        fps = cap.get(cv2.CAP_PROP_FPS)
        print(focus_amount)
        print(fps)

    if key == ord('n'):
        increment = 1 if last_set_focus <= neutral_focus else -1
        for transition_focus_level in range(last_set_focus, neutral_focus + increment, increment*5):
            print(transition_focus_level)
            cap.set(cv2.CAP_PROP_FOCUS, transition_focus_level)  # Focus
            time.sleep(1 / 1000)
            
        last_set_focus = neutral_focus

    # if key == ord(','):
#         cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)  # Focus

cap.release()
cv2.destroyAllWindows()
