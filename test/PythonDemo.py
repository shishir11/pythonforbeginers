'''
Created on Dec 27, 2018

@author: shishir.sarkar
'''

class MyClass(object):
   
    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        print('is this a right structure')
  
    
    def displayCount(self):
        print('is this function is correct..')    
        
        myclass = MyClass('','')
        myclass.displayCount()
        print('is this printing..')