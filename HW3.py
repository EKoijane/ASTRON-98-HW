#1 Oski Stole Your Power

#x = 5
#y = 2
#c = y
#for i in range(x):
#    y = y*c
    
#print(y)
    
#2 What Should I Wear

#Weather = [62, 69, 64, 73, 63, 71, 70]
#x = min(Weather)
#y = max(Weather)
#print(x,y)

#3 Check If It's The Weekend

#def isWeekend(x):
#    if ((x>5) and (x<=7)):
#        return True
#    else:
#        return False
#print(isWeekend(6))

#4 Fuel Efficiency Calculator

#distance = 100
#fuel = 5
#fuel_efficiency = (distance/fuel)
#print(fuel_efficiency)

#5 Secret Code

#n = (0,6,7,9,8)
#print(n[4],n[0],n[1],n[2],n[3])
#print(type(n)) #tuple

#6 Min and Max but for Loops

#6.1 For Loops

#Min

#table = [2024, 98, 131, 2, 3, 72]
#minimum = table[0]
#for i in range(1, 6):
#    if(table[i-1]<table[i]):
#        if(table[i-1]<=minimum):
#           minimum = table[i-1]
#    else:
#       minimum = table[i]
#print(minimum)

#Max

#table = [2024, 98, 131, 2, 3, 72]
#maximum = table[0]
#for i in range(1, 6):
#    if(table[i-1]>table[i]):
#        if(table[i-1]>=maximum):
#           maximum = table[i-1]
#    else:
#     if(table[i-1]>=maximum):
#           maximum = table[i-1]
#print(maximum)

#6.2 While Loops

#Min

#table = [2024, 98, 131, 2, 3, 72]
#minimum = table[0]
#i = 1
#while i < 6:
#    if(table[i-1]<table[i]):
#        if(table[i-1]<=minimum):
#           minimum = table[i-1]
#    else:
#       minimum = table[i]
#    i = i+1
#print(minimum)

#Max

#table = [2024, 98, 131, 2, 3, 72]
#maximum = table[0]
#i = 1
#while i < 6:
#    if(table[i-1]>table[i]):
#        if(table[i-1]>=maximum):
#           maximum = table[i-1]
#    else:
#     if(table[i-1]>=maximum):
#           maximum = table[i-1]
#    i = i+1
#print(maximum)

#7 Counting Vowels

#text = "Go, Bears"
#vowels = ["a", "e", "i", "o", "u"]
#count=0
#for i in text:
#    for j in range(len(vowels)):
#        if i==vowels[j]:
#            count = count + 1   
#print(count)

#8 Calculate Digital Root

#set = (2468)
#def add(num):
#    count = 0
#    n = str(num)
#    for i in n:
#        count = count + int(i)
#    """
#    >>> sum(5830) == 16
#    >>> sum(1234) == 10
#    """
#    return count
#print(add(set))