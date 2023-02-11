""" 
Hello. On the platform where I studied python syntax, I came across an interesting task.
For those who do not like to read a lot of text: 
The essence of the problem is to choose the right ending for the word programmer.

https://stepik.org/lesson/5047/step/6?unit=1086

At the Institute of Bioinformatics, a robot moves around the office. Recently, students from a group of programmers wrote a program for him, according to which the robot, when it enters a room, counts the number of programmers in it and says it out loud: "n programmers."

To make it sound right, for everyone
n must use the correct word ending.

Write a program that reads an integer n (non-negative) from user input, outputs this number to the console along with the correct word "programmer", so that the robot can communicate normally with people, for example: 1 programmer, 2 programmers, 5 programmers .

There can be a lot of programmers in a room. Check that your program will correctly handle all cases up to at least 1000 people.


В Институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу, согласно которой робот, заходя в комнату, считает количество в ней программистов и произносит вслух: «n программистов».

Чтобы это звучало правильно, для всех
n должен использовать правильное окончание слова.

Напишите программу, которая считывает из пользовательского ввода целое число n (неотрицательное), выводит это число в консоль вместе с правильным словом «программист», чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста , 5 программистов.

Программистов в комнате может быть много. Убедитесь, что ваша программа корректно обрабатывает все обращения не менее чем на 1000 человек.
'''
a = input()
first_formula = int(a[len(a) - 1]) 
second_formula = int(a[len(a) - 2]) 
if(first_formula == 1 and (second_formula != 1 or len(a) == 1)):
    print(a, " программист")
elif((first_formula == 2 or first_formula == 3 or first_formula == 4) and second_formula != 1):
    print(a, " программиста")
else:
    print(a, " программистов") 
