# File used for image capture feature of animation, using the pi camera

# import all the needed libraries 
import pygame
import sys
import os
import picamera
from time import sleep

pygame.init()

# resolution for the animation display
display_width, display_height = 800, 800
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Animaster Image Capture")

#  resolution for capturing images
#  SET SEPARATE FROM RESOLUTION FOR ANIMATION DISPLAY 
#  SEPARATE!!!
capture_width, capture_height = 800, 400

# specifying a folder to draw the images from
img_folder = "ImageFolder"  # Update with your image folder path

# function to load images from a folder
def load_images(folder): # slightly different from version seen in the preloaded anim ver 
    images = [os.path.join(folder, file) for file in os.listdir(folder) if file.lower().endswith(('.png', 'jpg', '.jpeg'))]
    return [pygame.image.load(image) for image in images]

# a separate function to run the animation
def run_animation(image_list):
    fps = 12
    clock = pygame.time.Clock()
    current_frame = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # updates the current frame
        current_frame = (current_frame + 1) % len(image_list)

        # draws the current frame
        screen.fill((255, 255, 255))  # white background
        screen.blit(image_list[current_frame], (0, 0))

        # updates display
        pygame.display.flip()

        # selects the frame rate
        clock.tick(fps)

# separate function to capture image
def capture_image(camera):
    camera.capture('image.jpg')
    captured_images.append(pygame.image.load('image.jpg'))

# setting up  the rasp pi camera
camera = picamera.PiCamera()
camera.resolution = (capture_width, capture_height)  # sets resolution for capturing images

# Start the preview
# preview is so the user can see what the camera sees while capturing their images 
# VERY VERY FRAGILE, do NOT edit this.
camera.start_preview()

######################################################################
# MAIN LOOP 
######################################################################

captured_images = []
preview_active = True

while preview_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # capture image
                capture_image(camera)
                print("Image captured.")
            elif event.key == pygame.K_RETURN:
                # ends the preview
                camera.stop_preview()
                preview_active = False
                break

# runs the captured animation
if captured_images:
    print("Running animation...")
    run_animation(captured_images)

# clean up camera
# WILL NEED TO ADD GPIO CLEANUP DOWN HERE ALSO 
camera.close()

