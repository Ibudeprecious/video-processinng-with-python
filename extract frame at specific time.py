import cv2

video = cv2.VideoCapture('video.mp4')
fps = int(video.get(cv2.CAP_PROP_FPS))

timestamp = "00:00:02.9" # Specify the timestamp to extract frame
hrs, min, sec = timestamp.split(':')
frame_position = float((float(hrs) * 3600 + float(min) * 60 + float(sec))*fps)


video.set(1, frame_position)  # Set the frame position
success, frame = video.read()
if success:
    cv2.imwrite('extracted_frame.jpg', frame)
    print(f"Frame extracted at {timestamp}.")
