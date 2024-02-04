
# import the needed libraries 
import os
import pygame
import sys
from PreloadOptions import InputHolder

# initializing pyhgame
pygame.init()

# setting up the display window 
width, height = 720, 400                   
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animation")

# get the current working directory
current_directory = os.getcwd()

# prints the current directory to the terminal 
# helps for troubleshooting incase of directory errors 
print("Current working directory:", current_directory)

# specifying the name of the subfolder with the images
image_folder_name = "ImageFolder"

#subfolder_name = InputHolder.UserInput
subfolder_name = InputHolder.UserInput                # want this to be variable 

# constructs the full path to the subfolder
image_folder = os.path.join(current_directory, image_folder_name)

subfolder = os.path.join(image_folder, subfolder_name)


# get a list of image paths in the specified folder
# uses beautiful amazing LIST COMPREHENSION :)
image_paths = [os.path.join(subfolder, file) for file in os.listdir(subfolder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# load images
images = [pygame.image.load(path) for path in image_paths]

# set initial image position
max_image_width = width 
max_image_height = height 
for index in range(len(images)):
    images[index] = pygame.transform.scale(images[index], (max_image_width, max_image_height))
    
image_rect = images[0].get_rect()
image_rect.center = (width // 2, height // 2)

# set animation variables
fps = 12                        #CUSTOMIZABLE SETTING   
clock = pygame.time.Clock() 
current_frame = 0

class Settings:
    """
    class just to hold and handle the users inputs
    """
    
    def __init__(self):
        self.fps = 12
        
    def update(self): 
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_f] and self.fps == 12:
            self.fps = 24
        
        elif keys[pygame.K_f] and self.fps == 24:
            self.fps = 12
            
        # PART THAT RETURNS USER TO BASE GUI UPON KEYPRESS  
        if keys[pygame.K_q]:
            pygame.quit()
            os.execvp("python", ["python", "UserGuiTemp.py"])
            
        if keys[pygame.K_p]:
            self.fps = 1
            if self.fps == 1 and keys[pygame.K_SPACE]:
                self.fps = 12
        
    
        
################################################################# 
# MAIN ANIMATION LOOP:
#################################################################

settings = Settings()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    settings.update()   # PART THAT UPDATES USER KEY PRESSES 
    fps = settings.fps
    #print(fps)     # for troubleshooting 

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
