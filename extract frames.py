import cv2

video = cv2.VideoCapture('video.mp4')
count = 0

success, frame = video.read()

while success:
    count += 1
    cv2.imwrite(f'frames/frame_{count}.jpg', frame)
    success, frame = video.read()

print(f"Extracted {count} frames.")
