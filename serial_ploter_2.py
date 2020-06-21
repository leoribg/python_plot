import serial
import matplotlib.pyplot as plt
from drawnow import *
import numpy as np

values = []
valuesx = []
valuesy = []
valuesz = []

plt.ion()
cnt=0
x = 0
y = 0
z = 0

serialArduino = serial.Serial('COM8', 115200)

def plotValues():
    plt.subplot(411)
    plt.title('Values of X')
    plt.ylim(0, 255)
    plt.plot(valuesx,'r')
    plt.subplot(412)
    plt.title('Values of Y')
    plt.ylim(0, 255)
    plt.plot(valuesy,'g')
    plt.subplot(413)
    plt.title('Values of Z')
    plt.ylim(0, 255)
    plt.plot(valuesz,'b')

    #plt.title('Serial value from Arduino')
    #plt.grid(True)
    #plt.ylabel('Values')
    #plt.plot(valuesx, 'rx-', label='values')
    #plt.legend(loc='upper right')

#pre-load dummy data
for i in range(0,26):
    values.append(0)
    valuesx.append(0)
    valuesy.append(0)
    valuesz.append(0)
    
while True:
    while (serialArduino.inWaiting()==0):
        pass
    valueRead = serialArduino.readline()
    #valueRead = serialArduino.read(1)

    print(valueRead)
    array = valueRead.split()
    if len(array) > 0:
        x = array[14]
        y = array[15]
        z = array[16]
        ch = str(x,'utf-8')
        b = x.decode('utf-8')
        x = int(str(b), 16)
        b = y.decode('utf-8')
        y = int(str(b), 16)
        b = z.decode('utf-8')
        z = int(str(b), 16)
    #check if valid value can be casted
    try:
        valueInInt = int(x)
        valuexInInt = int(x)
        valueyInInt = int(y)
        valuezInInt = int(z)
        print(valuexInInt)
        print(valueyInInt)
        print(valuezInInt)
        if valueInInt <= 1024:
            if valueInInt >= 0:
                values.append(valueInInt)
                values.pop(0)
                valuesx.append(valuexInInt)
                valuesx.pop(0)
                valuesy.append(valueyInInt)
                valuesy.pop(0)
                valuesz.append(valuezInInt)
                valuesz.pop(0)
                drawnow(plotValues)
            else:
                print ("Invalid! negative number")
        else:
            print ("Invalid! too large")
    except ValueError:
        print ("Invalid! cannot cast")