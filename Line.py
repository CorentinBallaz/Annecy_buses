# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:29:35 2019

@author: Asus
"""


from Stop import Stop

class Line:
    
    
    def __init__(self,file,nbLine):
        self.file = file
        self.nbLine = nbLine
        self.scheduleAller = self.uploadData()[0]
        self.scheduleRetour = self.uploadData()[1]
        self.scheduleVacAller = self.uploadData()[2]
        self.scheduleVacRetour = self.uploadData()[3]
        
    def uploadCondensateValue(self,lines):
        i = 0
        stop = ""
        schedule = ""
        schedules = []
        while lines[i] != ' ':
            stop = stop + lines[i]
            i = i + 1
        i = i + 1
        while i < len(lines):
            if lines[i]==' ':
                schedules = schedules + [schedule]
                schedule = ''
            else:
                schedule = schedule + lines[i]
            i = i + 1
        schedules = schedules + [schedule[0:len(schedule)-1]]
#        for j in range(0,len(schedules)):
#            if (schedules[j]!='-' and schedules[j]!=''):
#                schedules[j]=time.strptime(schedules[j],'%H:%M')
        return ([stop,schedules])
        
    
    def onlyStr(self,lines):
        res = True
        for i in range(0,len(lines)):
            if (lines[i]>='0' and lines[i]<='9'):
                res = False
        return res
        
    def getScheduleAller(self):
        return self.scheduleAller
    
    def getScheduleRetour(self):
        return self.scheduleRetour
    
    def getScheduleVacAller(self):
        return self.scheduleVacAller
    
    def getScheduleVacRetour(self):
        return self.scheduleVacRetour
    
    
    def uploadData(self):
        resAller = []
        resRetour = []
        resVacAller = []
        resVacRetour = []
        f = open(self.file,'r',encoding="utf-8") 
        lines = f.readlines()
        nbline = 2
        while (lines[nbline]!='\n'):
            resAller = resAller + [self.uploadCondensateValue(lines[nbline])]
            nbline = nbline + 1
        nbline = nbline + 1
        while (lines[nbline]!='\n'):
            resRetour = resRetour + [self.uploadCondensateValue(lines[nbline])]
            nbline = nbline + 1
        nbline = nbline + 3
        while (lines[nbline]!='\n'):
            resVacAller = resVacAller + [self.uploadCondensateValue(lines[nbline])]
            nbline = nbline + 1
        nbline = nbline + 1
        while (nbline < len(lines)):
            resVacRetour = resVacRetour + [self.uploadCondensateValue(lines[nbline])]
            nbline = nbline + 1
        return [resAller,resRetour,resVacAller,resVacRetour] 
        f.close()    
        
        
        
    def listStopAller(self):
        data = self.uploadData()
        res = []
        for i in range(0,len(data[0])):
            res = res + [data[0][i][0]]
        return res 
    
    def listStopRetour(self):
        data = self.uploadData()
        res = []
        for i in range(0,len(data[1])):
            res = res + [data[1][i][0]]
        return res
    
    
    def createStop(self,tabStop):
        res = tabStop
        listNameStop = self.listStopAller() 
        #nom des stop que l'on veut rajouter
        tabNameStop = []
        #nom des stop qu'on a déjà
        if (tabStop != []):
            for i in range(0,len(tabStop)):
                tabNameStop.append(tabStop[i].name)
        for j in range(0,len(self.listStopAller())):
            if not(listNameStop[j] in tabNameStop):
                nStop = Stop(self.getScheduleAller()[j][0],self.nbLine,self.getScheduleAller()[j][1])
                res.append(nStop)
            else:
                for n in range(0,len(tabStop)):
                    if listNameStop[j]==tabStop[n].name:
                        tabStop[n].setSchedule(self.nbLine,self.getScheduleAller()[j][1])
        for k in range(0,len(listNameStop)-1):
            for l in range(0,len(res)):
                if listNameStop[k]==res[l].name:
                    for m in range(0,len(res)):
                        if listNameStop[k+1]==res[m].name:
                            res[l].addNeighbors(res[m])
        return res