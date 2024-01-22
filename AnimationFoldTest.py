import os
import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Image Animation")

# Get the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# Specify the name of your subfolder containing images
subfolder_name = "subfolder_name"

# Construct the full path to the subfolder
image_folder = os.path.join(current_directory, subfolder_name)

# Get a list of image paths in the specified folder
image_paths = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Load images
images = [pygame.image.load(path) for path in image_paths]

# Set initial image position
image_rect = images[0].get_rect()
image_rect.center = (width // 2, height // 2)

# Set animation variables
fps = 12  # Adjust the frames per second as needed
clock = pygame.time.Clock()
current_frame = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
