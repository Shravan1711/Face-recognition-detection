import cv2
import numpy as np
import os

#local binary patterns histogram
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml') #generated_after_training_faces_make_sure_to_write_correct_path
cascadePath = "cascades/data/haarcascade_frontalface_default.xml" #your_own_path
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
id = 0
names = ['Shravan'] #its_my_name_here_but_you_can_take_input_from_user_while_taking_the_images_and_append_it_in_this_list_dynamically
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5, minSize=(int(minW), int(minH)),)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #as low as possible
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        print(confidence)
        if (confidence < 100):
            id = names[id]
            #so actual confidence is 100-conf
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)


    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
print("\n Exit")
cam.release()
cv2.destroyAllWindows()
