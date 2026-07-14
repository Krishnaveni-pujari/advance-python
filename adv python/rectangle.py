import cv2
import numpy as np

# Create a white image
img = np.ones((500, 700, 3), dtype=np.uint8) * 255

drawing = False
start_x, start_y = -1, -1

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global drawing, start_x, start_y, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp = img.copy()
            cv2.rectangle(temp, (start_x, start_y), (x, y), (255, 0, 0), 2)
            cv2.imshow("Draw Rectangle", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (start_x, start_y), (x, y), (255, 0, 0), 2)
        cv2.imshow("Draw Rectangle", img)

cv2.namedWindow("Draw Rectangle")
cv2.setMouseCallback("Draw Rectangle", draw_rectangle)

print("Press 'c' to clear")
print("Press 'q' to quit")

while True:
    cv2.imshow("Draw Rectangle", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        img = np.ones((500, 700, 3), dtype=np.uint8) * 255

    elif key == ord('q'):
        break

cv2.destroyAllWindows()