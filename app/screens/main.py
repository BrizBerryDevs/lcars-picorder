from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsElbow, LcarsHorizSmall, LcarsTabRight, LcarsBlockSmall, LcarsBlockMedium, LcarsButton, LcarsText, LcarsTabRLarge
from ui.widgets.screen import LcarsScreen
from ui.widgets.sprite import LcarsMoveToMouse

class ScreenMain(LcarsScreen):
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
        
        all_sprites.add(LcarsText(colours.ORANGE, (0, 110), "System Data", 1.5),
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
        all_sprites.add(LcarsText(colours.WHITE, (180, 110), "SUMMARY:", 1.5),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (235, 110), "6 SCANS PERFORMED"),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (260, 110), "14.3 kWh USED YESTERDAY"),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (285, 110), "1.3 TQuads DATA STORED"),
                        layer=3)
        self.info_text = all_sprites.get_sprites_from_layer(3)

        # date display
        self.stardate = LcarsText(colours.BLUE, (30, 110), "STARDATE 2711.05 17:54:32")
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # buttons        

        all_sprites.add(LcarsButton(colours.PURPLE, (102, 105), "INFO", self.infoHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.BEIGE, (102, 212), "SENSORS", self.sensorsHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.BLUE, (142, 105), "GAUGES", self.gaugesHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.PEACH, (142, 212), "WEATHER", self.weatherHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.PINK, (442, 220), "LOGOUT", self.logoutHandler),
                        layer=4)

        # gadgets        
        self.scan_gadget= LcarsGifImage("assets/gadgets/fwscan.gif", (325, 92), 100)
        self.scan_gadget.visible = True
        all_sprites.add(self.scan_gadget, layer=2)
        
        self.sensor_gadget = LcarsGifImage("assets/gadgets/lcars_anim2.gif", (235, 105), 100) 
        self.sensor_gadget.visible = False
        all_sprites.add(self.sensor_gadget, layer=2)

        self.dashboard = LcarsImage("assets/gadgets/dashboard.png", (187, 105))
        self.dashboard.visible = False
        all_sprites.add(self.dashboard, layer=2) 

        self.weather = LcarsImage("assets/weather.jpg", (188, 105))
        self.weather.visible = False
        all_sprites.add(self.weather, layer=2) 

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

    def gaugesHandler(self, item, event, clock):
        self.hideInfoText()
        self.sensor_gadget.visible = False
        self.scan_gadget.visible = False
        self.dashboard.visible = True
        self.weather.visible = False

    def sensorsHandler(self, item, event, clock):
        self.hideInfoText()
        self.sensor_gadget.visible = True
        self.scan_gadget.visible = False
        self.dashboard.visible = False
        self.weather.visible = False
    
    def weatherHandler(self, item, event, clock):
        self.hideInfoText()
        self.sensor_gadget.visible = False
        self.scan_gadget.visible = False
        self.dashboard.visible = False
        self.weather.visible = True

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
    
    
