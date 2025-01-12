/*
  Arduino LSM6DS3 - Accelerometer Application

  This example reads the acceleration values as relative direction and degrees,
  from the LSM6DS3 sensor and prints them to the Serial Monitor or Serial Plotter.

  The circuit:
  - Arduino Nano 33 IoT

  Created by Riccardo Rizzo

  Modified by Jose García
  27 Nov 2020

  This example code is in the public domain.
*/

#include <Arduino_LSM6DS3.h>

float x, y, z;
float netAcc;
int degreesX = 0;
int degreesY = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial)
    ;
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1)
      ;
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println("Hz");
}

void loop() {


  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);

    netAcc = sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2));
    Serial.println(netAcc);
    if (netAcc > 3) {
      Serial.println("Swiper no Swiping!");
    }
    // IMU.readAcceleration(x, y, z);
  }

  delay(100);
}