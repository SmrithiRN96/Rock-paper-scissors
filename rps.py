import random

def game() :
	me = 0
	comp = 0
	n = int(input("Enter the number of times you want to play : "))
	sel = ["r","p","s"]
	start(me,comp,n,sel)

def start(me,comp,n,sel) :
	print("Please choose r for rock, p for paper and s for scissors")
	for i in range(1,n+1) :
		a = input("Enter your choice : ")
		b = random.choice(sel)
		print("Computer choice is " + b)
		if(a == "r" and b == "p"):
			comp=comp+1
		elif(a == "p" and b == "r"):
			me=me+1
		elif(a == "r" and b == "s"):
			me=me+1
		elif(a == "s" and b == "r"):
			comp=comp+1
		elif(a == "s" and b == "p"):
			me=me+1
		elif(a == "p" and b == "s"):
			comp=comp+1
	if(me>comp):
		print("You won the game")
	elif(comp>me):
		print("Computer wins the game")
	else:
		print("The game is a tie")

game()

