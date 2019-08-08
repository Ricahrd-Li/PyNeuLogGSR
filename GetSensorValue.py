import json
import requests

def getSensorValue():
        data = requests.get(url = "http://localhost:22002/NeuLogAPI?GetSensorValue:[GSR],[1]").json()
        data = data['GetSensorValue'][0]
        print(data)
        return data

def exp():
        # startExpURL = "http://localhost:22002/NeuLogAPI?StartExperiment:[GSR],[1],"
        # print("------------------- Neulog -------------------")
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
        sampleNum = input("sample number:")

        # startExpURL = startExpURL + '['+ rate +'],[' + sampleNum + ']'

        # print(startExpURL)

        # start = input("start exp? [y/n]: ")
        # if(start == "y"):
        #     get = requests.get(url = startExpURL)

        # Get data from sensor
        # data = []
        # getSamplesURL = "http://localhost:22002/NeuLogAPI?GetExperimentSamples:[GSR],[1]"
        # data = requests.get(url = getSamplesURL).json()
        # dataList = data["GetExperimentSamples"][0]
        # if(len(dataList) > 0):
        #     dataList.pop(0)
        #     dataList.pop(0)
        for i in range(0, int(sampleNum)):
                data = requests.get(url = "http://localhost:22002/NeuLogAPI?GetSensorValue:[GSR],[1]").json()
                data = data['GetSensorValue'][0]
                print(data)
                Draw.draw(data)

# requests.get(url = "http://localhost:22002/NeuLogAPI?StopExperiment")

if __name__ == '__main__':
        exp()



