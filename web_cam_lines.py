import cv2

cap = cv2.VideoCapture(0)

drawing = False
start_point = None

def draw_line(event, x, y, flags, param):
    global drawing, start_point

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            frame_copy = frame.copy()
            cv2.line(frame_copy, start_point, (x, y), (0, 255, 0), 3)
            cv2.imshow("Draw Lines", frame_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(frame, start_point, (x, y), (0, 255, 0), 3)


cv2.namedWindow("Draw Lines")
cv2.setMouseCallback("Draw Lines", draw_line)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not found")
        break

    frame = cv2.flip(frame, 1)

    cv2.putText(
        frame,
        "Drag mouse to draw | C = Clear | Q = Quit",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.imshow("Draw Lines", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        frame[:] = 0

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()