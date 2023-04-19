clc, clearvars

% Define the initial position of the UAV
x0 = input("initial x-axis position : ");
y0 = input("initial y-axis position : ");
z0 = input("initial z-axis position : ");

% Define the initial direction of the antenna
theta_i = input("initial azimuthal angle of antenna : ");
phi_i = input("initial elevation angle of antenna : ");

% Define the initial time, final time and step size
t0 = input("initial time : ");
tf = input("final time : ");
dt = input("step size : ");

% Define the equation of motion wrt variable 't'
t = linspace(t0, tf, dt);
x = @(t) t.*3;
y = @(t) t.*4;
z = @(t) 5*tan(t);
X = x(t);
Y = y(t);
Z = z(t);

% Define the velocity at a time 't'
Vx = diff(X)./diff(t);
Vy = diff(Y)./diff(t);
Vz = diff(Z)./diff(t);

% Setting polar coordinates of the UAV
r = sqrt(X.^2 + Y.^2 + Z.^2);
phi_f = acos(sqrt(X.^2 + Y.^2)/r);
theta_f = acos(X./(r * cos(phi_f)));

% Computing the azimuthal and altitudnal angle moved
theta = theta_f(end) - theta_i;
phi = phi_f(end) - phi_i;
omega1 = theta/t;
omega2 = phi/t;

% Starting the tracking of UAV
disp("final coordinates of the UAV is : ")
disp("X coordinate : ", X(end)-x0)
disp("Y coordinate : ", Y(end)-y0)
disp("Z coordinate : ", Z(end)z0)
disp("final velocity of the UAV is : ")
disp("Velocity in X-direction : ", Vx(end))
disp("Velocity in Y-direction : ", Vy(end))
disp("Velocity in Z-direction : ", Vz(end))

% Tracking of the orientation of the antenna
disp("Final azimuthal angle of the antenna is : ", theta)
disp("Angular velocity of the antenna in direction of azimuthal angle is : ", omega1)
disp("Final altitudnal angle of the antenna is : ", phi)
disp("Angular velocity of the antenna in the direction of altitudnal angle is : ", omega2)
