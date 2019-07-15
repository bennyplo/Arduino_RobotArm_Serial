# Arduino_RobotArm_Serial
Arduino Robotic ARM Serial Connection

This is an example program for controlling a robotic arm
The Robotic ARM is built using the DIY 6-Axis Arm (+ the craw) and then integrated it with an Arduino 
1. The SainSmart DIY 6-Axis Arm is an off-the-shelf robot arm and a mechanical craw is integrated with the arm (more info: http://wiki.sainsmart.com/index.php/DIY_6-Axis_Servos_Control_Palletizing_Robot_Arm_Model_for_Arduino_UNO_MEGA2560)
2. Arduino compatible device (Intel Curie Module or Arduino UNO): 
- https://www.intel.com/content/www/us/en/support/products/94036/boards-and-kits/intel-curie-modules.html
- https://store.arduino.cc/arduino-uno-rev3	
3. 4AA battery packs x2

The motors of the robotic arm is connected to the Arduino's I/O port 2-7, and the craw is connected to port 8.
The power and ground of all motors are directly connected to the AA battery packs.
Note: 2 battery packs can be connnected in parallel to extend the battery power.

This program basically allows the user to control each motor of the robotic arm through the serial port connection.
In addition, a python program is also provided for user to use python to send command to robotic arm via the serial port. 

 
