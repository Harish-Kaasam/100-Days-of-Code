'''
Day - 2- Understanding data types and string manipulation

String - subscripting (string is a group of characters enclosed in ""/'', or it can be defined as characters which we dont want program to run)
The subscript operator is defined as square brackets [] . It is used to access the elements of string, list tuple, and so on.

H E L L O - string
0 1 2 3 4 - (n-1) index 

#Integers 

123456 == 123_456
#float
#Boolean

type(parameters) #type checking 
str(parameter) # we can use to type conversion to convert any datatype to string 
similarly 

int(), float()

Mathematical operator --> +,-,**,*,/

PEMDAS 
()
**
*
/
+
-
// - flowdivision (if you dont want decimal place in division)

round(expression, decimal_places)
#print(round(8/3 , 2)

F- strings --> “formatted string literals,”
we cna even call methods directly 
f"your string is {variable}, your height{float}"



'''


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("welcome to the tip calculator")

bill = float(input("what was your total bill? "))
ptip = input("what percentage tip would like to give? ")
split = input("how many people to split the bill? ")

percentage = int(ptip) / 100


total_roundoff =  round((bill + (bill * percentage ) )/ int(split), 2)


print(f"each person should pay {total_roundoff}")