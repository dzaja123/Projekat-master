import pygame
import time

pygame.init()


# Dimenzije prozora
WIN_DIMENSION = 700

win = pygame.display.set_mode((WIN_DIMENSION, WIN_DIMENSION))
pygame.display.set_caption("Projekat")


# Velicina table
N = 5

TARGETMOVES = N**2

# Boje
white = (255, 255, 255)
black = (0, 0, 0)
red = (180, 0, 0)

def Displej(board, final=False):
	
	win.fill(black)

	if not final:
		pygame.event.pump()

	for i in range(N):
		ydraw = i * (WIN_DIMENSION/N)
		for n in range(N):
			xdraw = n * (WIN_DIMENSION / N)
			pygame.draw.rect(win, red, (xdraw, ydraw, WIN_DIMENSION/N, WIN_DIMENSION/N), 3)
			displejTekst(board[i][n], xdraw, ydraw)
	
	while final:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				final = False
				print("Zatvara se aplikacija")

	pygame.display.update()
	
def tekst_objekti(text, font):
	textSurface = font.render(str(text), True, white)
	return textSurface, textSurface.get_rect()


def displejTekst(text, xdraw, ydraw):
	font = pygame.font.Font('freesansbold.ttf', 7 * N)
	TextSurf, TextRect = tekst_objekti(text, font)
	TextRect.center = ((xdraw + (WIN_DIMENSION / N) / 2), (ydraw + (WIN_DIMENSION / N) / 2))
	win.blit(TextSurf, TextRect)


def proveriValidnost(board, movx, movy):

	#Provera da li je moguce odigrati potez

	if (movx >= 0 and movy >= 0 and movx < N and movy < N and board[movx][movy] == " "):
		return True
	return False


def stampajTablu(board):

	#Stampanje table
    
	for i in range(len(board)):
		print(board[i])


def pozicijaKonja():
	currx = 0
	curry = 0

	
	board = [[" " for i in range(N)] for i in range(N)]

	xmoves = [-2, -2, -1, -1, 1, 1, 2, 2]
	ymoves = [1, -1, 2, -2, 2, -2, 1, -1]

	totalmoves = 1

	board[0][0] = 0
	Displej(board)

	if generisiPotez(board, currx, curry, totalmoves, xmoves, ymoves):
		stampajTablu(board)
		Displej(board, True)
	else: print("Nije moguce odigrati potez")
	

def generisiPotez(board, currx, curry, totalmoves, xmoves, ymoves):
	if totalmoves == TARGETMOVES:
		return True

	print("X osa: {}  Y osa: {}".format(currx, curry)) # Ispisivanje poteza
	
	Displej(board)		 


	for i in range(8):

		nextx = currx + xmoves[i]
		nexty = curry + ymoves[i]

		if proveriValidnost(board, nextx, nexty):
			board[nextx][nexty] = totalmoves
		

			if generisiPotez(board, nextx, nexty, totalmoves+1, xmoves, ymoves):

				return True
			# backtracking
			board[nextx][nexty] = " "

	return False


if __name__ == "__main__":
	pozicijaKonja()
	
