# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 21:44:27 2021

@author: hp
"""
# import urllib.request

# weburl = urllib.request.urlopen('http://maps.google.com/maps?q=25.31668,83.01041')
# print ("result code" + str(weburl.getcode()))

import webbrowser
import re
import csv
import math

#webbrowser.open("http://maps.google.com/maps?q={},{}".format(25.31668,83.01041))

# webbrowser.open("http://maps.google.com/maps?q={},{}".format(25.31668,83.01041))

# f'{self.first}.{self.last}@cs.uchicago.edu'

class Coordinate:
     
    
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        
        
    def __repr__(self):
        return("latitude : {}, longitude : {}".format(self.latitude, self.longitude))
        
    @classmethod
    def fromdegrees(cls, latitude, longitude):
        latitude = latitude*math.pi/180
        longitude = longitude*math.pi/180   
        return cls(latitude, longitude)
class School:
    def __init__(self, data):
        self.id = int(data["School_ID"])
        self.name = data["Short_Name"]
        self.network = data["Network"]
        self.address = data["Address"]
        self.zip = data["Zip"]
        self.phone = data["Phone"]
        self.grades = data["Grades"].split(",")
        self.location = Coordinate.fromdegrees(float(data["Lat"]), float(data["Long"]))
        
        def __repr__(self):
            return self.name

with open("E:/Courses/Python/hw3/vipulk-master-7b17dc6bfc5df7eda158bdb1f65ce9231592cf89/homework3/schools.csv") as f:
    data = []
    ind= 0
    schools = []
    for line in f:
        #data_line = re.split(r',(?=")', line.rstrip())
        data_line = list(csv.reader([line.rstrip()], delimiter=','))[0]
        
        if ind == 0:
            keys = data_line
        else:
            #print(dict(zip(keys, data_line)))
            data.append(dict(zip(keys, data_line)))
            schools.append(School(dict(zip(keys, data_line))))
            
        ind+=1
        
print(len(data))
print(len(schools))

        
        
# # print(data[1])
# grades = ["K", "1"]
# if *grades in ["K", "1", "2", "3"]:
#     print(True)
# else:
#     print(False)


# import math
# class Coordinate:
     
    
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
        
        
#     def __repr__(self):
#         return("latitude : {}, longitude : {}".format(self.latitude, self.longitude))
        
#     @classmethod
#     def fromdegrees(cls, latitude, longitude):
#         latitude = latitude*math.pi/180
#         longitude = longitude*math.pi/180   
#         return cls(latitude, longitude)
        
# p = Coordinate(25, 85)

# p1 = Coordinate.fromdegrees(25,85)

# print(p)
# print(p1)


 
    

