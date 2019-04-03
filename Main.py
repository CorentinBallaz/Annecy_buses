# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:49:53 2019

@author: Asus
"""

from Line import Line


file1 = r"1_Poisy-ParcDesGlaisins.txt"
file2 = r"2_Piscine-Patinoire_Campus.txt"

line1 = Line(file1,1)
line2 = Line(file2,2)

tabStop = line1.createStop([])
tabStop = line2.createStop(tabStop)
tabStop[0].setNeighbors(tabStop[2])                       

def shortest(depart,arrivee,passage={},compteur=0):

    if (depart.name in passage):
        if passage[depart.name] > compteur:
            passage[depart.name] = compteur
    else:        
        passage[depart.name] = compteur      
    compteur = compteur + 1      
    if (depart==arrivee or compteur>21):
        return passage    
    else:
        for i in range(0,len(depart.neighbors)):
            passage=shortest(depart.neighbors[i],arrivee,passage,compteur)
        return passage
    


def foremost(depart,arrivee,hour,passage={},compteur=0): 
    j = 0
    bestTime = convertTimeToInt(depart.schedule[depart.lines[0]][j])
    while (bestTime < hour and j<len(depart.schedule[depart.lines[0]])):
        j = j + 1
        bestTime = convertTimeToInt(depart.schedule[depart.lines[0]][j])
    if len(depart.lines)>1: 
        for k in range(1,len(depart.lines)):
            l = 0
            thistime = convertTimeToInt(depart.schedule[depart.lines[k]][l])
            while (thistime < hour and l<len(depart.schedule[depart.lines[k]])):
                l = l + 1
                thistime = convertTimeToInt(depart.schedule[depart.lines[k]][l])
            if thistime < bestTime:
                bestTime = thistime       
    
    compteur = compteur + (bestTime-hour)
          
    if (depart.name in passage):
        if passage[depart.name] > compteur:
            passage[depart.name] = compteur
    else:
        passage[depart.name] = compteur

    if (depart==arrivee or compteur>24*60):
        return passage    
    else:
        for i in range(0,len(depart.neighbors)):
            passage=foremost(depart.neighbors[i],arrivee,bestTime,passage,compteur)
        return passage
    


def onlyStr(line):
        res = True
        for i in range(0,len(line)):
            if (line[i]>='0' and line[i]<='9'):
                res = False
        return res    

def convertTimeToInt(strTime):
    if not(onlyStr(strTime)):
        if len(strTime)==4:
            res = int(strTime[0])*60 + int(strTime[2]+strTime[3])
        elif len(strTime)==5:
            res = int(strTime[0]+strTime[1])*60 + int(strTime[3]+strTime[4])
    else:
        return False
    return res

def convertIntToTime(intTime):
    h = intTime//60
    m = intTime%60
    return (str(h)+':'+str(m))
        
    
hour = convertTimeToInt('14:29')


print(foremost(tabStop[4],tabStop[10],hour))
#print(tabStop[8].schedule[1][22])
#print(tabStop[9].schedule[1][22])
#print(tabStop[9].schedule[2][21])
#print(convertTimeToInt(tabStop[5].schedule[1][23])-convertTimeToInt(tabStop[1].schedule[1][23]))

print()
print(shortest(tabStop[4],tabStop[10]))
#print(tabStop[0].neighbors)   

    
            
            