# Name: Chandler Dees
# Desc: 
#Alternate version of the animation software which 
#employs the pi camera for image capturing, basic form
#to test the camera

import pygame
from picamera import PiCamera
from time import sleep

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Image Animation")

# Initialize PiCamera
camera = PiCamera()

# Set initial image position
image_rect = pygame.Rect(0, 0, width, height)

# Set animation variables
fps = 30
clock = pygame.time.Clock()
current_frame = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capture image from the camera
    camera.capture('captured_image.jpg')

    # Load the captured image
    captured_image = pygame.image.load('captured_image.jpg')

    # Draw the current frame
    screen.blit(captured_image, image_rect)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

# Clean up and exit
pygame.quit()
