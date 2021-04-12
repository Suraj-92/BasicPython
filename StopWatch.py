'''
Author: Suraj N Temkar
Date: 11/04/2021
Title: Write a Stopwatch Program for measuring the time that elapses between the start and end 
'''

import time  # Import Time Library

# User Defined Function For StopWatch    
def stopWatch():
    second = 0    
    minute = 0   
    hours = 0
    while(True):
        print("------STOPWATCH------")     
        print('=============')    
        print(f"{hours} : {minute} : {second}")
        print('=============')    
        time.sleep(1)    
        second+=1    
        if(second == 60):    
            second = 0    
            minute+=1    
        if(minute == 60):    
            minute = 0    
            hours+=1   

# Main Function
if __name__ == '__main__':
    stopWatch() 
