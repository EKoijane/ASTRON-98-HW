#1 Debugging

#Observe Below

#2 Practicing Sliding & Striding

#2.1 Making a List a Variable

#def descriptiveVariable(a):
#    if a>0:
#        descriptiveVariable(a-1)
#        print(a, end=',')       
#print(descriptiveVariable(20))

descriptiveVariable = []
for i in range(20):
        descriptiveVariable.append(i+1)
#print(descriptiveVariable)
"""
Encountered AttributeError: 'tuple' object has no attribute to 'append' at line 17 when I wrote:
descriptiveVariable.append(i+1)
So I replaced the () with [] on line 15 and the for statement worked
"""
#print(descriptiveVariable)

#2.2 Working with List Elements

descriptiveVariable_Squared = []
for i in descriptiveVariable:
    descriptiveVariable_Squared.append(i**2)
#print(descriptiveVariable_Squared)
"""
Encountered AttributeError: 'tuple' object has no attribute to 'append' at line 22 when I wrote:
descriptiveVariable_Squared.append(i**2)
So I replaced the () with [] on line 20 and the for statement worked
"""
#2.3 Slicing

part1 = (descriptiveVariable[0:15])
part2 = (descriptiveVariable_Squared[16:20])
FirstFifteen = part1+part2
#print(FirstFifteen)


#2.4 Striding

EveryFifth = descriptiveVariable_Squared[::5]
#print(EveryFifth)

#2.5 SLicing & Striding

#print(descriptiveVariable_Squared[0:30])
#print(descriptiveVariable_Squared[30:0:-3])
"""
Encountered IndexError: list index out of range at line 44 when I wrote:
print(descriptiveVariable_Squared[-30])
So I replaced the [-30] with [30:0:-3] on line 44 and it printed correct index in range
"""

#3 2D Lists

#3.1 Creating a 5X5 2D List

#matrix = []

#for i in range(5):
#    row = []
#    for j in range(5):
#        row.append(i * 5 + j + 1)
#    matrix.append(row)


#for row in matrix:
    #print(row)

#3.2 Replacing 2D Lists with Multiples of 3

no3matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(i * 5 + j + 1)
    no3matrix.append(row)

for i in range (5):
     for j in range(5):
          if no3matrix[i][j]%3 == 0:
               no3matrix[i][j] = '?'

for row in no3matrix:
    #print(row)

#3.3 Summing None-'?' Elements

    NewMatrix = no3matrix
    
MatrixSum = sum(item for row in NewMatrix for item in row if item != '?')
print(MatrixSum)