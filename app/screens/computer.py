from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsElbow, LcarsHorizSmall, LcarsTabRight, LcarsBlockSmall, LcarsBlockMedium, LcarsButton, LcarsText, LcarsTabRLarge
from ui.widgets.screen import LcarsScreen
from ui.widgets.sprite import LcarsMoveToMouse

class ScreenComputer(LcarsScreen):
    def setup(self, all_sprites):
        
        all_sprites.add(LcarsBackgroundImage("assets/lcars_screen_main.png"),
                        layer=0)

        #top elbow
        all_sprites.add(LcarsElbow(colours.BLUE, 0, (-1, 5)),
                        layer=1)
        all_sprites.add(LcarsHorizSmall(colours.BLUE, (54, 189)),
                        layer=1)
        all_sprites.add(LcarsHorizSmall(colours.GREY_BLUE, (54, 223)),
                        layer=1)
        all_sprites.add(LcarsHorizSmall(colours.GREY_BLUE, (54, 257)),
                        layer=1)
        all_sprites.add(LcarsTabRight(colours.PURPLE, (54, 291)),
                        layer=1)
        
        # panel title
        
        all_sprites.add(LcarsText(colours.ORANGE, (0, 110), "Access Computer", 1.5),
                        layer=1)

        #lower elbow
        all_sprites.add(LcarsElbow(colours.RED_BROWN, 1, (75, 5)),
                        layer=1)
        all_sprites.add(LcarsHorizSmall(colours.RED_BROWN, (76, 189)),
                        layer=1)
        all_sprites.add(LcarsHorizSmall(colours.PEACH, (76, 223)),
                        layer=1)
        all_sprites.add(LcarsHorizSmall(colours.PEACH, (76, 257)),
                        layer=1)
        all_sprites.add(LcarsTabRight(colours.ORANGE, (76, 291)),
                        layer=1)

        # left panel blocks
        all_sprites.add(LcarsBlockSmall(colours.RED_BROWN, (149, 6), "SCAN", self.scanHandler),
                        layer=1)
        all_sprites.add(LcarsBlockSmall(colours.ORANGE, (186, 6), "LOGS", self.logsHandler),
                        layer=1)
        all_sprites.add(LcarsBlockSmall(colours.PEACH, (223, 6), "COMPUTER", self.computerHandler),
                        layer=1)
        all_sprites.add(LcarsBlockMedium(colours.PEACH, (260, 6), "P4"),
                        layer=1)
        all_sprites.add(LcarsBlockMedium(colours.PURPLE, (325, 6), "COMMS", self.commsHandler),
                        layer=1)
        all_sprites.add(LcarsBlockMedium(colours.BLUE, (390, 6), "SYSTEM", self.systemHandler),
                        layer=1)
        all_sprites.add(LcarsBlockMedium(colours.BLUE, (455, 6), ""),
                        layer=1)

        # info text
        all_sprites.add(LcarsText(colours.WHITE, (140, 110), "LAST SEARCH:", 1.5),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (195, 110), "Stardate 1603.17 15:36:24"),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (220, 110), "PARAMETERS:"),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (245, 110), "WARP ENGINE, ANTIMATTER CONTAINMENT"),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (285, 110), "DILITHIUM MATRIX, MAINTENANCE"),
                        layer=3)
        self.info_text = all_sprites.get_sprites_from_layer(3)

        # date display
        self.stardate = LcarsText(colours.BLUE, (30, 110), "STARDATE 2711.05 17:54:32")
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # buttons        

        all_sprites.add(LcarsButton(colours.PURPLE, (102, 105), "TEXT", self.infoHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.BEIGE, (102, 212), "VOICE", self.sensorsHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.PINK, (442, 220), "LOGOUT", self.logoutHandler),
                        layer=4) 

        #all_sprites.add(LcarsMoveToMouse(colours.WHITE), layer=1)
        self.beep1 = Sound("assets/audio/panel/201.wav")
        Sound("assets/audio/panel/220.wav").play()

    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 1000:
            self.stardate.setText("STARDATE {}".format(datetime.now().strftime("%d%m.%y %H:%M:%S")))
            self.lastClockUpdate = pygame.time.get_ticks()
        LcarsScreen.update(self, screenSurface, fpsClock)
        
    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            return False

    def infoHandler(self, item, event, clock):
        if self.info_text[0].visible == False:
            for sprite in self.info_text:
                sprite.visible = True
        self.sensor_gadget.visible = False
        self.scan_gadget.visible = True
        self.dashboard.visible = False
        self.weather.visible = False

    def scanHandler(self, item, event, clock):
        from screens.scan import ScreenScan
        self.loadScreen(ScreenScan())

    def logsHandler (self, item, event, clock):
        from screens.logs import ScreenLogs
        self.loadScreen(ScreenLogs())

    def computerHandler (self, item, event, clock):
        from screens.computer import ScreenComputer
        self.loadScreen(ScreenComputer())

    def systemHandler(self, item, event, clock):
        from screens.main import ScreenMain
        self.loadScreen(ScreenMain())

    def commsHandler(self, item, event, clock):
        from screens.comms import ScreenComms
        self.loadScreen(ScreenComms())
    
    def logoutHandler(self, item, event, clock):
        from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenAuthorize())
    
    
