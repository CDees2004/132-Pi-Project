import pygame
import sys
import os
import picamera
from time import sleep

pygame.init()

# Set resolution for the animation display
display_width, display_height = 800, 800
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Animation")

# Set resolution for capturing images
capture_width, capture_height = 800, 400

# Specifying a folder to draw the images from
img_folder = "ImageFolder"  # Update with your image folder path

# Function to load images from a folder
def load_images(folder):
    images = [os.path.join(folder, file) for file in os.listdir(folder) if file.lower().endswith(('.png', 'jpg', '.jpeg'))]
    return [pygame.image.load(image) for image in images]

# Function to run the animation
def run_animation(image_list):
    fps = 12
    clock = pygame.time.Clock()
    current_frame = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Update animation frame
        current_frame = (current_frame + 1) % len(image_list)

        # Draw the current frame
        screen.fill((255, 255, 255))  # White background
        screen.blit(image_list[current_frame], (0, 0))

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(fps)

# Function to capture image
def capture_image(camera):
    camera.capture('image.jpg')
    captured_images.append(pygame.image.load('image.jpg'))

# Set up Raspberry Pi camera
camera = picamera.PiCamera()
camera.resolution = (capture_width, capture_height)  # Set resolution for capturing images

# Start the preview
camera.start_preview()

# Main loop
captured_images = []
preview_active = True

while preview_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Capture image
                capture_image(camera)
                print("Image captured.")
            elif event.key == pygame.K_RETURN:
                # Stop the preview
                camera.stop_preview()
                preview_active = False
                break

# Run animation
if captured_images:
    print("Running animation...")
    run_animation(captured_images)

# Clean up camera
camera.close()

