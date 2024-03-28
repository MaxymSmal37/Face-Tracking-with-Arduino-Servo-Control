**Face Tracking with Arduino Servo Control**

This Python script utilizes OpenCV to detect faces in real-time through a webcam feed and controls the movement of a servo motor connected to an Arduino board based on the position of the detected faces. The Arduino code receives commands from Python through serial communication and adjusts the servo motor accordingly.

### Prerequisites

- Python 3.x
- OpenCV (`cv2` library)
- Arduino IDE
- Arduino board with a servo motor

### Setup Instructions

1. **Hardware Setup:**
   - Connect your servo motor to the Arduino board. Typically, the servo's signal wire should be connected to a PWM pin (e.g., pin 5), the power wire to 5V, and the ground wire to GND.

2. **Upload Arduino Sketch:**
   - Copy the provided Arduino sketch (`servo_control.ino`) into your Arduino IDE.
   - Upload the sketch to your Arduino board.

3. **Python Environment Setup:**
   - Install the required Python libraries using pip:
     ```
     pip install opencv-python pyserial
     ```

### Usage

1. **Connect Arduino:**
   - Connect your Arduino board to your computer via USB.

2. **Run Python Script:**
   - Execute the Python script (`face_tracking.py`).
   - Ensure that the webcam is properly connected and recognized by your system.

3. **Face Tracking:**
   - The script will open a window displaying the webcam feed with rectangles drawn around detected faces.
   - As faces move within the frame, the script sends commands to the Arduino to adjust the servo motor accordingly to keep the face in the center.

4. **Termination:**
   - To stop the script, press the 'q' key on the keyboard.

### Note

- Adjust the `COM` port in the Python script (`COM4` in this example) to match the port to which your Arduino is connected.
- Make sure the `haarcascade_frontalface_default.xml` file is available in the OpenCV data directory. This file is used for face detection.
- You may need to adjust the servo motor's range and direction based on your hardware setup. Modify the `servo_control.ino` code as needed.

### Credits

- The face detection algorithm uses Haar cascades provided by OpenCV.
- This project is inspired by various tutorials and examples available online, adapting them to suit specific requirements.

### Disclaimer

- This project is provided as-is, without any warranty. Use it at your own risk.
- Be cautious when working with hardware components, especially if you're not familiar with electronics or programming.
