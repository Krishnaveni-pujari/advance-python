import cv2

# 1. Initialize the system camera (0 is usually the default built-in webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open the system camera.")
    exit()

print("🎥 Camera started successfully!")
print("⌨️ Press 'q' on your keyboard while looking at the video window to exit.")

while True:
    # 2. Capture frame-by-frame from the live camera stream
    ret, frame = cap.read()

    if not ret:
        print("❌ Error: Failed to grab a frame from the camera.")
        break

    # 3. Convert the live frame to Grayscale (shades of gray)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 4. Apply Binary Thresholding to make it purely Black and White
    # Adjust 127 higher for a darker look, lower for a brighter look
    _, bw_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)

    # 5. Display the live black-and-white video stream in a window
    cv2.imshow("Live Black & White Camera Feed", bw_frame)

    # 6. Stop the loop if the user presses the 'q' key
    # cv2.waitKey(1) checks for keyboard input every 1 millisecond
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("👋 Closing camera feed...")
        break

# 7. Clean up and release the system resources
cap.release()
cv2.destroyAllWindows()
