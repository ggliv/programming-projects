### TODO
#	'Game over' detection
#	Simulate 2048 collision a little better (values will sometimes combine multiple times)
#	Documentation

import random
class TwentyFourtyEight:
	boardWidth, boardHeight = (4, 4) # default board width and height
	board = []
	pastBoard = ""
	score = 0

	def __init__(self, w = boardWidth, h = boardHeight):
		self.boardWidth, self.boardHeight = (w, h)
		self.board = [[None for x in range(self.boardWidth)] for y in range(self.boardHeight)]
		startPosOne = self.getRandomPosition()
		startPosTwo = self.getRandomPosition()
		while startPosTwo == startPosOne:
			startPosTwo = self.getRandomPosition()
		self.board[startPosOne[0]][startPosOne[1]] = 2
		self.board[startPosTwo[0]][startPosTwo[1]] = 2

	def __str__(self):
		boardString = ""
		for x in range(self.boardHeight):
			for y in range(self.boardWidth):
				boardString += str(self.board[x][y]) + "\t"
			else:
				boardString = boardString.strip()
			# can get ugly at higher dimensions, remove the multiplication part if you want it to have only one newline. added it to make the result more readable.
			boardString += "\n" * int(self.boardHeight/2)
		return boardString.strip()

	def moveUp(self):
		self.pastBoard = str(self.board)
		for x in range(self.boardHeight):
			for y in range(self.boardWidth):
				movePosition = [x, y]
				moveValue = self.board[x][y]
				if not self.spaceIsAvailable(movePosition):
					while self.spaceIsAvailable([movePosition[0] - 1, movePosition[1]]) and movePosition[0] - 1 > -1:
						movePosition[0] -= 1
					else:
						if movePosition[0] - 1 > -1 and moveValue == self.board[movePosition[0] - 1][movePosition[1]]:
							moveValue += moveValue
							self.score += moveValue
							movePosition[0] -= 1
					self.moveElement([x, y], movePosition, moveValue)

	def moveDown(self):
		self.pastBoard = str(self.board)
		for x in range(self.boardHeight - 1, -1, -1):
			for y in range(self.boardWidth):
				movePosition = [x, y]
				moveValue = self.board[x][y]
				if not self.spaceIsAvailable(movePosition):
					while self.spaceIsAvailable([movePosition[0] + 1, movePosition[1]]) and movePosition[0] + 1 < self.boardHeight:
						movePosition[0] += 1
					else:
						if movePosition[0] + 1 < self.boardHeight and moveValue == self.board[movePosition[0] + 1][movePosition[1]]:
							moveValue += moveValue
							self.score += moveValue
							movePosition[0] += 1
					self.moveElement([x, y], movePosition, moveValue)

	def moveLeft(self):
		self.pastBoard = str(self.board)
		for x in range(self.boardHeight):
			for y in range(self.boardWidth):
				movePosition = [x, y]
				moveValue = self.board[x][y]
				if not self.spaceIsAvailable(movePosition):
					while self.spaceIsAvailable([movePosition[0], movePosition[1] - 1]) and movePosition[1] - 1 > -1:
						movePosition[1] -= 1
					else:
						if movePosition[1] - 1 > -1 and moveValue == self.board[movePosition[0]][movePosition[1] - 1]:
							moveValue += moveValue
							self.score += moveValue
							movePosition[1] -= 1
					self.moveElement([x, y], movePosition, moveValue)

	def moveRight(self):
		self.pastBoard = str(self.board)
		for x in range(self.boardHeight):
			for y in range(self.boardWidth - 1, -1, -1):
				movePosition = [x, y]
				moveValue = self.board[x][y]
				if not self.spaceIsAvailable(movePosition):
					while self.spaceIsAvailable([movePosition[0], movePosition[1] + 1]) and movePosition[1] + 1 < self.boardWidth:
						movePosition[1] += 1
					else:
						if movePosition[1] + 1 < self.boardWidth and moveValue == self.board[movePosition[0]][movePosition[1] + 1]:
							moveValue += moveValue
							self.score += moveValue
							movePosition[1] += 1
					self.moveElement([x, y], movePosition, moveValue)

	def moveElement(self, fromPosition, toPosition, newValue):
		self.board[toPosition[0]][toPosition[1]] = newValue
		if fromPosition == toPosition: return
		self.board[fromPosition[0]][fromPosition[1]] = None

	def spawnNewValue(self):
		if None not in sum(self.board, []):
			return
		rand = self.getRandomPosition()
		while not self.spaceIsAvailable(rand):
			rand = self.getRandomPosition()
		self.board[rand[0]][rand[1]] = self.getNewValue()

	def getNewValue(self):
		boardMaxPower = 0
		boardMax = max([x if x != None else 0 for x in sum(self.board, [])])
		if boardMax == 2: return 2
		while boardMax != 1:
			boardMax >>= 1
			boardMaxPower += 1
		possiblePowers = [x + 1 for x in range(boardMaxPower)]
		powersWeights = [1/(x+1) for x in range(boardMaxPower + 1)]
		selectedPower = random.choices(possiblePowers, powersWeights[1:])
		return 2 ** selectedPower[0]

	def getRandomPosition(self):
		return [random.randint(0, self.boardHeight - 1), random.randint(0, self.boardWidth - 1)]

	# reports incorrectly when dealing with negative indices but all of the movement methods account for that
	def spaceIsAvailable(self, position):
		try:
			return True if self.board[position[0]][position[1]] == None else False
		except IndexError:
			return False
	
	def lastMoveWasImpactful(self):
		if str(self.board) == self.pastBoard: return False
		return True

	def checkGameOver(self):
		#if None in sum(self.board, []): return False
		return False