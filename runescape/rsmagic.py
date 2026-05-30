import pyautogui
import cv2
import numpy as np
import random
import time

# List of coordinates to move the mouse to
coordinates = [
    (1134, 273),
    (1061, 363),
    (1061, 311),
    (892, 261),
    (930, 167),
    (847, 355),
    (855, 389),
]

# Path to the "Attack Hobgoblin" option image
attack_option_image = 'attack_hobgoblin.png'

# Function to find the "Attack Hobgoblin" option on the screen
def find_attack_option():
    try:
        # Take a screenshot of the current screen
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

        # Load the "Attack Hobgoblin" template
        template = cv2.imread(attack_option_image, cv2.IMREAD_GRAYSCALE)

        # Perform template matching to find the attack option
        result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8  # Adjust this to increase or decrease match accuracy
        loc = np.where(result >= threshold)

        # If we found the attack option, return the position
        if len(loc[0]) > 0:
            top_left = (loc[1][0], loc[0][0])  # loc[1][0] is the x, loc[0][0] is the y
            w, h = template.shape[::-1]  # Template dimensions (width, height)
            center_x = top_left[0] + w // 2  # Center x-coordinate
            center_y = top_left[1] + h // 2  # Center y-coordinate
            return (center_x, center_y)  # Return center position
        
        return None

    except Exception as e:
        print(f"Error finding 'Attack Hobgoblin' option: {e}")
        return None

# Function to move the mouse to a coordinate, check for the "Attack Hobgoblin" option, and click
def move_and_check_attack(coords):
    try:
        # Apply a small random offset to simulate human-like movement
        rand_x = coords[0] + random.randint(-10, 10)
        rand_y = coords[1] + random.randint(-10, 10)

        # Move the mouse to the randomized position
        pyautogui.moveTo(rand_x, rand_y, duration=random.uniform(0.2, 0.5))
        print(f"Moved to {rand_x}, {rand_y}")

        # Look for the "Attack Hobgoblin" option after moving the mouse
        attack_position = find_attack_option()

        if attack_position:
            # Adding small random offset to simulate human-like clicking
            offset_x = random.randint(-5, 5)
            offset_y = random.randint(-5, 5)
            attack_position_with_offset = (attack_position[0] + offset_x, attack_position[1] + offset_y)

            print(f"'Attack Hobgoblin' option found at {attack_position}. Clicking with offset.")
            pyautogui.click(attack_position_with_offset)  # Click on the "Attack Hobgoblin" option
        else:
            print("Attack option not found.")

    except Exception as e:
        print(f"Error in move_and_check_attack: {e}")

# Main bot loop to go through all coordinates and move the mouse, then check for "Attack Hobgoblin"
def magic_bot():
    try:
        for coords in coordinates:
            move_and_check_attack(coords)  # Move to the coordinates and check for attack option
            time.sleep(random.uniform(1, 3))  # Random delay between actions

    except Exception as e:
        print(f"Unexpected error: {e}")
        time.sleep(5)  # Wait before retrying
        magic_bot()  # Restart the bot loop if an error occurs

# Run the bot
magic_bot()


# print("Move the mouse to the position you want to capture...")

# # Loop to keep checking the mouse position every 1 second
# while True:
#     x, y = pyautogui.position()  # Get the current position of the mouse
#     print(f"Mouse Position: ({x}, {y})")
#     time.sleep(1)  # Pause for 1 second before checking again







# import pyautogui
# import cv2
# import numpy as np
# import time
# import random
# import sys

# # List of hobgoblin images to search for
# hobgoblin_images = ['hobgoblin1.png', 'hobgoblin2.png', 'hobgoblin3.png', 'hobgoblin4.png']

# # Path to the "Attack Hobgoblin" option image
# attack_option_image = 'attack_hobgoblin.png'

# # Function to find a hobgoblin image on the screen
# def find_hobgoblin():
#     try:
#         # Take a screenshot of the current screen
#         screen = pyautogui.screenshot()
#         screen_np = np.array(screen)
#         screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

#         for image in hobgoblin_images:
#             # Load the template (the hobgoblin image)
#             template = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

#             # Perform template matching to find the hobgoblin image on the screen
#             result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
#             threshold = 0.82  # Adjust this to increase or decrease match accuracy
#             loc = np.where(result >= threshold)

#             # If we found a match, return the location
#             if len(loc[0]) > 0:
#                 # Return the position of the first match found
#                 return loc[::-1][0][0], loc[::-1][1][0]  # Return (x, y)
        
#         return None

#     except Exception as e:
#         print(f"Error finding hobgoblin: {e}")
#         return None

# # Function to find the "Attack Hobgoblin" option in the right-click menu
# def find_attack_option():
#     try:
#         # Take a screenshot of the current screen
#         screen = pyautogui.screenshot()
#         screen_np = np.array(screen)
#         screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

#         # Load the "Attack Hobgoblin" template
#         template = cv2.imread(attack_option_image, cv2.IMREAD_GRAYSCALE)

#         # Perform template matching to find the attack option
#         result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
#         threshold = 0.8  # Adjust this to increase or decrease match accuracy
#         loc = np.where(result >= threshold)

#         # If we found the attack option, return the position
#         if len(loc[0]) > 0:
#             return loc[::-1][0][0], loc[::-1][1][0]  # Return (x, y)
        
#         return None

#     except Exception as e:
#         print(f"Error finding 'Attack Hobgoblin' option: {e}")
#         return None

# # Function to right-click at a position and then click on the "Attack Hobgoblin" option
# def right_click_and_attack(hobgoblin_position):
#     try:
#         # Right-click on the hobgoblin position
#         pyautogui.rightClick(hobgoblin_position)
#         print(f"Right-clicked on hobgoblin at {hobgoblin_position}")

#         # Wait for the context menu to appear
#         time.sleep(1)

#         # Try to find the "Attack Hobgoblin" option
#         attack_position = find_attack_option()

#         if attack_position:
#             print(f"Found 'Attack Hobgoblin' option at {attack_position}. Clicking on it.")
#             pyautogui.click(attack_position)  # Click on the "Attack Hobgoblin" option
#         else:
#             print("Attack option not found.")
        
#     except Exception as e:
#         print(f"Error in right-click and attack: {e}")

# # Function to simulate a delay to mimic human behavior
# def random_delay(min_delay=0.5, max_delay=2):
#     try:
#         delay = random.uniform(min_delay, max_delay)
#         print(f"Waiting for {delay:.2f} seconds...")
#         time.sleep(delay)
#     except Exception as e:
#         print(f"Error in delay: {e}")

# # Main bot loop
# def magic_bot():
#     try:
#         while True:
#             # Try to find a hobgoblin image
#             hobgoblin_position = find_hobgoblin()

#             if hobgoblin_position:
#                 print(f"Hobgoblin found at {hobgoblin_position}!")  # Print the mouse coordinates
#                 right_click_and_attack(hobgoblin_position)  # Right-click and select "Attack Hobgoblin"
#                 random_delay(1, 3)  # Wait for a random amount of time before the next action
#             else:
#                 print("Hobgoblin not found, retrying...")

#             # To avoid running the bot too quickly, add a delay before the next search
#             random_delay(1, 2)  # Wait before checking again

#     except KeyboardInterrupt:
#         print("Bot stopped by user.")
#         sys.exit(0)  # Exit the program gracefully

#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         print("Bot restarting...")
#         time.sleep(5)  # Wait for 5 seconds before restarting the bot
#         magic_bot()  # Restart the bot loop

# # Run the bot
# magic_bot()


