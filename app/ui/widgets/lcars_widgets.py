import pygame
from pygame.font import Font
from pygame.locals import *
from pygame.mixer import Sound

from ui.widgets.sprite import LcarsWidget
from ui import colours

class LcarsLogo(LcarsWidget):
    """ The LCARS UFP logo (165x138) - implemented in PiCorder v0.1"""

    def __init__(self, pos, size, handler=None):
        image = pygame.image.load("assets/lcars_ufp_logo.png").convert()

        self.image = image
        LcarsWidget.__init__(self, pos, size, handler)


class LcarsElbow(LcarsWidget):
    """The LCARS corner elbow (183x72) - implemented in PiCorder v0.1"""
    
    STYLE_BOTTOM_LEFT = 0
    STYLE_TOP_LEFT = 1
    STYLE_BOTTOM_RIGHT = 2
    STYLE_TOP_RIGHT = 3
    
    def __init__(self, colour, style, pos, handler=None):
        image = pygame.image.load("assets/elbow.png").convert()
        if (style == LcarsElbow.STYLE_BOTTOM_LEFT):
            image = pygame.transform.flip(image, False, True)
        elif (style == LcarsElbow.STYLE_BOTTOM_RIGHT):
            image = pygame.transform.rotate(image, 180)
        elif (style == LcarsElbow.STYLE_TOP_RIGHT):
            image = pygame.transform.flip(image, True, False)
        
        self.image = image
        size = (image.get_rect().width, image.get_rect().height)
        LcarsWidget.__init__(self, colour, pos, size, handler)
        self.applyColour(colour)

class LcarsHorizSmall(LcarsWidget):
    """ The LCARS Horizontal bar (32x16) - implemented in PiCorder v0.1"""

    def __init__(self, colour, pos, handler=None):
        image = pygame.image.load("assets/horiz_1.png").convert()

        self.image = image
        LcarsWidget.__init__(self, colour, pos, handler)
        self.applyColour(colour)

class LcarsHorizMed(LcarsWidget):
    """ The LCARS Horizontal bar (81x16) - implemented in PiCorder v0.1"""

    def __init__(self, colour, pos, handler=None):
        image = pygame.image.load("assets/horiz_2.png").convert()

        self.image = image
        LcarsWidget.__init__(self, colour, pos, handler)
        self.applyColour(colour)

class LcarsHorizLong(LcarsWidget):
    """ The LCARS Horizontal bar (121x16) - implemented in PiCorder v0.1"""

    def __init__(self, colour, pos, handler=None):
        image = pygame.image.load("assets/horiz_3.png").convert()

        self.image = image
        LcarsWidget.__init__(self, colour, pos, handler)
        self.applyColour(colour)

class LcarsTabLeft(LcarsWidget):
    """Left-hand Tab widget (like radio button) (21x16) - implemented in PiCorder v0.1"""

    def __init__(self, colour, pos, handler = None, rectSize = None):
        if rectSize == None:
            image = pygame.image.load("assets/tab.png").convert()
            size = (image.get_rect().width, image.get_rect().height)
        else:
            size = rectSize
            image = pygame.Surface(rectSize).convert()
            image.fill(colour)

        self.image = image
        LcarsWidget.__init__(self, colour, pos, handler, size)
        self.applyColour(colour)

class LcarsTabRight(LcarsWidget):
    """Right-hand Tab widget (like radio button) (21x16) - implemented in Picorder v0.1"""
    
    def __init__(self, colour, pos, handler = None, rectSize = None):
        if rectSize == None:
            image = pygame.image.load("assets/tab1.png").convert()
            size = (image.get_rect().width, image.get_rect().height)
        else:
            size = rectSize
            image = pygame.Surface(rectSize).convert()
            image.fill(colour)

        self.image = image
        LcarsWidget.__init__(self, colour, pos, handler, size)
        self.applyColour(colour)

class LcarsTabRLarge(LcarsWidget):
    """Right-hand Tab widget (45x34) - implemented in Picorder v0.1"""
    
    def __init__(self, colour, size, pos, handler = None, rectSize = None):
        if rectSize == None:
            image = pygame.image.load("assets/tab4.png").convert()
            size = (image.get_rect().width, image.get_rect().height)
        else:
            size = rectSize
            image = pygame.Surface(rectSize).convert()
            image.fill(colour)

        self.image = image
        LcarsWidget.__init__(self, colour, pos, handler, size)
        self.applyColour(colour)

class LcarsButton(LcarsWidget):
    """Button - either rounded or rectangular if rectSize is spcified"""

    def __init__(self, colour, pos, text, handler=None, rectSize=None):
        if rectSize == None:
            image = pygame.image.load("assets/button.png").convert()
            size = (image.get_rect().width, image.get_rect().height)
        else:
            size = rectSize
            image = pygame.Surface(rectSize).convert()
            image.fill(colour)

        self.colour = colour
        self.image = image
        font = Font("assets/swiss911.ttf", 19)
        textImage = font.render(text, False, colours.BLACK)
        image.blit(textImage, 
                (image.get_rect().width - textImage.get_rect().width - 10,
                    image.get_rect().height - textImage.get_rect().height - 5))
    
        LcarsWidget.__init__(self, colour, pos, size, handler)
        self.applyColour(colour)
        self.highlighted = False
        self.beep = Sound("assets/audio/panel/202.wav")

    def handleEvent(self, event, clock):
        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)):
            self.applyColour(colours.WHITE)
            self.highlighted = True
            self.beep.play()

        if (event.type == MOUSEBUTTONUP and self.highlighted):
            self.applyColour(self.colour)
           
        return LcarsWidget.handleEvent(self, event, clock)
        
class LcarsText(LcarsWidget):
    """Text that can be placed anywhere"""

    def __init__(self, colour, pos, message, size=1.0, background=None, handler=None):
        self.colour = colour
        self.background = background
        self.font = Font("assets/swiss911.ttf", int(19.0 * size))
        
        self.renderText(message)
        # center the text if needed 
        if (pos[1] < 0):
            pos = (pos[0], 160 - self.image.get_rect().width / 2)
            
        LcarsWidget.__init__(self, colour, pos, None, handler)

    def renderText(self, message):        
        if (self.background == None):
            self.image = self.font.render(message, True, self.colour)
        else:
            self.image = self.font.render(message, True, self.colour, self.background)
        
    def setText(self, newText):
        self.renderText(newText)

class LcarsBlockLarge(LcarsButton):
    """Left navigation block - large version"""

    def __init__(self, colour, pos, text, handler=None):
        size = (81, 147)
        LcarsButton.__init__(self, colour, pos, text, handler, size)

class LcarsBlockMedium(LcarsButton):
   """Left navigation block - medium version"""

   def __init__(self, colour, pos, text, handler=None):
        size = (81, 62)
        LcarsButton.__init__(self, colour, pos, text, handler, size)

class LcarsBlockSmall(LcarsButton):
   """Left navigation block - small version"""

   def __init__(self, colour, pos, text, handler=None):
        size = (81, 34)
        LcarsButton.__init__(self, colour, pos, text, handler, size)

    
