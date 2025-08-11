import cv2

video = cv2.VideoCapture('video.mp4')

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
no_frame = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))

print(f"Width: {width}")
print(f"Height: {height}")
print(f"Number of Frames: {no_frame}")
print(f"FPS: {fps}")
