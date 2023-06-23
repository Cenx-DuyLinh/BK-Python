import time
import numpy as np
import matplotlib.pyplot as plt
import turtle 
from PID_Kalman_Module import *

#GLOBAL PARAMS
timer = 0
setpoint = 0
sim_time = 1000
x_init = 0
y_init = -4
mass = 2 #kg
min_thrust = 0 #N
max_thrust = 40 #N
g = -9.81 #m/s2
v_initial = 0 #initial velocity
thrust_update_frequency = 50 #Hz
noise_intensity = 0.01

#PID GAINS Ziegler–Nichols method
Ku = 50 
Tu = 315 * 0.016

#Ku test for 50Hz
# KP = 50
# KI = 0
# KD = 0

#Classic PID
KP = 0.6 * Ku 
KI = 1.2 * Ku / Tu *2.5
KD = 0.075 * Ku * Tu *4

class Drone():
    def __init__(self):
        self.Drone = turtle.Turtle()
        self.Drone.shapesize(3,3)
        self.Drone.shape('square')
        self.Drone.color('black')
        self.Drone.penup()
        self.Drone.goto(x_init, y_init)
        self.Drone.speed(0)
        
        self.ddy = 0
        self.dy = v_initial
        self.y = y_init

    def get_ddy(self):
        return self.ddy
    
    def get_dy(self):
        return self.dy
    
    def get_y(self):
        return self.Drone.ycor()/100

    def update(self, thrust, dt):
        self.ddy = g + thrust / mass
        self.dy += self.ddy * dt
        self.y += self.dy * dt
        self.Drone.sety(self.y*100)
        
class Simulation():
    def __init__(self):
        self.DroneObject = Drone()
        self.thrust_pid = PID(KP, KI, KD, KN = 5, antiWindup= True)
        self.thrust_pid.setLims(min_thrust, max_thrust)
        self.screen = turtle.Screen()
        self.screen.setup(500,900,250,50)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(180)
        self.marker.goto(60, setpoint)
        self.marker.color('red')
        self.sim = True
        self.KalmanFilter = False 
        self.timer = 0
        self.yposition = []
        self.times = []
        self.kpe = []
        self.kie = []
        self.kde = []
        self.thrust = []
        self.DT = []
        self.Y_KALMAN = []
        self.Y_MEASURE = []
        self.time_interval = 1 / thrust_update_frequency
        self.NOISE = np.random.normal(0, noise_intensity, sim_time)
        self.kalmanfilter = Kalman()
        
    def graph(self, x, y1, y2, y3, y4):
        fig, (ax1, ax2) = plt.subplots(2, sharex= True)
        ax1.set(ylabel='Rocket \nHeight')
        ax1.plot(x,y1)
        ax1.plot(x,y3,'tab:red')
        ax1.plot(x,y4,'tab:green')
        ax1.grid()
        ax2.set(ylabel='Rocket \nThrust')
        ax2.plot(x,y2,'tab:brown')
        ax2.grid()
        ax2.set(xlabel='Simulation Time')
        plt.show()
        
    def loop(self):
        dt = 0.1
        elapsed_time = 0
        drone_thrust = -2*g
        y_measure, y_kalman = 0, 0
        while (self.sim):
            t1 = time.time()
            y_position = self.DroneObject.get_y()
            y_measure = y_position + self.NOISE[int(self.timer-1)]
            if elapsed_time >= self.time_interval:
                if (self.KalmanFilter):
                    y_kalman = self.kalmanfilter.Filter(y_measure)[0]
                    drone_thrust = self.thrust_pid.compute(float(y_kalman), 0, dt)
                else: drone_thrust = self.thrust_pid.compute(y_measure, 0, dt)
                elapsed_time = 0
            #print(drone_thrust,self.DroneObject.get_y(), dt)
            self.DroneObject.update(drone_thrust, dt)
            t2 = time.time()
            dt = t2 - t1
            self.DT.append(dt)
            elapsed_time += dt
            self.timer += 1
            if self.timer > sim_time:
                print("Sim ended")
                self.sim = False
            elif self.DroneObject.get_y() > 1000 or self.DroneObject.get_y() < -1000:
                print("Out of bounds")
                self.sim = False
            
            self.yposition.append(y_position)
            self.times.append(self.timer)
            self.thrust.append(drone_thrust)
            self.Y_MEASURE.append(y_measure)
            self.Y_KALMAN.append(float(y_kalman))
            
        print("Simulation update frequency: ", 1/np.average(self.DT))
        self.graph(self.times, self.yposition, self.thrust, self.Y_MEASURE, self.Y_KALMAN)
        
def main():
    sim = Simulation()
    sim.loop()
    
if __name__ == '__main__':
    main()