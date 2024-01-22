
#importing all the needed libraries 
import pygame
import sys
import os
import ImageFolder 

pygame.init()

# Setting up the pygame display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animation")

# Specifying a folder to draw the images from 
img_folder = ImageFolder

images = [os.path.join(img_folder, file) for file in os.listdir(img_folder) if file.lower().endswith(('.png', 'jpg', '.jpeg'))]

# using good old LIST COMPREHENSION in order to create a list of  

images = [pygame.image.load(value) for value in images]

# Set initial image position
image_rect = images[0].get_rect()
image_rect.center = (width // 2, height // 2)

# Set animation variables
fps = 12
clock = pygame.time.Clock()
current_frame = 0

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update animation frame
    current_frame = (current_frame + 1) % len(images)
    # want to potentially add a rebound feature where you can toggle
    # if you want the animation to play backwards once the final frame 
    # of the initial display has been reached

    # Draw the current frame
    screen.fill((255, 255, 255))  # White background
    screen.blit(images[current_frame], image_rect)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)
