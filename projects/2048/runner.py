### TODO
#	Make a curses interface? What's there now is pretty ugly and annoying to interact with.

import os
from TwentyFourtyEight import TwentyFourtyEight as TFE

game = TFE()

def clearShell():
	if os.name == "posix": os.system("clear")
	if os.name == "nt": os.system("cls")

while True:
	clearShell()
	print(game)
	print()
	print("Score: " + str(game.score))
	userinput = input("[U]p, [d]own, [l]eft, or [r]ight?: ").lower()
	if userinput == "quit" or game.checkGameOver(): break
	elif userinput == "u": game.moveUp()
	elif userinput == "d": game.moveDown()
	elif userinput == "l": game.moveLeft()
	elif userinput == "r": game.moveRight()
	else: continue
	if game.lastMoveWasImpactful(): game.spawnNewValue()