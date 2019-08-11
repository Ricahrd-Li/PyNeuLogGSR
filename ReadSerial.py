import serial 
import datetime as dt 
import pyautogui

ser = serial.Serial('COM4', 9600)

if __name__ == '__main__':
    # print(pyautogui.position())
    while 1:
        signal = ser.readline()
        if  signal == b'1\r\n' : 
            print(dt.datetime.now().strftime('%H:%M:%S') + ": Button Pressed")    

        elif signal == b'0\r\n' : 
            print(dt.datetime.now().strftime('%H:%M:%S') + ": Button Released") 
                    
        elif signal == b'2\r\n' :
            startTime = dt.datetime.now().strftime('%H:%M:%S') 
            pyautogui.click(580, 95) 
            pyautogui.click(580, 95)             
            print( startTime + ": Exp Starts!!") 

