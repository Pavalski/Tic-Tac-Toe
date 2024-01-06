import pygame
pygame.init()

from colour import Colour
from board import Board
import time

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(Colour.WHITE)

FPS = 60

board = Board(screen)

curr_player = 1

def main():
  global curr_player
  clock = pygame.time.Clock()
  while True:
    clock.tick(FPS)
    screen.fill(Colour.WHITE)
    board.draw()
    if board.win != None:
      board.win_screen()
      pygame.display.update()
      time.sleep(3) # A buffer to show the player how they lost
      pygame.quit()
      quit()
    else:
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          left_clicked = pygame.mouse.get_pressed()[0]
          if left_clicked:
            for index, grid in enumerate(board.grids):
              if grid.collidepoint(pygame.mouse.get_pos()):
                if board.texts[index] == " ":
                  if curr_player == 1:
                    board.texts[index] = "X"
                    curr_player = 2
                  else:
                    board.texts[index] = "O"
                    curr_player = 1
      board.win_comb()
      pygame.display.update()

main()