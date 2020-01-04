# Dice roll
import random
print("The program returns a number from dice roll\n")
input("Press ENTER to roll a dice\n")
liczba = random.randint(1,5)
repSetList = ["1/6","2/5","3/3","5/2","6/1"]
if liczba == 1:
	print("Dice roll returtend ", repSetList[0])
if liczba == 2:
	print("Dice roll returtend ", repSetList[1])
if liczba == 3:
	print("Dice roll returtend ", repSetList[2])
if liczba == 4:
	print("Dice roll returtend ", repSetList[3])
if liczba == 5:
	print("Dice roll returtend ", repSetList[4])
