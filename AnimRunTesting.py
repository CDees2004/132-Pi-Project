
# import the needed libraries 
import os
import pygame
import sys

# initializing pyhgame
pygame.init()

# setting up the display window 
width, height = 1000, 800                    # POTENTIALLY CUSTOMIZABLE SETTING 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animation")

# get the current working directory
current_directory = os.getcwd()

# prints the current directory to the terminal 
# helps for troubleshooting incase of directory errors 
print("Current working directory:", current_directory)

# specifying the name of the subfolder with the images
image_folder_name = "ImageFolder"

subfolder_name = "Gojo"



# constructs the full path to the subfolder
image_folder = os.path.join(current_directory, image_folder_name)

subfolder = os.path.join(image_folder, subfolder_name)


# get a list of image paths in the specified folder
# uses beautiful amazing LIST COMPREHENSION :)
image_paths = [os.path.join(subfolder, file) for file in os.listdir(subfolder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# load images
images = [pygame.image.load(path) for path in image_paths]

# set initial image position
image_rect = images[0].get_rect()
image_rect.center = (width // 2, height // 2)

# set animation variables
fps = 12                        #CUSTOMIZABLE SETTING   
clock = pygame.time.Clock() 
current_frame = 0

################################################################# 
# MAIN ANIMATION LOOP:
#################################################################

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the current frame
    screen.fill((255, 255, 255))  # White background
    screen.blit(images[current_frame], image_rect)

    # update animation frame
    current_frame = (current_frame + 1) % len(images)

    # update display
    pygame.display.flip()

    # cap the frame rate
    clock.tick(fps)

# clean up and exit
pygame.quit()
sys.exit()
