import pandas as pd
df=pd.DataFrame({'DateTime':['2022-12-14','2022-12-14','2022-12-14','2022-12-14','2022-11-13','2022-11-13','2022-11-13','2022-11-13','2022-10-12','2022-10-12','2022-10-12','2022-09-11','2022-09-11','2022-09-11','2022-09-11','2022-08-10','2022-08-10','2022-08-10','2022-08-10','2022-07-09','2022-07-09','2022-07-09','2022-07-09'],
     'Location':['WHITEMAN','BUCKLEY','MAXWELL','EDWARDS','WHITEMAN','BUCKLEY','MAXWELL','EDWARDS','WHITEMAN','BUCKLEY','MAXWELL','WHITEMAN','BUCKLEY','MAXWELL','EDWARDS','WHITEMAN','BUCKLEY','MAXWELL','EDWARDS','WHITEMAN','BUCKLEY','MAXWELL','EDWARDS',]})

#Locations to search for
Bases = ['WHITEMAN','BUCKLEY','MAXWELL','EDWARDS']
#list of unique dates
Dates = (df['DateTime'].unique())

#nested for loop to search through each unique date for a specific location
for i in Dates:
    for x in Bases:
        df2=df.query("DateTime == @i")
        df3=df2.query("Location == @x")
        if df3.empty: print('Location ' + x + ' not found on ' + i)

#Last line checks if the query came back with nothing, and if so prints out that location and time as missing.  In this test dataset, I made the 2022-10-12 date missing just Edwards AFB.
