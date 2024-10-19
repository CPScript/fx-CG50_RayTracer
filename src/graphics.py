import machine
import time

def init_screen(): # Initialize the display (assuming it uses a specific display library)
    pass

def draw_pixel(x, y, color): # Draw a pixel on the screen at position (x, y) with the specified color
    if 0 <= x < 320 and 0 <= y < 240:  # Check if coordinates are within bounds
        # Assuming a simple method to set the pixel color
        # The actual implementation depends on the calculator's graphics API which isn't publicly avalible atm.
        
        # Example: Use the display object to set pixel color
        display.pixel(x, y, color)
        
        # for testing purposes
        print(f'Drawing pixel at ({x}, {y}) with color {color}')

# Optional: A function to clear the screen
def clear_screen():
    for y in range(240):
        for x in range(320):
            draw_pixel(x, y, 0)  # Draw black pixels to clear the screen
