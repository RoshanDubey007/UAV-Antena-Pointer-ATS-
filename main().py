import sympy as sp
import numpy as np
t = sp.Symbol ('t')


# theta = azimuthal angle
# phi = altitudnal angle

# Define the initial position of the UAV
x0 = int(input("initial x-axis position : "))
y0 = int(input("initial y-axis position : "))
z0 = int(input("initial z-axis position : "))

# Define the initial direction of the antenna
theta_i = int(input("Enter the azimuth of antenna : "))
phi_i = int(input("Enter the elevation of antenna : "))

# Define the initial time and final time
t0 = int(input("Enter initial time : "))
tf = int(input("Enter final time : "))

# Define the equation of motion at a time "t"
x = 3*t
y = 4**t
z = 5*sp.tan(t)

# Define the velocity at a time "t"
Vx = sp.diff(x,t)
Vy = sp.diff(y,t)
Vz = sp.diff(z,t)

# Define the functions for the respective equation of motion and velocities
def X(t):
    x = 3*t
    return x

def Y(t):
    y = 4**t
    return y

def Z(t):
    z = 5*np.tan(t)
    return z

def VX (T):
    VX = Vx.subs(t,T)
    return VX

def VY (T):
    VY = Vy.subs(t,T)
    return VY

def VZ (T):
    VZ = Vz.subs(t,T)
    return VZ    

# Setting polar coordinates of the UAV 
r = sp.sqrt((x**2) + (y**2) + (z**2))
phi_f = sp.acos((sp.sqrt(x**2) + (y**2))/r)
theta_f = sp.acos(x/(r * sp.cos(phi_f)))

# Computing the azimuthal and altitudnal angle moved
def THETA ():
    global theta
    theta = theta_f - theta_i
    THETA = theta.subs(t,T)
    return THETA
    
def PHI ():
    global phi
    phi = phi_f - phi_i
    PHI = phi.subs(t,T)
    return PHI

def OMEGA1 ():    
    omega1 = theta/t
    OMEGA1 = omega1.subs(t,T)
    return OMEGA1

def OMEGA2 ():
    omega2 = phi/t
    OMEGA2  = omega2.subs(t,T)
    return OMEGA2
    
# Start the tracking of UAV
T = tf-t0
print("final co-ordinates of the UAV is : (", X(T), " , ", Y(T), " , ", Z(T), ")")
print()
print("final velocity of the UAV is : (", VX(T), " , ", VY(T), " , ", VZ(T), ")")

# Tracking of the orientation of the antenna
print("The final azimuthal angle of the antenna is : ", THETA())
print("The final angular velocity for azimuthal angle of the antenna is : ", OMEGA1())
print("The final altitudnal angle of the antenna is : ", PHI())
print("The final angular velocity for altitudnal angle of the antenna is : ", OMEGA2())
