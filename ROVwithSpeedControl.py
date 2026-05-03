import pygame 
import time
from time import sleep  
from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Button
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory  

factory = PiGPIOFactory(host='192.168.0.202')

UpCam = LED(13, pin_factory=factory)
LeftHorizontal = Servo(20, pin_factory=factory)
RightHorizontal = Servo(21, pin_factory=factory)
Left45 = Servo(19, pin_factory=factory)
Right45 = Servo(26, pin_factory=factory)
twist = Servo(6, pin_factory=factory)
hand = Servo(5, pin_factory=factory)
cam = 0
claw = 0.00
arm = 0.00
speed = 3.7

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)
pygame.init()
direction = int
power = float(0.00)
pwm = float(0.00)

def left_forward():
    pwm = abs(power)     
    LeftHorizontal.value=-pwm
    
def left_reverse():
    pwm = abs(power)
    LeftHorizontal.value=pwm

def left_forward_reverse_stop():
    LeftHorizontal.value=0

def left_up():
    pwm = abs(power)  
    Left45.value=pwm
    
def left_down():
    pwm = abs(power)  
    Left45.value=-pwm  

def left_up_down_stop():
    Left45.value=0
    
def right_forward():
    pwm = abs(power)
    RightHorizontal.value=pwm
      
def right_reverse():
    pwm = abs(power)
    RightHorizontal.value=-pwm
    
def right_forward_reverse_stop():
    RightHorizontal.value=0

def right_up():
    pwm = abs(power)  
    Right45.value=-pwm
    
def right_down():
    pwm = abs(power) 
    Right45.value=pwm
     
def right_up_down_stop():
    Right45.value=0
    
def red_stop():
    print('EMERGENCY STOP')
    LeftHorizontal.value=0.00
    RightHorizontal.value=0.00 
    Left45.value=0.00
    Right45.value=0.00
    
    
def camoff():
    print('Cam DOWN')
    UpCam.off()
    
    
def camon():
    print ('Cam UP')
    UpCam.on()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:            
            direction = (event.axis)
            power = (event.value)
            power = (power/speed)
            power = round(power,2)
            print (power, " ", direction)
            
            # LEFT MOTORS CODE
        
            # direction == 1 left stick 
            if direction == 1 and power < -0.02: 
                left_forward()
        
            
            if direction == 1 and power  > 0.02:
                left_reverse()
            
            if direction == 1 and abs((power) < 0.01) and abs((power) >-0.01):
                left_forward_reverse_stop()
            
            # direction 0 = left stick horizontal axis
            if direction == 0 and power < -0.02:
                left_up()
            
            if direction == 0 and power > 0.02:
                left_down()
            
            if direction == 0 and abs((power) < 0.01) and abs((power) >-0.01):
                left_up_down_stop()
            
            
            #  RIGHT MOTORS CODE
            if direction == 3 and power < -0.02: 
                right_forward()
            
            if direction == 3 and power > 0.02:
                right_reverse()
            
            if direction == 3 and abs((power) < 0.01) and abs((power) >-0.01):
                right_forward_reverse_stop()
                       
            if direction == 2 and power > 0.02:
                right_up()
                
            if direction == 2 and power < -0.02:
                right_down()
            
            if direction == 2 and abs((power) < 0.01) and abs((power) >-0.01):
                right_up_down_stop()
                               
        if event.type == pygame.JOYBUTTONDOWN:
         
            if event.button == 2:
                red_stop()  #  This is where the EMERGENCY STOP event is detected.
         
            if event.button == 4:
                speed = (speed + 1.1)
                if speed >= 7:
                    speed = 7
                print (speed)
         
            if event.button == 5:
                speed = (speed - 1.1)
                if speed <= 2.6:
                    speed = 2.6
                print (speed)
          
            if event.button == 9:
                if cam == 0:
                    cam = 1
                    camon()
                else:
                    cam = 0
                    camoff()
         
