import serial 
import datetime as dt 
import pyautogui
import random

ser = serial.Serial('COM4', 9600)
i = 0 

if __name__ == '__main__':
    # print(pyautogui.position())
    while 1:
        signal = ser.readline()
        # print(signal.decode("ascii"))
        if  signal == b'4\r\n' :
            pyautogui.click(580, 95) 
            pyautogui.click(580, 95)      
            t = "Exp Starts!\n"       
            i = 0
            print(t)   
            f = open("expData.txt","w+") 
            f.write(t)

        elif signal == b'2\r\n' : 
            i += 1 
            t = str(i)+"--->"+ ser.readline().decode("ascii")[:-2] + ": Pinch start\n" 
            print(t) 
            f.write(t)

        elif signal == b'3\r\n' : 
            t = ser.readline().decode("ascii")[:-2] + ": Pinch end\n\n"
            print(t)  
            f.write(t)

                    
        elif signal == b'1\r\n' : 
            t = ser.readline().decode("ascii")[:-2] + ": Exp end!"
            f.write(t)
            f.close()
            print(t)  

