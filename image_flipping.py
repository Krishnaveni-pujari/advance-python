import cv2

# Read the image
image = cv2.imread("sample.png")

# Flip the image
# 1 = Horizontal flip
flipped_image = cv2.flip(image, 1)

# Display the original and flipped image
cv2.imshow("Original Image", image)
cv2.imshow("Flipped Image", flipped_image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()