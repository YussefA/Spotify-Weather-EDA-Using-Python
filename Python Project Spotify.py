import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity
from typing import Match

df = pd.read_csv("C:/Users/yusse/OneDrive/Desktop/Python Project DataSets/spotify_weather_data.csv")
# Data Analysis for the weather type Fog
fog = df[df["Weather"] == "Fog"]
max = fog['Popularity'].max()

sortedFog = fog.sort_values("Popularity", ascending=False)
sortedFog = sortedFog[sortedFog.index <=399]

def getFog():
    print(sortedFog.iloc[0]["Track Name"], ":", sortedFog.iloc[0]["Artist"], ":", sortedFog.iloc[0]["Popularity"])


# Data Analysis for the weather type Rain
rain = df[df["Weather"] == "Rain"]
sortedRain = rain.sort_values("Popularity", ascending=False)
sortedRain = sortedRain[sortedRain.index <=399]


def getRain():
    print(sortedRain.iloc[0]["Track Name"], ":", sortedRain.iloc[0]["Artist"], ":", sortedRain.iloc[0]['Popularity'])


# Data Analysis for the weather type Mist
mist = df[df["Weather"] == "Mist"]
sortedMist = mist.sort_values("Popularity", ascending=False)
sortedMist = sortedMist[sortedMist.index <=399]


def getMist():
    print(sortedMist.iloc[0]["Track Name"], ":", sortedMist.iloc[0]["Artist"], ":", sortedMist.iloc[0]['Popularity'])


# Data Analysis for the weather type Snow
snow = df[df["Weather"] == "Snow"]
sortedSnow = snow.sort_values("Popularity", ascending=False)
sortedSnow = sortedSnow[sortedSnow.index <=399]


def getSnow():
    print(sortedSnow.iloc[0]["Track Name"], ":", sortedSnow.iloc[0]["Artist"], ":", sortedSnow.iloc[0]['Popularity'])


# Data Analysis for the weather type Drizzle
drizzle = df[df["Weather"] == "Drizzle"]
sortedDrizzle = drizzle.sort_values("Popularity", ascending=False)
sortedDrizzle = sortedDrizzle[sortedDrizzle.index <=399]


def getDrizzle():
    print(sortedDrizzle.iloc[0]["Track Name"], ":", sortedDrizzle.iloc[0]["Artist"], ":",
          sortedDrizzle.iloc[0]['Popularity'])


# Data Analysis for the weather type Thunderstorm
thunderstorm = df[df["Weather"] == "Thunderstorm"]
sortedThunderstorm = thunderstorm.sort_values("Popularity", ascending=False)
sortedThunderstorm = sortedThunderstorm[sortedThunderstorm.index <=399]


def getThunder():
    print(sortedThunderstorm.iloc[0]["Track Name"], ":", sortedThunderstorm.iloc[0]["Artist"], ":",
          sortedThunderstorm.iloc[0]['Popularity'])


# Data Analysis for the weather type Clouds
clouds = df[df["Weather"] == "Clouds"]
sortedClouds = clouds.sort_values("Popularity", ascending=False)
sortedClouds = sortedClouds[sortedClouds.index <=399]


def getClouds():
    print(sortedClouds.iloc[0]["Track Name"], ":", sortedClouds.iloc[0]["Artist"], ":",
          sortedClouds.iloc[0]['Popularity'])


# Data Analysis for the weather type Clear
clear = df[df["Weather"] == "Clear"]
sortedClear = clear.sort_values("Popularity", ascending=False)
sortedClear = sortedClear[sortedClear.index <=399]


def getClear():
    print(sortedClear.iloc[0]["Track Name"], ":", sortedClear.iloc[0]["Artist"], ":", sortedClear.iloc[0]['Popularity'])

def mostPop():
    sorted = df.sort_values("Popularity", ascending=False)
    print(sorted.iloc[0]["Weather"],":", sorted.iloc[0]["Track Name"], ":", sorted.iloc[0]["Artist"], ":", sorted.iloc[0]['Popularity'])

"""fog=df[df["Weather"]=="Fog"]
print(fog.shape)
f=df[df["Weather"]=="Rain"]
print(f.shape)
M=df[df["Weather"]=="Mist"]
print(M.shape)
cl=df[df["Weather"]=="Clear"]
print(cl.shape)
c=df[df["Weather"]=="Clouds"]
print(c.shape)
d=df[df["Weather"]=="Drizzle"]
print(d.shape)
t=df[df["Weather"]=="Thunderstorm"]
print(t.shape)
s=df[df["Weather"]=="Snow"]
print(s.shape)"""

def weather_music():
    Array_Sorted_Df= [sortedFog, sortedRain, sortedClear, sortedClouds, sortedThunderstorm, sortedMist, sortedDrizzle, sortedSnow]
    most=0
    c=0
    Arrayy=[]
    arrpop=[]
    for dff in Array_Sorted_Df:
       for x in iter(dff["Popularity"]):
            c += x
       y= c/399
       if (y>most):
            most=y
            Arrayy.append(dff)
    count=0
    while(0<len(Arrayy)):
        print(Arrayy[count]["Weather"])
        count+=1






# User input
print(" This is a Projected aimed to preform Data analysis on a spotify dataset relative to weather conditions\n",
      "This dataset contains the Weather type, Track Name, Artist, Album, Image, and Popularity\n")

runn = True
def switchh(userin):
    if userin == 1:
        return mostPop()
    elif userin == 2:
        userI = int(input(" Fog: 1\n Mist: 2\n Rain: 3\n Snow: 4\n Drizzle: 5\n Thunderstorm: 6\n Clouds: 7\n Clear: 8\n"))
        if userI == 1:
            getFog()
        elif (userI == 2):
            getMist()
        elif (userI == 3):
            getRain()
        elif (userI == 4):
            getSnow()
        elif (userI == 5):
            getDrizzle()
        elif (userI == 6):
            getThunder()
        elif (userI == 7):
            getClouds()
        elif (userI == 8):
            getClear()
        else:
            userI = input("Invalid Input, press 'ENTER' to try again")
    elif userin == 3:
        weather_music()
    else:
        return 0


user1 = int(input(" 1) Most Popular song\n 2) Most Popular song based on weather Conditions\n 3) Most musically engaging weather condition\n"))
temp = user1
while(temp!=0):
    switchh(temp)
    temp = int(input(" 1) Most Popular song\n 2) Most Popular song based on weather Conditions\n 3) Most musically engaging weather condition\n 0) EXIT\n"))


