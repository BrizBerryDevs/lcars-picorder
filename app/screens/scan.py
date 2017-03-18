from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsElbow, LcarsHorizSmall, LcarsTabRight, LcarsBlockSmall, LcarsBlockMedium, LcarsButton, LcarsText, LcarsTabRLarge
from ui.widgets.screen import LcarsScreen
from ui.widgets.sprite import LcarsMoveToMouse

class ScreenScan(LcarsScreen):
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

        # panel title

        all_sprites.add(LcarsText(colours.ORANGE, (0, 110), "Scan", 1.5),
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
        all_sprites.add(LcarsText(colours.WHITE, (150, 110), "LAST SCAN RESULTS:", 1.5),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (210, 110), "AMBIENT TEMP: 73.4 F"),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (235, 110), "AIR PRESSURE: 101.325 KPa"),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (260, 110), "RELATIVE HUMIDITY: 42.6 %"),
                        layer=3)
        self.info_text = all_sprites.get_sprites_from_layer(3)

        # date display
        self.stardate = LcarsText(colours.BLUE, (30, 110), "STARDATE 2711.05 17:54:32")
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # buttons        
        all_sprites.add(LcarsButton(colours.RED_BROWN, (442, 220), "LOGOUT", self.logoutHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.PURPLE, (102, 105), "BASIC SCAN", self.basicScanHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.BEIGE, (102, 212), "HIGHER SCAN", self.highScanHandler),
                        layer=4)

        # gadgets        
        self.scan_gadget= LcarsGifImage("assets/gadgets/fwscan.gif", (325, 92), 80)
        self.scan_gadget.visible = True
        all_sprites.add(self.scan_gadget, layer=2)


        #Scan screens

            #Basic Scan

        all_sprites.add(LcarsText(colours.BLUE, (145, 100), "GEO", 1.5),
                        layer=5)
        all_sprites.add(LcarsTabRLarge(colours.BLUE, 2, (143, 140)),
                        layer=5)

        all_sprites.add(LcarsText(colours.WHITE, (150, 220), "Geological Scan"),
                        layer=5)

        all_sprites.add(LcarsText(colours.BLUE, (198, 100), "MET", 1.5),
                        layer=5)
        all_sprites.add(LcarsTabRLarge(colours.BLUE, 2, (196, 150)),
                        layer=5)

        all_sprites.add(LcarsText(colours.WHITE, (225, 120), "Meteorological Scan"),
                        layer=5)

        all_sprites.add(LcarsText(colours.BLUE, (248, 100), "BIO", 1.5),
                        layer=5)
        all_sprites.add(LcarsTabRLarge(colours.BLUE, 2, (246, 150)),
                        layer=5)

        all_sprites.add(LcarsText(colours.WHITE, (275, 120), "Biological Scan"),
                        layer=5)
        
        self.basic_scan = all_sprites.get_sprites_from_layer(5)
        for sprite in self.basic_scan:
            sprite.visible = False

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

    def hideInfoText(self):
        if self.info_text[0].visible:
            for sprite in self.info_text:
                sprite.visible = False

    def showInfoText(self):
        if self.info_text[0].visible == False:
            for sprite in self.info_text:
                sprite.visible = True

    def basicScanHandler(self, item, event, clock):
        self.hideInfoText()
        for sprite in self.basic_scan:
            sprite.visible = True

    def highScanHandler(self, item, event, clock):
        self.hideInfoText()
        
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
    
    
