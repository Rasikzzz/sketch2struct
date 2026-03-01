import cv2
import numpy as np
import matplotlib.pyplot as plt

#preprocessing
def preprocess(img_path):
  img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
  blur = cv2.GaussianBlur(img, (5,5),0)
  _, binary = cv2.threshold(
      blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
  )
  if np.mean(binary) > 127:
    binary = 255 - binary

  kernal = np.ones((3,3),np.uint8)
  clean = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernal, iterations=1)
  return clean

#pre process testing
img = preprocess("test1.png")

plt.imshow(img, cmap="gray")
plt.title("preprocessing sketch")
plt.axis("off")
plt.show()
