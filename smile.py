import random
import cv2
import time
import os

face_cascade = cv2.CascadeClassifier(os.path.abspath("haarcascade_frontalface_default.xml"))
smile_cascade = cv2.CascadeClassifier(os.path.abspath("smile.xml"))

video = cv2.VideoCapture(0)
num = 0

def smile_meter(frame, x1, y1):
    global num

    if num > 4000:
        x = str(random.randint(0, 100))

        font = cv2.FONT_HERSHEY_COMPLEX
        color = (255,0,0)

        text = cv2.putText(frame, "Your smile is", (int(x1)+15, int(y1)-70),
                           font, 1, color, 4, cv2.LINE_AA)

        text = cv2.putText(frame, x + " %", (int(x1)+50, int(y1)-20), font, 1, color, 
                           4, cv2.LINE_AA)

        time.sleep(15)
        num = 0
        return num

    else: 
        x = str(random.randint(0, 100))
        font = cv2.FONT_HERSHEY_COMPLEX
        color = (255,0,0)

        text = cv2.putText(frame, "Smile Meter", (int(x1)+15,int(y1)-70), font, 1, color, 4,cv2.LINE_AA)
        text = cv2.putText(frame, x + " %", (int(x1)+50, int(y1)-20), font, 1, color, 
                    4, cv2.LINE_AA)
                    
        num += 5
        return num


while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for x,y,w,h in face:
        img = cv2.circle(frame, (x,y), 10,(0,100,255),-1)
        smile = smile_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=20)

        for x1,y1,w1,h1 in smile:
            img = cv2.rectangle(frame, (x1,y1), (x1+(w1),y1+(h1)), (255,0,0),3)
            smile_meter(frame,x,y)

    cv2.imshow("smile meter", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()