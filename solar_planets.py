import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Function to add text to the image
def add_text(image, text, position, font_size=0.5, color=(255, 255, 255), thickness=1):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, position, font, font_size, color, thickness, cv2.LINE_AA)

# Add text for each planet
add_text(img, "Mercury", (50, 50))
add_text(img, "Venus", (150, 100))
add_text(img, "Earth", (250, 150))
add_text(img, "Mars", (350, 200))
add_text(img, "Jupiter", (450, 250))
add_text(img, "Saturn", (550, 300))
add_text(img, "Uranus", (650, 350))
add_text(img, "Neptune", (750, 400))

# Display the image
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_system_with_name.jpg", img)
