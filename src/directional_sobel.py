import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure
from scipy import ndimage


#defining custom kernal


# Vertical continuity kernel (5x5)
kv = np.array([
    [-1, -1,  0,  1,  1],
    [-2, -2,  0,  2,  2],
    [-3, -3,  0,  3,  3],
    [-2, -2,  0,  2,  2],
    [-1, -1,  0,  1,  1]
], dtype=np.float32)

# Horizontal continuity kernel (5x5)
kh = np.array([
    [-1, -2, -3, -2, -1],
    [-1, -2, -3, -2, -1],
    [ 0,  0,  0,  0,  0],
    [ 1,  2,  3,  2,  1],
    [ 1,  2,  3,  2,  1]
], dtype=np.float32)

#applying convolution

gv = cv2.filter2D(img, -1, kv)
gh = cv2.filter2D(img, -1, kh)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Preprocessed")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(np.abs(gv), cmap='gray')
plt.title("Vertical Response")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(np.abs(gh), cmap='gray')
plt.title("Horizontal Response")
plt.axis('off')

plt.show()

#orientation map
mag_v = np.abs(gv).astype(np.float32)
mag_h = np.abs(gh).astype(np.float32)

eps = 1e-6
ratio = mag_h / (mag_v + eps)
orientation = np.zeros_like(mag_v, dtype=np.uint8)
orientation[ratio < 0.5] = 1
orientation[ratio > 2.0] = 2

mag_v = np.abs(gv).astype(np.float32)
mag_h = np.abs(gh).astype(np.float32)

eps = 1e-6
ratio = mag_h / (mag_v + eps)

orientation = np.zeros_like(mag_v, dtype=np.uint8)

vertical_mask   = (ratio < 0.7) & (mag_v > 30)
horizontal_mask = (ratio > 1.4) & (mag_h > 30)

orientation[vertical_mask] = 1
orientation[horizontal_mask] = 2

#visualization of orientation map

plt.figure(figsize=(6,6))
plt.imshow(orientation, cmap="hot")
plt.title("orientation map ( 1= vertical, 2 = horizontal)")
plt.axis("off")
plt.show()

#line clustering

vertical_mask = (orientation == 1).astype(np.uint8) * 255
horizontal_mask = (orientation == 2).astype(np.uint) * 255

#visualization of mask

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(vertical_mask, cmap='gray')
plt.title("Vertical Mask")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(horizontal_mask, cmap='gray')
plt.title("Horizontal Mask")
plt.axis('off')

plt.show()

#connected component labeling

from skimage import measure

labels_v = measure.label(vertical_mask, connectivity=2)
labels_h = measure.label(horizontal_mask, connectivity=2)

#visualization

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(labels_v, cmap='nipy_spectral')
plt.title("Vertical Wall Clusters")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(labels_h, cmap='nipy_spectral')
plt.title("Horizontal Wall Clusters")
plt.axis('off')

plt.show()

# Removes small noisy connected components and keeps only meaningful line segments
def filter_small_components(labels, min_size=100):
    output = np.zeros_like(labels)
    for region in measure.regionprops(labels):
        if region.area >= min_size:
            output[labels == region.label] = region.label
    return output
