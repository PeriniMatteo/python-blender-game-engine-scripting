
import bge
import serial
#import time

cont = bge.logic.getCurrentController()
obj = cont.owner

sens = cont.sensors["readSer"] #the name of the Blender sensor connected to this control

serialport = serial.Serial('/dev/ttyUSB0', 9600)  

def readSer():

    if sens.positive:  #only want one value set from the sensor each loop
        try:
            line=serialport.readline().decode('ascii') #read a line from the serial port
            #print(line)
            obj.applyRotation([float(line), 0, 0], 0) # apply the rotation on the x axes 
            #time.sleep(0.05)
        except:
            print("Exception")
