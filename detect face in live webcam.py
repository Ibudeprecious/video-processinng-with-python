import cv2

face_cascade = cv2.CascadeClassifier('faces.xml')

video = cv2.VideoCapture(0)

success, frame = video.read()

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # and save as .avi
output = cv2.VideoWriter('detect face in live webcam.avi', fourcc, 15, (frame.shape[1], frame.shape[0]))


while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 3, minSize=(100, 100))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 255), 4)
    output.write(frame)
    cv2.imshow('recording', frame)
    key = cv2.waitKey(1)
    if key == ord('k'):
        break
    success, frame = video.read()

output.release()
video.release()
cv2.destroyAllWindows()

print('done')
