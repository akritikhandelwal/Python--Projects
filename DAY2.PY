# data types 

#1. strings: characters (always in double quotes)
print("hello")
#subscripting: pulling out a letter from a string 
print("hello"[0])
print("hello"[4])

#2. Integer: numbers without any decimal places 
print(123+234)

#when we have large numbers and want to visualise it through comma; 123,345,345 in python it can be written as 
print(123_345_456 + 135_567_678)
#it is interpreted as 123345456

#3. Float: numbers with decimal 
print(235.56)

#4. Boolean - two possible values - TRUE & FALSE 

num_char = len(input("What is your name?"))
#print("Your name has " + num_char + "characters")  THIS IS ERROR STATEMENT 

#but we cannot concatenate string with integers 
#TYPE FUNCTION - tells the type of datatype
print(type(num_char)) 

#CORRECT STATEMENT - CONVERTING DATATYPES 
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = float("2233.34")
print(type(a))

print(float("77") + float(33.34))

#exercise:
a = str(input("Enter your number"))
b = int(a[0]) 
c = int(a[1])
print(b+c)

#mathematical operators: + , - , * , / , **(exponent) FOLLOWS BODMAS 
print(3+3-3/3*3)

#exercise: BMI calculator 
weight = input("Enter your weight in kgs\n")
height = input("Enter your height in meters\n")
BMI = int(int(weight)/(float(height)**2))
print(BMI)

#round function 
print(round(2.666666,2))

#division / - gives floating number whereas division // - gives integer 
print(4/3)
print(type(4/3))
print(4//3)
print(type(4//3))

score = 0
score = score + 1
#shortcut for this is:
score +=1 
score -=1
score *=2
print(score)

#f string - converts multiple datatypes to string 
score = 10
height = 1.5
isWinning = True
print(f"your score is {score};your height is {height} and your winning is {isWinning}")

#exercise:
current_age = input("What is your current age?")
calc = ((90 - int(current_age))*365)//7
print("You have " + str(calc) + " weeks left")










