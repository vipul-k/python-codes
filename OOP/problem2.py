# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:42:58 2021

@author: Vipul Kumar
"""
import math
import webbrowser
import csv


class Coordinate:
     
    
    def __init__(self, latitude, longitude):
        '''
        The Coordinate class stores a latitude, longitude pair indicating a physical location on Earth.

        Parameters
        ----------
        latitude : Float
            Represents the latitude in radians.
        longitude : Float
            Represents the longitude in radians.


        '''
        self.latitude = latitude
        self.longitude = longitude
        
        
    def __repr__(self):
        '''
        Dunder method used to represent the instance of Coordinate class in terms of attributes latitudes and longitudes.

        Returns
        -------
        String containing the Latitude and Longitude of the Coordinate class instance.

        '''
        return("latitude : {}, longitude : {}".format(self.latitude, self.longitude))
        
    @classmethod
    def fromdegrees(cls, latitude, longitude):
        '''
        Class method that accepts two floats representing latitude and longitude in degrees and returns an instance of Coordinate.

        Parameters
        ----------

        latitude : Flaot
            Represents latitude in degrees
        longitude : Float
            Represents longitude in degrees

        Returns
        -------
        Returns instance of Coordinate class
            

        '''
        latitude = latitude*math.pi/180
        longitude = longitude*math.pi/180   
        return cls(latitude, longitude)
        
        
    def distance(self, coord):
        '''
        Method accepts another instance of Coordinate and calculates the distance in miles to it from the current instance using Haversine formula

        Parameters
        ----------
        coord : Object 
        Instance of Coordinate class

        Returns
        -------
        Float
            Distance between coord instance and current instance in miles.

        '''
        
        term1 = math.sin((coord.latitude-self.latitude)/2)**2
        term2 = math.cos(self.latitude)*math.cos(coord.latitude)*(math.sin((coord.longitude-self.longitude)/2)**2)
        return 2*3961*math.asin(math.sqrt(term1 + term2))
        
        
    def as_degrees(self):
        '''
        Return a tuple of the latitude and longitude in degrees.

        Returns
        -------
        Tuple of floats
            DESCRIPTION.
        Tuple contains the latitude and longitude of the current instance in degrees.

        '''
        return (self.latitude*180/math.pi, self.longitude*180/math.pi)
        
    def show_map(self):
        '''
        Open up Google Maps in a web browser with a point placed on the latitude/longitude of the coordinate

        '''
        webbrowser.open("http://maps.google.com/maps?q={},{}".format(self.latitude, self.longitude))
        
        
        
class School:
    def __init__(self, data):
        '''
        Each instance of School class represents a single public school in Chicago.

        Parameter
        ----------
        data : Dictionary
            A dictionary corresponding to a row of the "schools.csv" CSV file

        Attributes
        -------
        self.id : the unique ID of the school ("School ID" column) stored as an integer
        self.name : short name of the school ("Short Name" column)
        self.network : the network the school is in ("Network" column)
        self.address : the street addres of the school
        self.zip : the ZIP code of the school
        self.phone : the phone number of the school
        self.grades : a list of grades taught at the school (stored as an actual list, not just the string from the CSV file)
        self.location : the location of the school as an instance of the Coordinate class (which you
        wrote above)
        '''
        self.id = int(data["School_ID"])
        self.name = data["Short_Name"]
        self.network = data["Network"]
        self.address = data["Address"]
        self.zip = data["Zip"]
        self.phone = data["Phone"]
        self.grades = [i.strip() for i in data["Grades"].split(",")]
        self.location = Coordinate.fromdegrees(float(data["Lat"]), float(data["Long"]))
        
    def __repr__(self):
        '''
        Dunder method returns the self.location attribute of the nstance in lieu of the instance

        Returns
        -------
        self.name : Class attribute
            

        '''
        return self.name
        
    def distance(self, coord):
        '''
        Accepts an instance of the Coordinate class and return the distance in miles from the specified location to the school.

        Parameters
        ----------
        coord : Object
            Instance of coordinate class

        Returns
        -------
        Float
            Distance in miles of coord instance from school.

        '''
        #Uses the distance methods defined in Coordinate class
        return coord.distance(self.location)
        
    def full_address(self):
        '''
        Returns a multi-line string (a string that includes a newline character with the street address, city, state, and ZIP code of the school.

        Returns
        -------
        String
            Address of the school

        '''
        full_address = [self.address, "CHICAGO, IL", self.zip]
        return '\n'.join(full_address)
        
        
class CPS:
    def __init__(self, filename):
        '''
        

        Parameters
        ----------
        filename : String
            Path of the csv file

        Attributes
        -------
        self.schools : list of School instances.

        '''
        ind = 0
        self.schools = []
        with open(filename) as f:            
            for line in f:
                data_line = list(csv.reader([line.rstrip()], delimiter=','))[0]

                #codition used to read column names in the csv files as keys for dictionary
                if ind == 0:
                    keys = data_line
                else:
                    self.schools.append(School(dict(zip(keys, data_line))))
                ind+=1
            
              

        
    def nearby_schools(self, coord, radius=1.0):
        '''
        Accepts an instance of the Coordinate class and returns a list of School instances that are within radius miles of the given coordinate.

        Parameters
        ----------
        coord : Object
            Instance of Coordinate class
        radius : Float, optional
            radius in miles in which schools are to be seacrched. The default is 1.0.

        Returns
        -------
        schools_nearby : List
            List of schools in the given radius

        '''
        schools_nearby = []
        for school in self.schools:
            if school.distance(coord) < radius:
                schools_nearby.append(school)
        return schools_nearby
        
    def get_schools_by_grade(self, *grades):
        '''
        accepts one or more grades as strings ("K","3", etc.) and returns a list of School instances that teach all of the given grades.

        Parameters
        ----------
        *grades : List of grades
            Grades to be searched

        Returns
        -------
        school_g : List
            List of schools that offer the given grades

        '''
        school_g = []
        for school in self.schools:
            if grades in school.grades:
                school_g.append(school)
        return school_g
        
    def get_schools_by_network(self, network):
        '''
        Method accepts the network name as a string (like "Charter") and returns a list of School instances in that network.

        Parameters
        ----------
        network : String
            NAme of the network

        Returns
        -------
        school_ntwrk : List
            List of schools in the given network.

        '''
        school_ntwrk = []
        for school in self.schools:
            if network == school.network:
                school_ntwrk.append(school)
        return school_ntwrk
    
    
if __name__ == '__main__':
    cps = CPS("E:/Courses/Python/hw3/vipulk-master-7b17dc6bfc5df7eda158bdb1f65ce9231592cf89/homework3/schools.csv")
    print(len(cps.schools))
    print(cps.schools[:5])
    
    