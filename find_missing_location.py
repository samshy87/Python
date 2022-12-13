import pandas as pd
df=pd.DataFrame({'Name':['2022-12-14','2022-12-14','2022-12-14','2022-12-14','2022-11-13','2022-11-13','2022-11-13','2022-11-13','2022-10-12','2022-10-12','2022-10-12','2022-09-11','2022-09-11','2022-09-11','2022-09-11','2022-08-10','2022-08-10','2022-08-10','2022-08-10','2022-07-09','2022-07-09','2022-07-09','2022-07-09'],
     'FT_Team':['WHITEMAN','BUCKLEY','MAXWELL','EDWARDS','WHITEMAN','BUCKLEY','MAXWELL','EDWARDS','WHITEMAN','BUCKLEY','MAXWELL','WHITEMAN','BUCKLEY','MAXWELL','EDWARDS','WHITEMAN','BUCKLEY','MAXWELL','EDWARDS','WHITEMAN','BUCKLEY','MAXWELL','EDWARDS',]})
print(df)
print(" ")
teamNames = ['WHITEMAN','BUCKLEY','MAXWELL','EDWARDS']
fNames = (df['Name'].unique())

#nested for loop to search through each unique name for a specific team name
for i in teamNames:
    for x in fNames:
        # the ~ in front of df.loc is used to say when x is NOT in FT_Team.  
        # its used to make 'isin' effectively 'notin'.
        df2=~df.loc[(df['Name']==x),'FT_Team'].isin([i])
        print(df2)

#each printed line is a boolean check if that Team name is there or not.  
#To go from here, in your code you'll need to check for a return value of true, that will mean whatever name you are searching for is not there and then do whatever action is required after.
