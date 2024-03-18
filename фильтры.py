import cv2

cap = cv2.VideoCapture(0)

#0 16 66
#75 255 88

while True:
    return_code, img = cap.read()
    if return_code:
        #print(type(img), img)
        cv2.imshow("Original", img)
        cv2.imshow("Gray", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
        cv2.imshow("HSV", cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
        key = cv2.waitKey(1)
        if key == 27: break
    else:
        print("Не удалось получить изображение с камеры")

cap.release()
cv2.destroyAllWindows()
