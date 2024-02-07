
#Name: chandler Dees  
#Date: 2 - 8 - 23
#Desc: file that takes in arguements and iterates the animation software
#      through the appropriate subfolder which is specified by an argument 
#      provided by the tkinter window.

import os
import pygame
import sys
from PreloadOptions import InputHolder

# Initializing pygame
pygame.init()

# Setting up the display window 
width, height = 720, 400                   
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animation")

# Get the current working directory
current_directory = os.getcwd()

# Prints the current directory to the terminal 
# Helps for troubleshooting in case of directory errors 
print("Current working directory:", current_directory)

# Specifying the name of the subfolder with the images
image_folder_name = "ImageFolder"

# Subfolder_name = InputHolder.UserInput
subfolder_name = InputHolder.UserInput  # THIS ALLOWS THE USER TO PICK A PRELOADED ANIMATION

# Constructs the full path to the subfolder
image_folder = os.path.join(current_directory, image_folder_name)
subfolder = os.path.join(image_folder, subfolder_name)

# Get a list of image paths in the specified folder
# Uses list comprehension and sorts the paths
image_paths = sorted([os.path.join(subfolder, file) for file in os.listdir(subfolder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))])

# Load and scale images
max_image_width, max_image_height = width, height
images = [pygame.transform.scale(pygame.image.load(path), (max_image_width, max_image_height)) for path in image_paths]

# Set initial image position
image_rect = images[0].get_rect()
image_rect.center = (width // 2, height // 2)

clock = pygame.time.Clock() 
current_frame = 0

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
            os.execvp("python", ["python", "Main.py"])      # THIS IS DEPENDENT ON HARDWARE. FOR PI IT IS PYTHON3 FOR WINDOWS IT IS PYTHON!!!

# Main animation loop:
settings = Settings()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    settings.update()  # Part that updates user key presses 
    fps = settings.fps

    # Draw the current frame
    screen.fill((255, 255, 255))  # White background
    screen.blit(images[current_frame], image_rect)

    # Update animation frame
    current_frame = (current_frame + 1) % len(images)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

# Clean up and exit
pygame.quit()
sys.exit()
