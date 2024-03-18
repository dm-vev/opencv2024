import cv2
import numpy as np

cam = cv2.VideoCapture(0)

success, frame = cam.read()

print(success, frame.shape, type(frame[10, 20, 1]))

width = frame.shape[1]
height = frame.shape[0]
print(f'Разрешение: {width}x{height}')

while (True):
    # read
    success, frame = cam.read()

    #process
    min_line = int(min(height, width))
    height_add = 0 if min(height, width) == height else (height - width) // 2
    width_add = 0 if min(height, width) == width else (width - height) // 2

    frame[int(min_line * 0.25)+height_add:int(min_line * 0.75)+height_add, int(min_line * 0.25) + width_add:int(min_line * 0.75) + width_add, 0:1] = 255
    #frame = 255 - frame

    #if (np.random.randint(4) == 3):
    #   frame[100:700, 100:1200, 1] = frame[120:720, 130:1230, 1]

    # if (np.random.randint(3) == 2):
    #    frame[:, :, 2] = frame[:, :, 1]

    #if (np.random.randint(3) == 2):
    #    frame[:, 100:200, :] = 255 - frame[:, 100:200, :]

    # output
    cv2.imshow("frame", frame)

    # process keyboard
    #key = cv2.waitKey(50) & 0xFF
    key = cv2.waitKey(1)
    if key == 27: break

cv2.waitKey(0)
cam.release()
cv2.destroyAllWindows()
cv2.waitKey(10)
