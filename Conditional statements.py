leap=1990
if leap % 4 == 0:
    print('Its a leap year')
else:
    print("1990 is not a multiple of 4 hence it's not a leap year")

print(1990%4)


#Fizz Buzz
a=int(input())
if (a % 3 ==0 and a % 5==0):
     print("FIZZBUZZ")
elif (a % 3)==0:
     print("FIZZ")
elif (a % 5)==0:     
     print("BUZZ")
elif (a % 3 !=0 and a % 5 !=0) and (a % 3) != 0 and (a % 5) != 0:
    print("Invalid number")


#program marks
mark=int(input())
if (mark >0 and mark <=100) and (mark >50) and (mark >=90 and mark <100):
    print("VALID MARK(BETWEEN 0 TO 100)")
    print("PASS MARK")
    print("GRADE A")
elif (mark >0 and mark <=100) and (mark >50) and (mark >=80 and mark <90):
    print("VALID MARK(BETWEEN 0 TO 100)")
    print("PASS MARK")
    print("GRADE B")
elif (mark >0 and mark <=100) and (mark >50) and (mark >=70 and mark <80):   
    print("VALID MARK(BETWEEN 0 TO 100)")
    print("PASS MARK")
    print("GRADE C")
elif (mark >0 and mark <=100) and (mark >50) and (mark >=60 and mark <70):   
    print("VALID MARK(BETWEEN 0 TO 100)")
    print("PASS MARK")   
    print("GRADE D")
elif (mark >0 and mark <=100) and (mark >50) and (mark >=50 and mark <60):   
    print("VALID MARK(BETWEEN 0 TO 100)")
    print("PASS MARK")    
    print("GRADE E")
elif (mark <=0):
    print("INVALID MARK(BETWEEN 0 TO 100)")
    





