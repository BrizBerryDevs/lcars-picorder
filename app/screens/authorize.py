import pygame
from pygame.mixer import Sound

from ui import colours
from ui.widgets.background import LcarsBackgroundImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import *
from ui.widgets.screen import LcarsScreen

class ScreenAuthorize(LcarsScreen):

    def setup(self, all_sprites):
        all_sprites.add(LcarsBackgroundImage("assets/lcars_screen_main.png"),
                        layer=0)

        #top bar
        all_sprites.add(LcarsTabLeft(colours.BLUE, (10, 10), 1),
                        layer=0)
        all_sprites.add(LcarsText(colours.ORANGE, (7, 33), "LCARS ONLINE"),
                        layer=0)
        all_sprites.add(LcarsHorizLong(colours.GREY_BLUE, (10, 114)),
                        layer=0)
        all_sprites.add(LcarsHorizLong(colours.GREY_BLUE, (10, 166)),
                        layer=0)
        all_sprites.add(LcarsTabRight(colours.ORANGE, (10, 289), 1),
                        layer=0)

        #United Federation of Planets Logo
        all_sprites.add(LcarsLogo(colours.ORANGE, (40, 77)),
                        layer=0)

        # bottom bar
        all_sprites.add(LcarsTabLeft(colours.ORANGE, (457, 10), 1),
                        layer=0)
        all_sprites.add(LcarsHorizLong(colours.GREY_BLUE, (457, 33)),
                        layer=0)
        all_sprites.add(LcarsHorizLong(colours.GREY_BLUE, (457, 100)),
                        layer=0)
        all_sprites.add(LcarsHorizLong(colours.GREY_BLUE, (457, 166)),
                        layer=0)
        all_sprites.add(LcarsTabRight(colours.ORANGE, (457, 289), 1),
                        layer=0)
        
        

        all_sprites.add(LcarsText(colours.BLACK, (454, -1), "PiCorder v0.1"), 
                        layer=0)        

        all_sprites.add(LcarsText(colours.ORANGE, (190, -1), "AUTHORIZATION REQUIRED", 2),
                        layer=0)

        all_sprites.add(LcarsText(colours.BLUE, (270, -1), "ONLY AUTHORIZED PERSONNEL", 1.5),
                        layer=1)
        all_sprites.add(LcarsText(colours.BLUE, (300, -1), "MAY ACCESS THIS TERMINAL", 1.5),
                        layer=1)

        all_sprites.add(LcarsText(colours.BLUE, (380, -1), "TOUCH TERMINAL TO PROCEED", 1),
                        layer=1)
        
        #all_sprites.add(LcarsText(colours.BLUE, (390, -1), "FAILED ATTEMPTS WILL BE REPORTED", 1.5),layer=1)


        all_sprites.add(LcarsButton(colours.GREY_BLUE, (245, 11), "1", self.num_1), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (245, 111), "2", self.num_2), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (245, 211), "3", self.num_3), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (285, 11), "4", self.num_4), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (285, 111), "5", self.num_5), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (285, 211), "6", self.num_6), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (325, 11), "7", self.num_7), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (325, 111), "8", self.num_8), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (325, 211), "9", self.num_9), layer=2)
        all_sprites.add(LcarsButton(colours.GREY_BLUE, (365, 111), "0", self.num_0), layer=2)
        all_sprites.add(LcarsText(colours.WHITE, (410, -1), "ENTER PIN FOR ACCESS", 1.5),
                        layer=2)

        self.layer1 = all_sprites.get_sprites_from_layer(1)
        self.layer2 = all_sprites.get_sprites_from_layer(2)

        # sounds
        Sound("assets/audio/panel/215.wav").play()
        self.sound_granted = Sound("assets/audio/accessing.wav")
        self.sound_beep1 = Sound("assets/audio/panel/201.wav")
        self.sound_denied = Sound("assets/audio/access_denied.wav")
        self.sound_deny1 = Sound("assets/audio/deny_1.wav")
        self.sound_deny2 = Sound("assets/audio/deny_2.wav")

        ############
        # SET PIN CODE WITH THIS VARIABLE
        ############
        self.pin = 3141
        ############
        self.reset()

    def reset(self):
        # Variables for PIN code verification
        self.correct = 0
        self.pin_i = 0
        self.granted = False
        for sprite in self.layer1: sprite.visible = True
        for sprite in self.layer2: sprite.visible = False

    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Play sound
            self.sound_beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            if (not self.layer2[0].visible):
                for sprite in self.layer1: sprite.visible = False
                for sprite in self.layer2: sprite.visible = True
                Sound("assets/audio/enter_authorization_code.wav").play()
            elif (self.pin_i == len(str(self.pin))):
                # Ran out of button presses
                if (self.correct == 4):
                    self.sound_granted.play()
                    from screens.main import ScreenMain
                    self.loadScreen(ScreenMain())
                else:
                    self.sound_deny2.play()
                    self.sound_denied.play()
                    self.reset()

        return False

    def num_1(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '1':
            self.correct += 1

        self.pin_i += 1

    def num_2(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '2':
            self.correct += 1

        self.pin_i += 1

    def num_3(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '3':
            self.correct += 1

        self.pin_i += 1

    def num_4(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '4':
            self.correct += 1

        self.pin_i += 1

    def num_5(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '5':
            self.correct += 1

        self.pin_i += 1

    def num_6(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '6':
            self.correct += 1

        self.pin_i += 1

    def num_7(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '7':
            self.correct += 1

        self.pin_i += 1

    def num_8(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '8':
            self.correct += 1

        self.pin_i += 1

    def num_9(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '9':
            self.correct += 1

        self.pin_i += 1

    def num_0(self, item, event, clock):
        if str(self.pin)[self.pin_i] == '0':
            self.correct += 1

        self.pin_i += 1
    
        
