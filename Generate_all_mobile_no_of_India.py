#!/usr/bin/python3
#Ref=https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India
__author__ = "Dr. Kamlesh K. Sahu"
__version__ = "v 0.1"


circle = ""
operator = ""
circle_table = []
circle_table2 = []
operator_table = []
operator_table2 = []

print("----------------------------------------------")
print("Select circle")

#circle_code
circle_code = open("code_circle_number")
for circle_line in circle_code:
    circle_column = circle_line.rstrip("\n").split("\t")
    print("\t",circle_column[0], "for" , circle_column[2])

circle_choice = int(input("Enter Circle number "))

circle_code = open("code_circle_number")
for circle_line in circle_code:
    circle_column = circle_line.rstrip("\n").split("\t")
    circle_table = (circle_column[0],circle_column[1],circle_column[2])
    circle_table2.append(circle_table)

for x in circle_table2:
    if int(x[0]) == circle_choice:
        circle = x[1]

#operator_code
operator_code = open("code_operator_number")
for operator_line in operator_code:
    operator_column = operator_line.rstrip("\n").split("\t")
    print("\t",operator_column[0], "for" , operator_column[2])

operator_choice = int(input("Enter operator number "))

operator_code = open("code_operator_number")
for operator_line in operator_code:
    operator_column = operator_line.rstrip("\n").split("\t")
    operator_table = (operator_column[0],operator_column[1],operator_column[2])
    operator_table2.append(operator_table)

for x in operator_table2:
    if int(x[0]) == operator_choice:
        operator = x[1]

numfile = open("mobile_no_" + circle + "_" + operator + ".txt", "w")

mob_op_circle = open("mobile_operator_circle")
for line in mob_op_circle:
    column = line.rstrip("\n").split("\t")
    if column[2] == circle and column[1] == operator:
        num = int(column[0].rstrip())
        num1 = num * 1000000
        num2 = num1 + 1000000
        while num1 < num2:
            #print(num1)
            numfile.write(str(num1))
            numfile.write("\n")
            num1 += 1

numfile.close()

print("----------------------------------------------")
print("Script ends here")