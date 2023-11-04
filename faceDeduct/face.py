import cv2

trained_dataset = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Read an image 
img = cv2.imread("images/Pic.jpg")

# Convert the frame to grayscale
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a named window and display the grayscale image
cv2.namedWindow("Face Detection")
cv2.imshow("Face Detection", grey)
cv2.waitKey(0)
cv2.destroyWindow("Face Detection")

# Find the faces
faces = trained_dataset.detectMultiScale(grey)

# Draw the faces on the original image (img)
for x, y, width, height in faces:
    cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 2)

# Display the image with rectangles drawn on it
cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
