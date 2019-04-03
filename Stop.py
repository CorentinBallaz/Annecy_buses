# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:34:44 2019

@author: Asus
"""

class Stop:
    """
    class that defined bus stop and buses that pass
    """
    
    def __init__(self,name,line,schedule,neighbors=[]):
        self.name = name
        self.neighbors = neighbors
        self.lines = []
        self.lines.append(line)
        self.schedule = {}
        self.schedule[line] = schedule
        
    def setSchedule(self,line,schedule):
        self.lines.append(line)
        self.schedule[line] = schedule    
        
    def addNeighbors(self,neighbors):
        self.neighbors = self.neighbors + [neighbors]
        
    def setNeighbors(self,neighbors):
        self.neighbors = [neighbors]
        
    def __repr__(self):
        return self.name
    
    
        
