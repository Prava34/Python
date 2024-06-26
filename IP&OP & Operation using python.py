#BASICS OF PYTHON-INPU AND OUTPUT AND OPERATION HACKERANK PROBLEMS#
#1)Write a program to print "Hello, World!"
'''print("\"Hello, World!\"")'''

#2)Write a program to print Hello World with tab
'''print("Hello World\tHello World")'''

#3)Write a program to print the given sample output.
'''print("Hello World\nHello World")'''

#4)Write a program to print the details of a student. The student's details consist of his/her name, age, CGPA, and grade.
'''import math
name=input()
age=int(input())
CGPA=float(input())
grade=input()
print("Name:",name)
print("Age:",age)
print("CGPA:",math.floor(CGPA*100)/100)
print("Grade:",grade)'''

#5)Write a program to get a character as an input and print its ASCII value.
'''c=input()
print(ord(c))'''

#6)Write a program to get a number (ASCII value) as input and print its equivalent character.
'''a=int(input())
print(chr(a))'''

#7)Write a program to get a float value from the user and display it in the below-mentioned format.
#HINT: Use ceil() and floor() functions from the header file.
'''import math
n=float(input())
print(int(n))
print(math.ceil(n))
print(math.floor(n))'''

#8)write a program to print area and perimeter of a rectangle
'''l=int(input())
b=int(input())
perimeter=l*b
area=2*(l+b)
print("The required length is",area,"m")
print("The required area of carpet is",perimeter,"sqm")'''

#9)write a program to compute the profit if a, b, and c are given?
'''a=int(input())
b=int(input())
c=int(input())
d=(a*b)-(a*c)
print(d-100)'''

#10)write a program written as follows "I will be always four" “I can only be opened when you add my first and last digit and enter it” and “If you find a sign, you should not consider it”
#help Snape break the code and open the door so that they can save the Sorcerer's tomb. 
'''n=int(input())
n=abs(n)
f=n//1000
l=n%10
print(f+l)'''

#11)write a program to print spiliting the team
'''n=int(input())
m=int(input())
o=n//m
p=n%m
print("The number of friends in each team is",o,"and left out is",p)'''

#12)write a program to print interest,amount and discount
'''x=int(input())
y=int(input())
r=int(input())
interest=float((x*y*r)/100)
amount=float(x+interest)
discount=float(interest*(2/100))
final=float(amount-discount)
print("{:.2f}".format(interest))
print("{:.2f}".format(amount))
print("{:.2f}".format(discount))
print("{:.2f}".format(final))'''

#13)write a program to print distance formula
'''x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
d1=float((x1+x2)/2)
d2=float((y1+y2)/2)
print("Arun's house is located at({:.1f},{:.1f})".format(d1,d2))'''

#14)write a program to print the operation dollars and cents
'''k=int(input())
i=int(input())
o=int(input())
p=int(input())
tc=i+p
td=k+o+(tc//100)
rd=tc%100
print(td)
print(rd)'''

#15)write a program to print the tresaure hunter
'''total=int(input())
ben=int(input())
blackbread=int(input())
ben_share=(total*ben)//100
left=total-ben_share
blackbread=(left*blackbread)//100
remaining=total-(ben_share+blackbread)
priates=remaining//3
print(ben_share)
print(blackbread)
print(priates)'''

#16)write a program to print reverse of 3 digit
'''n=int(input())
first=n//100
n=n%100
second=n//10
n=n%10
third=n//1
n=n%1
rev=third*100+second*10+first
print(rev)'''

#17)write a program to print tic tac toe
'''x=int(input())
row=(x-1)//3
column=(x-1)%3
print(row,column)'''
