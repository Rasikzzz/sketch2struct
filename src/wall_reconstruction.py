# Fits a straight vertical line for each connected component by averaging x-coordinates

def fit_vertical_lines(labels):
  h,w = labels.shape
  output = np.zeros((h,w),dtype=np.uint8)

  for region in measure.regionprops(labels):
    coords = region.coords

    ys = coords[:, 0]
    xs = coords[:, 1]

    x_mean = int(np.mean(xs))

    y_min = np.min(ys)
    y_max = np.max(ys)

    cv2.line(output, (x_mean, y_min),(x_mean, y_max),255,2)
  return output

# Fits a straight horizontal line for each connected component by averaging y-coordinates

def fit_horizontal_lines(labels):
    h, w = labels.shape
    output = np.zeros((h, w), dtype=np.uint8)

    for region in measure.regionprops(labels):
        coords = region.coords
        ys = coords[:, 0]
        xs = coords[:, 1]


        y_mean = int(np.mean(ys))

        x_min = np.min(xs)
        x_max = np.max(xs)

        cv2.line(output, (x_min, y_mean), (x_max, y_mean), 255, 2)

    return output

# Reconstruct dominant vertical wall segments from labeled connected components
clean_v = fit_vertical_lines(labels_v)

# Reconstruct dominant horizontal wall segments from labeled connected components
clean_h = fit_horizontal_lines(labels_h)

# Combine vertical and horizontal reconstructions to form the final floor plan structure
clean_plan = cv2.bitwise_or(clean_v, clean_h)

#Visualization of output

plt.figure(figsize=(6,6))
plt.imshow(clean_plan, cmap='gray')
plt.title("Straightened Floor Plan")
plt.axis('off')
plt.show()
