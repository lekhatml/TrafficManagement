import numpy as np
import cv2
import datetime
def recordVideo():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    r = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]
    fpath = "videos/" + r + '.avi'
    out = cv2.VideoWriter(fpath, fourcc, 20.0, (640, 480))
    while (True):
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('Video Recording', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()
