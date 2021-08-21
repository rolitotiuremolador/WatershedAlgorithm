import cv2
from matplotlib import pyplot as plt

img = cv2.imread('water_coins.jpg')
img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

plt.figure("Binary")
plt.imshow(thresh,cmap='gray')

plt.figure("Grayscale")
plt.imshow(gray)

plt.show()