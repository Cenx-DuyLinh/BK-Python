class PID:
    def __init__(self,KP,KD,KI,tau,dt,error) -> None:
        self.KP = KP
        self.KI = KI
        self.KD = KD
        self.tau = tau
        self.dt = dt    
        self.error = error
        self.error_old = 0
        self.I = 0
        self.D = 0
    def compute_thrust (self):
        self.P = self.KP * self.error
        self.I = ((self.KI * self.dt)/2)*(self.error + self.error_old) + self.I
        self.D = (2*self.KD/(2*self.tau+self.dt))*(self.error - self.error_old)+ ((2*self.tau-self.dt)/(2*self.tau+self.dt))*self.D
        self.error_old = self.error
        self.thrust = self.I + self.P + self.D
        return self.thrust
class Drone:
    def __init__(self,weight,current_height,destination_height,acceleration,velocity,g,thrust,dt) -> None:
        self.thrust = thrust
        self.dt = dt
        self.weight = weight
        self.g = g 
        self.destination_height = destination_height
        self.current_height = current_height
        self.current_height = current_height
        self.acceleration = acceleration
        self.velocity  = velocity
    def compute_acceleration(self):
        self.acceleration = self.thrust / self.weight - self.g
    def compute_velocity(self):
        self.velocity = self.acceleration * self.dt
    def compute_height(self):
        self.current_height = self.current_height + self.velocity*self.dt + 0.5* self.acceleration*(self.dt**2)
    def update_error(self):
        return (self.destination_height - self.current_height)
    
def RUN():
    import time
    #Drone Info-----------------------------------------------------------
    weight= 10 #kg
    current_height = 0 #m
    destination_height = 20 #m
    velocity = 0 #m/s
    acceleration = 0 #m/s2
    g = 9.806 #m/s2 
    thrust = 0 #Newton
    #PID Info--------------------------------------------------------------
    KP = 10
    KD = 0.05
    KI = 1.5
    tau = 0.005
    dt = 0.3 #s
    #----------------------------------------------------------------------
    
    object_drone = Drone(weight,current_height,destination_height,acceleration,velocity,g,thrust,dt)
    object_propeller = PID(KP,KD,KI,tau,dt,destination_height-current_height)

    while True:
        object_drone.thrust = object_propeller.compute_thrust()
        object_drone.compute_acceleration()
        object_drone.compute_height()
        print(f'Current height:{object_drone.current_height:.3f}m, P: {object_propeller.P:.3f}, D:{object_propeller.D:.3f}, I:{object_propeller.I:.3f}, thrust:{object_propeller.thrust:.3f}N')
        object_drone.compute_velocity()
        object_propeller.error = object_drone.update_error()
        time.sleep(dt)

if __name__ == '__main__':
    RUN()