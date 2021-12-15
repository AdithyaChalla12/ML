import cv2

face_cascade=cv2.CascadeClassifier('C:/Users/adith/OneDrive/Desktop/Adithya/My Projects/Facial Recg/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/adith/OneDrive/Desktop/Adithya/My Projects/Facial Recg/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret,img = cap.read()
    # Our operations on the frame come here
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converting into grayscale image
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # Creating dimensions of face
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)#Creating dimensions of eyes
        
    cv2.imshow('img',img)
    k=cv2.waitKey(30)&0xFF
    if k==27:
        break
            
cap.release()
cv2.destroyAllWindows()