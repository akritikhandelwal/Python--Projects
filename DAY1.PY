#Understanding Print command
print("Hello World")

#print modifiers- what if we have 2 double quotes inside paranthesis; then we will use this method:
print('she said: "hello" and left')
#or 
print("she said: \"hello\" and left")

#string manipulation 
#instead of writing print multiple times we use:
print("Hello World\nHello\nPython")

#string concatenation 
print("Hello" + " " + "World")

#input function
#example 1
input("what is your name?")
print(input("what is your name?"))
print("Hello" + " " + input("what is your name?"))

#example 2
a = int(input("Enter the number"))
b = int(input("Enter the number"))
print(a+b)

#finding out the length of the string
a = len(input("Enter your name"))
print(a)

#variables: "a" , "b" used above are nothing but variables; they make our tasks easier
a = "Basic"
b = "Assembly"
c = ("a:" + a + " b:" + b)
print(c)


