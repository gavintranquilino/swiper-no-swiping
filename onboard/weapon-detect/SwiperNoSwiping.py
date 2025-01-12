import serial
import time
import pygame
import mouse

# Configure the serial connection
arduino = serial.Serial(port='COM38', baudrate=9600, timeout=1)  # Replace 'COM5' with your Arduino port
time.sleep(2)  # Wait for the connection to initialize
pygame.mixer.init()
pygame.mixer.music.load("Swiper no swiping.mp3")

swiped = False
sensitivity = 1.7
isOn = False

try:
    print("Program started. Left-click to activate, right-click to deactivate.")
    while True:
        # Waiting for left click to activate
        while not isOn:
            if mouse.is_pressed('left'):
                print("Left mouse button clicked! Activating...")
                isOn = True
                time.sleep(0.5)  # Debounce delay to prevent accidental double-clicks

        # Active mode: Processing Arduino data
        while isOn:
            if arduino.in_waiting > 0:
                try:
                    # Read and process data from Arduino
                    line = arduino.readline().decode('utf-8').strip()
                    line_value = float(line)
                    print(f"Arduino Value: {line_value}")
                    if line_value > sensitivity:
                        swiped = True
                except ValueError:
                    print(f"Invalid data received from Arduino: {line}")

            # Play sound if a swipe is detected
            if swiped and not pygame.mixer.music.get_busy():
                print('Swiper no Swiping!')
                pygame.mixer.music.play()
                swiped = False

            # Check for right click to deactivate
            if mouse.is_pressed('right'):
                print("Right mouse button clicked! Deactivating...")
                isOn = False
                time.sleep(0.5)  # Debounce delay

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    print("Cleaning up resources...")
    arduino.close()
