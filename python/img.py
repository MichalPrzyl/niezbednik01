import cv2


img = cv2.imread("tapeta.jpg")

cutter = 25


width = int(img.shape[1] * cutter / 100)
height = int(img.shape[0] * cutter / 100)


img2 = cv2.resize(img, (width, height))

img3 = cv2.bitwise_not(img2)

while 1:

    cv2.imshow("TITLE", img3)

    key=cv2.waitKey(0)
    if key == ord('q'):
        break