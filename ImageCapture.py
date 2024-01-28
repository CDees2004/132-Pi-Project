
# Name: Chandler Dees
# Date: 1 - 27 - 24
# Desc: 
#     - version of the animation software that uses the raspberry pi camera 
#     - for image capture and appends those images to a list, it then runs 
#     - the base animation software using said list of captured images 

import pygame
import sys
import os
import picamera
from time import sleep

pygame.init()

# setting up the pygame display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animation")

# specifiying the folder to draw the images from
img_folder = "ImageFolder" 

# function to load images from a folder
def load_images(folder):
    images = [os.path.join(folder, file) for file in os.listdir(folder) if file.lower().endswith(('.png', 'jpg', '.jpeg'))]
    return [pygame.image.load(image) for image in images]

# function to run the animation
def run_animation(image_list):
    fps = 12
    clock = pygame.time.Clock()
    current_frame = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # updates the animation frame
        current_frame = (current_frame + 1) % len(image_list)

        # draws the current frame
        screen.fill((255, 255, 255))  # White background
        screen.blit(image_list[current_frame], (0, 0))

        # updates display
        pygame.display.flip()

        # sets the frame rate 
        clock.tick(fps)

# function to capture image
def capture_image():
    camera.capture('image.jpg')
    #***APPENDS CAPTURED IMAGE TO LIST
    captured_images.append(pygame.image.load('image.jpg'))

# sets up Raspberry Pi camera
camera = picamera.PiCamera()

# MAIN loop
captured_images = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Capture image
                capture_image()
                print("Image captured.")
            elif event.key == pygame.K_RETURN:
                # Run animation
                if captured_images:
                    print("Running animation...")
                    run_animation(captured_images)

# clean up camera
camera.close()
# once GPIO is implemented we also need gpio.cleanup
