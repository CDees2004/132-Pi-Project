
#Name: Chandler Dees  
#Date: 2 - 8 - 23
#Desc: file that takes in arguements and iterates the animation software
#      through the appropriate subfolder which is specified by an argument 
#      provided by the tkinter window.

import os
import pygame
import sys
from PreloadOptions import InputHolder

pygame.init()

# setting up the display window 
width, height = 800, 550                   
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animation")

# getting the current working directory
current_directory = os.getcwd()

# prints cwd to terminal for troubleshooting 
#print("Current working directory:", current_directory)

# specifying the name of the folder with the other subfolders
image_folder_name = "ImageFolder"

# Subfolder_name = InputHolder.UserInput
subfolder_name = InputHolder.UserInput  # THIS ALLOWS THE USER TO PICK A PRELOADED ANIMATION

# constructs the full path to the subfolder (specified by user)
image_folder = os.path.join(current_directory, image_folder_name)
subfolder = os.path.join(image_folder, subfolder_name)

# gets a list of image paths in the specified folder
# makes use of my favorite thing, list comprehension and sorts the paths
# SORTING IS NEEDED TO PLAY IMAGES IN ORDER, VITAL DO NOT MESS WITH IT 
image_paths = sorted([os.path.join(subfolder, file) for file in os.listdir(subfolder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))])

# load and scale the images to fit the window size 
max_image_width, max_image_height = width, height
images = [pygame.transform.scale(pygame.image.load(path), (max_image_width, max_image_height)) for path in image_paths]

# sets the initial image position
image_rect = images[0].get_rect()
image_rect.center = (width // 2, height // 2)

clock = pygame.time.Clock() 
current_frame = 0

# a class specifically to encompass the settings that
# the user can modify with keyboard input 

class Settings:
    """
    Class just to hold and handle the user's inputs
    """
    
    def __init__(self):
        self.fps = 12
        
    def update(self): 
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_f] and self.fps == 12:
            self.fps = 24
        
        elif keys[pygame.K_f] and self.fps == 24:
            self.fps = 12
            
        # Part that returns the user to the base GUI upon keypress  
        if keys[pygame.K_q]:
            pygame.quit()
            os.execvp("python3", ["python3", "Main.py"])      # THIS IS DEPENDENT ON HARDWARE. FOR PI IT IS PYTHON3 FOR WINDOWS IT IS PYTHON!!!

# Main loop
settings = Settings()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    settings.update()  # updates looking for users input  
    fps = settings.fps

    # draw the current frame
    screen.fill((255, 255, 255))  
    screen.blit(images[current_frame], image_rect)

    # updates animation frame
    current_frame = (current_frame + 1) % len(images)

    # update display
    pygame.display.flip()

    # cap the frame rate
    clock.tick(fps)

# clean up and exit
pygame.quit()
sys.exit()
