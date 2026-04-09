/*Goal: Use a laser proximity sensor (e.g., VL53L0X) to create a "geofence." If an object is detected within a certain range, the AGV (Automated Guided Vehicle) slows down, and the incident is logged to an SD card.
Circuit Guide
Sensor: VL53L0X (I2C: SDA to A4, SCL to A5 on Arduino).
Storage: SD Card Module (SPI: MOSI 11, MISO 12, SCK 13, CS 10).
Output: PWM signal to Motor Driver to reduce speed.
*/
#include <Wire.h>
#include <VL53L0X.h>
#include <SD.h>

VL53L0X sensor;
const int motorPin = 5; // PWM pin for speed control

void setup() {
  Wire.begin();
  sensor.init();
  sensor.setTimeout(500);
  sensor.startContinuous();
  SD.begin(10);
}

void loop() {
  uint16_t distance = sensor.readRangeContinuousMillimeters();
  int speed = 255; // Default Full Speed

  if (distance < 500) { // Geofence: 500mm
    speed = 100; // Slow down
    File logFile = SD.open("logs.txt", FILE_WRITE);
    if (logFile) {
      logFile.println("Collision Alert: Distance " + String(distance));
      logFile.close();
    }
  }
  analogWrite(motorPin, speed);
}
