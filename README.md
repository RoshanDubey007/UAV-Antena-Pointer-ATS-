# UAS-AVIONICS-TASK
## UAS RECRUITMENT TASK
Task Name: Unmanned Aerial Vehicle (UAV) Antenna Tracking System (ATS) Design using MATLAB

Applicant Details:
Name: Roshan Kumar Dubey
Branch: Electronics and Communication
Department: Avionics
Roll Number: 2K22/A18/08

Task Description:
The objective of this task is to design an antenna tracking system for a UAV that accurately tracks its motion and maintains a strong signal connection. The system must be able to compute the appropriate direction and orientation of the antenna based on the UAV's position and velocity, and adjust the antenna in real-time. The mathematical formulation of the system should be implemented using MATLAB.

Code Summary:
The antenna tracking system is designed using MATLAB code, where the initial coordinates of the UAV, (x0, y0, z0), and the initial orientation of the antenna, phi and theta, are set through user input. The motion of the UAV with respect to time is described by the following equations:

x = 7t^2
y = 13t^2
z = 8*tan(t)

The velocities in the respective axes are then computed as:

Vx = 14t
Vy = 26t
Vz = 8(sec(t))^2

To determine the final orientation of the antenna, the final values of theta and phi, namely theta_final and phi_final, are computed using the principles of polar coordinate geometry. The direction of the antenna is then adjusted in real-time to track the UAV's motion.

A loop is implemented to simulate the UAV's motion from t = 0 to t = final time with a user-defined step size. As the coordinates of the x, y, and z axes change accordingly, the direction and orientation of the antenna change to achieve the task's ultimate objective - to give the final pointing of the antenna.

In summary, the implemented MATLAB code computes the appropriate direction and orientation of the antenna based on the UAV's position and velocity and adjusts the antenna in real-time to maintain a strong signal connection.