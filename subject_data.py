# -*- coding: utf-8 -*-
"""
Created on Thu May  5 22:31:45 2022

@author: tz2916
"""


import datetime
import os
import pickle
import pandas as pd
from tqdm import tqdm


def CGM_text2csv(data_dir,basedate=datetime.date(2015, 5, 22)):
    dt = 'HDeviceCGM'
    isheader = True
    csv_dir = data_dir+'csv/'+dt+'.csv'
    
    if not os.path.exists(csv_dir):
        print('Covert CGM data')
        
        with open(data_dir+dt+'.txt') as f:
            with open(csv_dir, 'w') as export:
                for line in f:
                    #Work line by line within the file
        
                    if isheader:
                        #Executes on the first iteration i.e. when reading the header
                        
                        isheader = False
                        #All future lines will not be header lines
        
                        export.write("\"id\",\"time\",\"bgl\"\n")
                        #Write the export file's header
        
                        continue
                        #Move to the next iteration without executing the rest of the code
        
                    line = line.split('|')
                    #Split the data by delimiting character so it can be worked with
        
                    day = datetime.timedelta(days = int(line[4]))
                    #obtain the "number of days since enrolled in study" field in a way useful for doing date arithmetic 
        
                    thisdate = basedate + day
                    #Create the date that will get written to the file
        
                    thistime = datetime.datetime.strptime(line[5], "%H:%M:%S").time()
                    #Read the reading time as a time object
        
                    thedatetime = datetime.datetime.combine(thisdate,thistime)
                    #Combine the read date and time objects
        
        
                    export.write(str(line[2]) + "," + str(thedatetime) + "," + line[9][0:3] + "\n")

def bolus_text2csv(data_dir,basedate=datetime.date(2015, 5, 22)):
    dt = 'HDeviceBolus'
    isheader = True
    csv_dir = data_dir+'csv/'+dt+'.csv'
  
    if not os.path.exists(csv_dir):
        print('Covert bolus data')
        
        with open(data_dir+dt+'.txt') as f:
            with open(csv_dir, 'w') as export:
                for line in f:
                    #Work line by line within the file
        
                    if isheader:
                        #Executes on the first iteration i.e. when reading the header
                        
                        isheader = False
                        #All future lines will not be header lines
        
                        export.write("\"id\",\"time\",\"bolus\"\n")
                        #Write the export file's header
        
                        continue
                        #Move to the next iteration without executing the rest of the code
        
                    line = line.split('|')
                    #Split the data by delimiting character so it can be worked with
        
                    day = datetime.timedelta(days = int(line[4]))
                    #obtain the "number of days since enrolled in study" field in a way useful for doing date arithmetic 
        
                    thisdate = basedate + day
                    #Create the date that will get written to the file
        
                    thistime = datetime.datetime.strptime(line[5], "%H:%M:%S").time()
                    #Read the reading time as a time object
        
                    thedatetime = datetime.datetime.combine(thisdate,thistime)
                    #Combine the read date and time objects
        
                    bolustype = line[6]
                    if bolustype =='normal' or bolustype =='Normal':
                        export.write(str(line[2]) + "," + str(thedatetime) + "," + line[9] + "\n")
                        
                    elif bolustype =='square':
                        extime = round(int(line[13])/60000/5)
                        for i in range(0,extime):
                            thedatetime = datetime.timedelta(minutes=5)+thedatetime
                            export.write(str(line[2]) + "," + str(thedatetime) + "," + line[11] + "\n")
                            
                    elif bolustype =='dual/square':   
                        
                        export.write(str(line[2]) + "," + str(thedatetime) + "," + line[9]+ "\n")
                        extime = round(int(line[13])/60000/5)
                        for i in range(1,extime):
                            thedatetime = datetime.timedelta(minutes=5)+thedatetime
                            export.write(str(line[2]) + "," + str(thedatetime) + "," + line[11] + "\n")
                             
                    elif bolustype == 'Combination':
                      export.write(str(line[2]) + "," + str(thedatetime) + "," + line[9]+ "\n")
                      extime = round(int(line[13])/5)
                      for i in range(1,extime):
                          thedatetime = datetime.timedelta(minutes=5)+thedatetime
                          export.write(str(line[2]) + "," + str(thedatetime) + "," + line[11] + "\n") 
                          
                    else:
                        print(f"No such type:{line[:7]}")
        

              
data_dir ='Data Tables/'
csv_dir =  data_dir+'csv/'             
if not os.path.exists(csv_dir):
    CGM_text2csv(data_dir)
    bolus_text2csv(data_dir)
 
df_bolus = pd.read_csv(csv_dir+'HDeviceBolus.csv',parse_dates=['time']).sort_values(by=['time','id'],ignore_index=True)
df_CGM = pd.read_csv(csv_dir+'HDeviceCGM.csv',parse_dates=['time']).sort_values(by=['time','id'],ignore_index=True)
df_all = pd.merge_asof(df_CGM, df_bolus,
                      on='time',
                      by='id',
                      direction='nearest',
                      tolerance=pd.Timedelta('2.5min'))
df_all = df_all.fillna(0)
df_all = df_all.sort_values(by=['id','time'],ignore_index=True)
id_set = df_all.id.unique()
idx = pd.Series(dtype='int64')
for pid in tqdm(id_set):
    
    df_p = df_all[df_all.id==pid]
    ts = df_p.time
    dt = round((ts-ts.iloc[0])/pd.Timedelta('5min'))
    idx = pd.concat([idx,dt])
df_all['idx'] = idx
df_all = df_all.drop_duplicates(subset=['id','idx'])

save_df = 0
if save_df:
     with open("./all_data_REPLACE-BG.pkl","wb") as f:
        pickle.dump(df_all, f)        
