import serial
import time
import pygame

# Configure the serial connection
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=1)  # Replace 'COM3' with your Arduino port
time.sleep(2)  # Wait for the connection to initialize
pygame.mixer.init()
pygame.mixer.music.load("Swiper no swiping.mp3")
pygame.mixer.music.play()

swiped = False

try:
    while True:
        # Read data from Arduino
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            print(line)
            if line == "1":
                swiped = True

        if swiped and pygame.mixer.music.get_busy():
            swiped = False

        if swiped == True:
            print('Swiper no Swiping!')
            pygame.mixer.music.play()
            swiped = False

        # time.sleep(1  # Wait for 1 second
except KeyboardInterrupt:
    print("Communication stopped.")
finally:
    arduino.close()
