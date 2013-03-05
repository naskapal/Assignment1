'''
Created on Mar 5, 2013

@author: Rizky
'''
import random
def main():
    score = 0
    repeat = eval(input("How many problems would you like?\t"))
    for i in range (repeat):
        num1=random.randint(10,99)
        num2=random.randint(10,99)
        if num1<num2:
            num1,num2 = num2,num1
        print("Question",str(i+1),":\t What is",num1,"-",num2,"?\t")
        answer = eval(input(""))
        if answer == num1-num2:
            print("Correct!")
            score = score+1
        else:
            print("No,",num1,"-",num2,"is",num1-num2)
    print("Your score is",(score/repeat)*100,"%")
    
main()