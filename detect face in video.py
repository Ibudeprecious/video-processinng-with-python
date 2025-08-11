import cv2

face_cascade = cv2.CascadeClassifier('faces.xml')

video = cv2.VideoCapture('video.mp4')

success, frame = video.read()

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # and save as .avi
output = cv2.VideoWriter('detect face in video.avi', fourcc, 30, (frame.shape[1], frame.shape[0]))


while success:
    faces = face_cascade.detectMultiScale(frame, 1.5, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 10)
    output.write(frame)
    success, frame = video.read()

output.release()
video.release()

print('done')
