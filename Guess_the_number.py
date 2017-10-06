#Created by: Alireza Teimoori
#Created on: 5 Oct 2017
#Created for: ICS3UR-1
#Lesson: Unit 3-02
#This program is to learn if and else statments 
#The code shows "you won!"if the user's entry is the winning number(random)


import ui
from numpy import random
# random number to guess
number_to_guess=random.randint(1,10)
# random number generator

##print(number_to_guess)
## random number test

def check_button_touch_up_inside(sender):
    #Checks if the number user entres is the winning number or not
    
    #input
    user_number=int(view['user_number_textfield'].text)
    
    #process
    if user_number == number_to_guess:
        #output
        view['answer_lable'].text = "You won!!!"
    else:
        view['answer_lable'].text = "Sorry,your number was not the winning number.The winning number is:" +str(number_to_guess)
view = ui.load_view()
view.present('sheet')
