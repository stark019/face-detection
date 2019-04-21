import cv2
 
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
 
while True:
 
    ret, frame = cap.read()
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
 
    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30))
 
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,
            (x,y),  #top left
            (x+w, y+h), #bottom right
            (0,0,255),2 #rgb value of color
            )
    if len(faces)>=1:
        print(len(faces))
    cv2.imshow('camera', frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()

