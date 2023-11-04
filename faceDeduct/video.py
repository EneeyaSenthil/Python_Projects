import cv2

# Load the pre-trained cascade classifier for face detection
trained_dataset = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Open the video file
video = cv2.VideoCapture("videos/video.mp4")

while True:
    # Read a frame from the video
    success, frame = video.read()
    if not success:
        break

    # Convert the frame to grayscale
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = trained_dataset.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    # Display the frame with detected faces
    cv2.imshow("Video", frame)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
video.release()
cv2.destroyAllWindows()
