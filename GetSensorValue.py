import json
import requests
import time 

def startExp():
        # rate = input("Rate:\n\
        #         1 = 10000 per second\n\
        #         2 = 3000 per second\n\
        #         3 = 2000 per second\n\
        #         4 = 1000 per second\n\
        #         5 = 100 per second\n\
        #         6 = 50 per second\n\
        #         7 = 20 per second\n\
        #         8 = 10 per second\n\
        #         :")
        rate = '6'
        sampleNum = '50' # 1s
        requests.get(url = "http://localhost:22002/NeuLogAPI?StartExperiment:[GSR],[1],["+ rate + "],[" + sampleNum + "]")

def stopExp():
        requests.get(url = "http://localhost:22002/NeuLogAPI?StopExperiment")

def getSamples():
        timeStamp = []
        # begin time 
        timeStamp.append(time.time()*1000.0)
        data = requests.get(url = "http://localhost:22002/NeuLogAPI?GetExperimentSamples:[GSR],[1]").json()['GetSensorValue'][0]
        if(len(data) > 0):
                data.pop(0)
                data.pop(0)


def getSensorValue():
        data = requests.get(url = "http://localhost:22002/NeuLogAPI?GetSensorValue:[GSR],[1]").json()
        data = data['GetSensorValue'][0]
        print(data)
        return data

