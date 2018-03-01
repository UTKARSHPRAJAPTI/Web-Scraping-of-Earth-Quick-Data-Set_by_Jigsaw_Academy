from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import os
import json
'''
url=("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2016-10-01&endtime=2016-10-02")
data=requests.get(url)
data=data.json()
type(data)
print(data.keys())
data=data['features']
'''
earthquake_file=open('earthquake_details1.1.json','w')                                                      #create a new json file
def  earthquake_api(starttime,endtime):
    url='https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime='+starttime+'&endtime='+endtime+''
    str_response=requests.get(url)
    json_response = json.loads(str_response.text) 
    earthquake_file.write(json.dumps(json_response,indent=3)) #write item in new file dumps work like BeautifulSoup
    earthquake_file.write("\n")
    print(earthquake_file)
    

def main():
    starttingdate='2016-10-01'
    endingdate='2016-10-02'
    
    earthquake_api(starttingdate,endingdate)

if __name__ == '__main__':
    main()