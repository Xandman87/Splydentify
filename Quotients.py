# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 11:48:00 2011

@author: Xandman-mini
"""
import json
class Quotients:
# dictionary carrying quotients   
    data = {'aa' : 0.0,'ac' : 0.0,'ag' : 0.0,'at' : 0.0,
            'ta' : 0.0,'tc' : 0.0,'tg' : 0.0,'tt' : 0.0,
            'ga' : 0.0,'gc' : 0.0,'gg' : 0.0,'gt' : 0.0,
            'ca' : 0.0,'cc' : 0.0,'cg' : 0.0,'ct' : 0.0,
            'a' : 0.0,'t' : 0.0,'g' : 0.0, 'c' : 0.0}

# Makes an json-file holding relativ frequencys
    def makeJson(self,file, name):
        line = file.readline()
        while(line!= ""):
            if(line[0] != '>'):
                self.count(line)
            line = file.readline()      
        self.calcQuotients()
        self.storeJson(name)
            
 #counts occuracies of motifs            
    def count (self,line):
        if(line[0] == 'a'):
            self.data['a'] = self.data['a'] + 1.0
        elif(line[0 == 't']):
            self.data['t'] = self.data['t'] + 1.0
        elif(line[0 == 'g']):
            self.data['g'] = self.data['g'] + 1.0
        elif(line[0 == 'c']):
            self.data['c'] = self.data['c'] + 1.0
            
        self.data['aa'] = self.data['aa'] + float(line.count('aa'))
        self.data['ac'] = self.data['ac'] + float(line.count('ac'))
        self.data['ag'] = self.data['ag'] + float(line.count('ag'))
        self.data['at'] = self.data['at'] + float(line.count('at'))
        self.data['ta'] = self.data['ta'] + float(line.count('ta'))
        self.data['tc'] = self.data['tc'] + float(line.count('tc'))
        self.data['tg'] = self.data['tg'] + float(line.count('tg'))
        self.data['tt'] = self.data['tt'] + float(line.count('tt'))
        self.data['ga'] = self.data['ga'] + float(line.count('ga'))
        self.data['gc'] = self.data['gc'] + float(line.count('gc'))
        self.data['gg'] = self.data['gg'] + float(line.count('gg'))
        self.data['gt'] = self.data['gt'] + float(line.count('gt'))
        self.data['ca'] = self.data['ca'] + float(line.count('ca'))
        self.data['cc'] = self.data['cc'] + float(line.count('cc'))
        self.data['cg'] = self.data['cg'] + float(line.count('cg'))
        self.data['ct'] = self.data['ct'] + float(line.count('ct'))

#calculates relativ frequencys of motifs and stores them in dictionary        
    def calcQuotients(self):
        sumStart = 0
        sumTransition = 0
        
        for key in self.data.iterkeys():
            if(key == 'a' or key =='c'or key =='t'or key =='g'):
                sumStart = sumStart + self.data[key] 
            else:
                sumTransition = sumTransition + self.data[key] 
                
                 
        for key in self.data.iterkeys():
            if(key == 'a' or key =='c'or key =='t'or key =='g'):
                if(sumStart > 0.0):
                    self.data[key] = self.data[key]/sumStart
            else:
                 if(sumTransition > 0.0):
                     self.data[key] = self.data[key]/sumTransition
            
#generates json file            
    def storeJson(self,name):
        file = open(name,'w')
        content = json.dumps(self.data, ensure_ascii=False)
        file.write(content)
        file.close
        for key in self.data.iterkeys():
            self.data[key] = 0.0

#open training files        
pos = open('train_pos.txt', 'r')  
neg = open('train_neg.txt', 'r')       
        
quotient = Quotients()    
quotient.makeJson(pos, 'markov_pos.json') 
quotient.makeJson(neg,'markov_neg.json') 
 
        
    
            
        
            
        
        
    