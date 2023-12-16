import pygame
from colour import Colour

class Board:
  def __init__(self, screen):
    self.screen = screen
    self.texts = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    self.grids = [pygame.Rect(0, 0, 200, 200), pygame.Rect(200, 0, 200, 200), pygame.Rect(400, 0, 200, 200), pygame.Rect(0, 200, 200, 200), pygame.Rect(200, 200, 200, 200), pygame.Rect(400, 200, 200, 200), pygame.Rect(0, 400, 200, 200), pygame.Rect(200, 400, 200, 200), pygame.Rect(400, 400, 200, 200)]
    self.font = pygame.font.SysFont("dejavusansmono", 150)
    self.win = None

  def draw(self):
    pygame.draw.line(self.screen, Colour.BLACK, (200, 0), (200, 600), 10)
    pygame.draw.line(self.screen, Colour.BLACK, (400, 0), (400, 600), 10)
    pygame.draw.line(self.screen, Colour.BLACK, (0, 200), (600, 200), 10)
    pygame.draw.line(self.screen, Colour.BLACK, (0, 400), (600, 400), 10)
    for index, text in enumerate(self.texts):
      if text != " ":
        if text == "X":
          text = self.font.render(text, True, Colour.RED)
        elif text == "O":
          text = self.font.render(text, True, Colour.BLUE)
        text_rect = text.get_rect()
        text_rect.center = self.grids[index].center # gets the center of the grid square
        self.screen.blit(text, text_rect)

  def update_board(self):
    for e in pygame.event.get():
      if e == pygame.MOUSEBUTTONDOWN:
        left_clicked = pygame.mouse.get_pressed()[0]
        if left_clicked:
          for index, grid in enumerate(self.grids):
            if grid.collidepoint(pygame.mouse.get_pos()):
              self.texts[index] = "X"

  def win_comb(self):
    for i in [0, 3, 6]:
      if "".join(self.texts[i: i + 3]) == "XXX":
        self.win = "X"
      elif "".join(self.texts[i: i + 3]) == "OOO":
        self.win = "O"

    cols = [[self.texts[col + i] for i in [0, 3, 6]] for col in range(3)]
    for col in cols:
      if col == ["X", "X", "X"]:
        self.win = "X"
      elif col == ["O", "O", "O"]:
        self.win = "O"

    if [self.texts[i] for i in [0, 4, 8]] == ["X", "X", "X"]:
      self.win = "X"
    elif [self.texts[i] for i in [0, 4, 8]] == ["O", "O", "O"]:
      self.win = "O"
    if [self.texts[i] for i in [2, 4, 6]] == ["X", "X", "X"]:
      self.win = "X"
    elif [self.texts[i] for i in [2, 4, 6]] == ["O", "O", "O"]:
      self.win = "O"

    #Checks if the board is full
    try:
      full = True
      for i in self.texts:
        if i == " ":
          full = False
      if full:
        if self.win == None:
          self.win = False
    except:
      pass
      
  def win_screen(self):
    if self.win == False:
      text = self.font.render("Tie", True, Colour.GREEN)
    else:
      text = self.font.render(f"{self.win} Won!", True, Colour.GREEN)
    text_rect = text.get_rect()
    text_rect.center = (300, 300)
    self.screen.blit(text, text_rect)