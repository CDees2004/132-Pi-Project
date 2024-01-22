# this is the absolute base version of the animation file, 
# a fallback version to use for troubleshooting when errors 
# arrise in more complex version of the program 


import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Image Animation")

# Load images
image_paths = ["image1.png", "image2.png", "image3.png"]
images = [pygame.image.load(path) for path in image_paths]

# Set initial image position
image_rect = images[0].get_rect()
image_rect.center = (width // 2, height // 2)

# Set animation variables
fps = 30
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

    # Draw the current frame
    screen.fill((255, 255, 255))  # White background
    screen.blit(images[current_frame], image_rect)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)
