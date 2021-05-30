import pygame
from pygame.locals import *

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Painter")

FPS = 0

class Painter:
  def __init__(self, WIN):
    self.painted = []
    self.PAINT_LIMIT = 500 
    self.BASE_PAINT_THICKNESS = 5
    self.paint_thickness = self.BASE_PAINT_THICKNESS
    self.JOIN_LIMIT = 50
    self.paint_color = {"black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "white":(255,255,255), "purple":(128,0,128)}
    self.paint_color_used = self.paint_color["black"]
    self.WIN = WIN

  def place_circle(self):
    mouse_pos = pygame.mouse.get_pos()
    if not mouse_pos in self.painted:
      self.painted.append((mouse_pos, self.paint_color_used, self.paint_thickness))
    # if len(self.painted) == self.PAINT_LIMIT:
    #   self.painted.pop(0)

  def paint(self):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
      self.place_circle()

    for i,j,k in self.painted:
      pygame.draw.circle(self.WIN, j, i, k)
    for i in range(len(self.painted)-1):
      if ((self.painted[i][0][0] - self.painted[i+1][0][0]) ** 2 + (self.painted[i][0][1] - self.painted[i+1][0][1]) ** 2) ** 0.5 < self.JOIN_LIMIT * self.paint_thickness/self.BASE_PAINT_THICKNESS:
        pygame.draw.line(self.WIN, self.painted[i][1], self.painted[i][0], self.painted[i+1][0], self.painted[i][2])

  def color_buttons(self):

    r=25

    self.black_button.circle(r)
    self.red_button.circle(r)
    self.green_button.circle(r)
    self.blue_button.circle(r)
    self.white_button.circle(r)

    self.black_button.update()
    self.red_button.update()
    self.green_button.update()
    self.blue_button.update()
    self.white_button.update()

    self.thickness_1.circle(r)
    self.thickness_2.circle(r)
    self.thickness_3.circle(r)
    self.thickness_4.circle(r)
    self.thickness_5.circle(r)

    self.thickness_1.update()
    self.thickness_2.update()
    self.thickness_3.update()
    self.thickness_4.update()
    self.thickness_5.update()


  def draw_window(self, event):
    self.WIN.fill(self.paint_color["white"])
    self.paint()
    if event.type == pygame.MOUSEBUTTONDOWN:
      self.black_button.mouseDown = True
      self.red_button.mouseDown = True
      self.green_button.mouseDown = True
      self.blue_button.mouseDown = True
      self.white_button.mouseDown = True

      if self.black_button.hovering:
        self.paint_color_used = self.paint_color["black"]
      if self.red_button.hovering:
        self.paint_color_used = self.paint_color["red"]
      if self.green_button.hovering:
        self.paint_color_used = self.paint_color["green"]
      if self.blue_button.hovering:
        self.paint_color_used = self.paint_color["blue"]
      if self.white_button.hovering:
        self.paint_color_used = self.paint_color["white"]

      self.thickness_1.mouseDown = True
      self.thickness_2.mouseDown = True
      self.thickness_3.mouseDown = True
      self.thickness_4.mouseDown = True
      self.thickness_5.mouseDown = True

      if self.thickness_1.hovering:
        self.paint_thickness = self.BASE_PAINT_THICKNESS
      if self.thickness_2.hovering:
        self.paint_thickness = self.BASE_PAINT_THICKNESS * 2
      if self.thickness_3.hovering:
        self.paint_thickness = self.BASE_PAINT_THICKNESS * 3
      if self.thickness_4.hovering:
        self.paint_thickness = self.BASE_PAINT_THICKNESS * 4
      if self.thickness_5.hovering:
        self.paint_thickness = self.BASE_PAINT_THICKNESS * 5

    if event.type == pygame.MOUSEBUTTONUP:
      self.black_button.mouseDown = False
      self.red_button.mouseDown = False
      self.green_button.mouseDown = False
      self.blue_button.mouseDown = False
      self.white_button.mouseDown = False

      self.thickness_1.mouseDown = False
      self.thickness_2.mouseDown = False
      self.thickness_3.mouseDown = False
      self.thickness_4.mouseDown = False
      self.thickness_5.mouseDown = False

    self.color_buttons()
    pygame.display.update()

  def generate_buttons(self):

    h = 50
    w = 400
    n = 5
    r = 25
    x = (w-2*n*r)/(n+1)

    self.black_button = Button(self.WIN, "B", (x+r,h), self.paint_color["black"], self.paint_color["white"], self.paint_color["purple"], self.paint_color["green"])
    self.red_button = Button(self.WIN, "R", (2*(x+r)+r,h), self.paint_color["red"], self.paint_color["white"], self.paint_color["purple"], self.paint_color["black"])
    self.green_button = Button(self.WIN, "G", (3*(x+r)+2*r,h), self.paint_color["green"], self.paint_color["white"], self.paint_color["purple"], self.paint_color["black"])
    self.blue_button = Button(self.WIN, "B", (4*(x+r)+3*r,h), self.paint_color["blue"], self.paint_color["white"], self.paint_color["purple"], self.paint_color["black"])
    self.white_button = Button(self.WIN, "E", (5*(x+r)+4*r,h), self.paint_color["white"], self.paint_color["black"], self.paint_color["purple"], self.paint_color["green"])

    offset = WIDTH/2

    self.thickness_1 = Button(self.WIN, "1", (x+r+offset,h), self.paint_color["black"], self.paint_color["purple"], self.paint_color["white"], self.paint_color["white"])
    self.thickness_2 = Button(self.WIN, "2", (2*(x+r)+r+offset,h), self.paint_color["black"], self.paint_color["purple"], self.paint_color["white"], self.paint_color["white"])
    self.thickness_3 = Button(self.WIN, "3", (3*(x+r)+2*r+offset,h), self.paint_color["black"], self.paint_color["purple"], self.paint_color["white"], self.paint_color["white"])
    self.thickness_4 = Button(self.WIN, "4", (4*(x+r)+3*r+offset,h), self.paint_color["black"], self.paint_color["purple"], self.paint_color["white"], self.paint_color["white"])
    self.thickness_5 = Button(self.WIN, "5", (5*(x+r)+4*r+offset,h), self.paint_color["black"], self.paint_color["purple"], self.paint_color["white"], self.paint_color["white"])

  def generate_widgets(self):
    self.generate_buttons()

  def main(self):
    clock = pygame.time.Clock()
    run = True
    self.generate_widgets()
    while run:
      clock.tick(FPS)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        self.draw_window(event)

    pygame.quit()

class Button:
  def __init__(self, win, text, pos, color, highlight, press, txtColor):
    pygame.init()
    self.win = win
    self.text = text
    self.pos = pos
    self.color = color
    self.highlight = highlight
    self.press = press
    self.txtColor = txtColor
    self.button_shape = None

    self.mouseDown = False
    self.mouseUp = False

    self.font = pygame.font.SysFont("Arial", 25)

    self.colorUsed = self.color

    self.type = None

    self.hovering = False

  def circle(self, radius):
    if type(radius) is int:
      self.type = "circle"
      self.radius = radius
      self.button_shape = pygame.draw.circle(self.win, self.colorUsed, self.pos, radius)
      self.win.blit(self.font.render(self.text, True, self.txtColor), (self.pos[0]-self.font.size(self.text)[0]/2,self.pos[1]-self.font.size(self.text)[1]/2))
    else:
      raise TypeError("{} is an invalid type. Type int required.".format(type(dimensions)))

  def rectangle(self, dimensions):
    if type(dimensions) is int:
      self.type = "rectangle"
      self.dimensions = (dimensions, dimensions)
      rect = pygame.Rect(self.pos, self.dimensions)
      self.button_shape = pygame.draw.rect(self.win, self.colorUsed, rect)
      self.win.blit(self.font.render(self.text, True, self.txtColor), (self.pos[0]+dimensions, self.pos[1]+dimensions))
    elif type(dimensions) is tuple:
      self.type = "rectangle"
      self.dimensions = dimensions
      rect = pygame.Rect(self.pos, dimensions)
      self.button_shape = pygame.draw.rect(self.win, self.colorUsed, rect)
      self.win.blit(self.font.render(self.text, True, self.txtColor), (self.pos[0]+dimensions[0], self.pos[1]+dimensions[1]))
    else:
      raise TypeError("{} is an invalid type. Accepted types are int and tuple.".format(type(dimensions)))

  def highlight_button(self):
    if self.mouseDown:
      self.colorUsed = self.press
    else:
      self.colorUsed = self.highlight
    if self.type == "rectangle":
      self.rectangle(self.dimensions)
    elif self.type == "circle":
      self.circle(self.radius)

  def de_highlight_button(self):
    self.colorUsed = self.color
    if self.type == "rectangle":
      self.rectangle(self.dimensions)
    elif self.type == "circle":
      self.circle(self.radius)

  def press_highlight(self):
    self.colorUsed = self.press
    if self.type == "rectangle":
      self.rectangle(self.dimensions)
    elif self.type == "circle":
      self.circle(self.radius)

  def update(self):
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    if self.type == "rectangle":
      inX = False
      inY = False
      if mouse_pos_x < (self.pos[0] + dimensions[0]) and mouse_pos_x > self.pos[0]:
        inX = True
      if mouse_pos_y < (self.pos[1] + dimensions[1]) and mouse_pos_y > self.pos[1]:
        inY = True
      if inX and inY:
        self.hovering = True
      else:
        self.hovering = False

      if self.hovering:
        self.highlight_button()
      else:
        self.de_highlight_button()


      if self.mouseDown and self.hovering:
        self.press_highlight()


    elif self.type == "circle":
      inCircle = False
      if ((self.pos[0] - mouse_pos_x) ** 2 + (self.pos[1] - mouse_pos_y) ** 2) ** 0.5 <= self.radius:
        inCircle = True
      else:
        inCircle = False
      if inCircle:
        self.hovering = True
      else:
        self.hovering = False

      if self.hovering:
        self.highlight_button()
      else:
        self.de_highlight_button()

      if self.mouseDown and self.hovering:
        self.press_highlight()

if __name__ == "__main__":
  p = Painter(WIN)

  p.main()