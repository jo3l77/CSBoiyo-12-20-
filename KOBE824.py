# set up the variables (rate, initial_balance, target_balance)


#initial variables,constants


#INITIAL_BALANCE = 800


#TARGET = INITIAL_BALANCE*3


#RATE: 3.0

'''
INITIAL_BALANCE = 800
TARGET = INITIAL_BALANCE*3
RATE = 3.0
balance = INITIAL_BALANCE
year = 0
while balance<TARGET:
    year = year+1
    interest = balance*RATE/100
    balance = balance + interest

 print("The investment tripled after", year, "years.")
 '''

import turtle

for i in range(1,300):
    turtle.forward(270)
    turtle.left(94) 
    turtle.speed(10)
    turtle.pencolor(100)
    
