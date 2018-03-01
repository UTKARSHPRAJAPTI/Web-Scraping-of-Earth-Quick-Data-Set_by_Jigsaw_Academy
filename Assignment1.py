import json
from pprint import pprint
import pandas as pd
import os

   
def main():
    i=0
    
    with open('earthquake_details1.1.json') as file:
        dict_data = json.load(file)
        i=len(dict_data['features'])
        print(len(dict_data['features']))
        print (type(dict_data['features']))

        feature_data= dict_data['features']
        print(feature_data[0])
        print(type(feature_data[0]))
    
    lat=[]
    lng=[]
    title=[]
    place=[]
    mag=[]

    for d in range(i):
        lat.append(dict_data['features'][d]['geometry']['coordinates'][0])
        
        lng.append(dict_data['features'][d]['geometry']['coordinates'][1])
        
        title.append(dict_data['features'][d]['properties']['place'])
        place.append (dict_data['features'][d]['properties']['title'])
        mag.append(dict_data['features'][d]['properties']['mag'])
    
    Data_Frame=pd.DataFrame({'Lat':lat,'Long':lng,'Title':title,'Place':place,'Magnitude':mag})
    os.chdir('D:\\coding ninjas notes\\Data Science With Python\\T02 Scientifuc Distribustions Used In Python For Data Science\\Graded assignment')
    Data_Frame.to_csv('data.csv',index=False)   
    
    mag_two = Data_Frame.loc[Data_Frame['Magnitude'] > 2]
    print (mag_two.count())

    plc_gr_cali = Data_Frame[Data_Frame['Place'].str.contains("California")]
    print (plc_gr_cali.count())
    mag_fiv = Data_Frame.loc[Data_Frame['Magnitude'] > 5]
    print (mag_fiv.count())

if __name__ == '__main__':     # if the function is the main function ...
    main() # ...call it