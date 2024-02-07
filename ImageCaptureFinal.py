# Name: Chandler Dees
# Date: 2 - 8 - 24
# Desc: This file is the file used for dynamic image capturing 
#       this allows the user to submit their own images at any 
#       time utilizing the pi camera

#import all of the needed libraries

import pygame
import sys
import os
import picamera


pygame.init()

# sets up the resolution for the animation display
display_width, display_height = 800, 800
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Image Capture Animation")

# sets resolution for capturing images SEPARATELY 
capture_width, capture_height = 800, 400

# specifies the  folder to draw the images from
img_folder = "ImageFolder"  # updated to ImageFolder

# class dedicated to holding the settings that the user can change 
# once the animation has been compiled. This updates, looking for 
# inputs constatntly at the same time that the frames update. 

class Settings:
    """
    class just to hold and handle user inputs 
    """
    def __init__(self):
        self.fps = 12

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_f] and self.fps == 12:
            self.fps = 24

        elif keys[pygame.K_f] and self.fps == 24:
            self.fps = 12

        # part that returns user to Main upon quit
        if keys[pygame.K_q]:
            pygame.quit()
            os.execvp("python3", ["python3", "Main.py"])    # leave as python3 since this only works on raspbery pi 

# function that loads the images from a folder

def load_images(folder):
    images = [os.path.join(folder, file) for file in os.listdir(folder) if file.lower().endswith(('.png', 'jpg', '.jpeg'))]
    return [pygame.image.load(image) for image in images]

# initializing an instance of the settings class so we can update it later
settings = Settings()


# function to run the animation
# this is stored in a function to allow it to run separately after image capture
# whereas the preloaded animatons would simply run this on its own automatically

def run_animation(image_list, settings):
    fps = 12    # by default it initializes the frames per second to 12 (eastern standard)
    clock = pygame.time.Clock()
    current_frame = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # looks to see if the user ever wants to quit 
                pygame.quit()
                sys.exit()
        
        settings.update() # checks for user setting input 
        fps = settings.fps
        
        # updates the animation frame
        current_frame = (current_frame + 1) % len(image_list)

        # draws the current frame
        screen.fill((255, 255, 255))  # White background
        screen.blit(image_list[current_frame], (0, 0))

        # update the display
        pygame.display.flip()

        # limits the frame rate to the user desired amount of either 12 or 24
        clock.tick(fps)

# a separate function used exclusively to capture images

def capture_image(camera):
    camera.capture('image.jpg')
    captured_images.append(pygame.image.load('image.jpg'))

# setting up Raspberry Pi camera
camera = picamera.PiCamera()
# sets the resolution for capturing images
camera.resolution = (capture_width, capture_height)  

# starts the preview
# the preview is the window that allows users to see what the camera sees during the 
# image capture portion of the program. THIS IS VITAL DONT BREAK IT
camera.start_preview()

##################
# Main loop
##################

# initialize an empty list for the captured images to be appended to 
captured_images = []
# allows users to see themselves 
preview_active = True

while preview_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # looks for quit 
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # captures image
                capture_image(camera)
                print("Image captured.")
            elif event.key == pygame.K_RETURN:
                # stops the preview
                camera.stop_preview()
                preview_active = False
                break

# runs the animation
if captured_images:
    print("Running animation...")
    run_animation(captured_images, settings)

# clean up camera
camera.close()

