##############################################################################################
### Dingen op het scherm

#om dingen op het scherm te kunnen zetten
import lvgl as lv
import lvgl_esp32
from fri3d.badge.display import display
wrapper = lvgl_esp32.Wrapper(display)
wrapper.init()

#om de tijd op het scherm te kunnen zetten
import time

#de file lv_colors.py moet in dezelfde folder staan als deze file
from . import lv_colors as col

#zelfgemaakte letters; de file lijn_letters moet in dezelfde fodler staan als deze file
from . import lijn_letters

class Scherm:
    
     #badge is een horloge?
    klok_tick = time.ticks_ms() #onthouden wanneer de tijd voor het laatst is getoond
    
    def __init__(self):
        ################################################################################
        # Met lvgl kan je ook meerdere 'schermen' maken, en die afwisselen op de display van de badge
        self.scherm_1 = self.maak_scherm_1()
        lv.screen_load(self.scherm_1)

        self.scherm_2 = lv.obj(0)
        self.achtergrond(kleur = lv.PALETTE.GREEN, rand = lv.PALETTE.PURPLE, screen = self.scherm_2)
        self.schrijf_fried(self.scherm_2)
        #lv.screen_load(self.scherm_2) deze nu nog niet laden
        
        self.scherm_klok = self.maak_klok()
    
    def maak_klok(self):
        self.scherm_klok = lv.obj(0)
        screen = self.scherm_klok
        #self.achtergrond(kleur =lv.PALETTE.PURPLE, rand = lv.PALETTE.YELLOW, screen = self.scherm_klok)
        self.achtergrond(kleur = 0xffffff, rand = lv.PALETTE.YELLOW, screen = self.scherm_klok)
        tijd = time.gmtime()
        uur = tijd[3]
        
        minuut = tijd[4]
        seconde = tijd[5]
        toon_tijd = f"{uur:02}" + ":" + f"{minuut:02}" 
       # self.maak_label(de_tekst = toon_tijd, kleur = col.lv_colors.SILVER, screen = self.scherm_klok)
        
        letter_style = lijn_letters.geef_letter_style(kleur = col.lv_colors.YELLOW, lijn_dikte = 9)
        
        #Nu de letters, beetje schuiven tot ze goed staan
        offset_y = -30
        lijn_letters.schrijf_letter(toon_tijd[0],-100, 0 + offset_y, letter_style, screen)
        lijn_letters.schrijf_letter(toon_tijd[1],-40, 0 + offset_y, letter_style, screen)
        lijn_letters.schrijf_letter(".", -5, 10 + offset_y, letter_style, screen)
        lijn_letters.schrijf_letter(".", -5, 50 + offset_y, letter_style, screen)
        lijn_letters.schrijf_letter(toon_tijd[3],40, 0 + offset_y, letter_style, screen)
        lijn_letters.schrijf_letter(toon_tijd[4],100, 0 + offset_y, letter_style, screen)
        self.klok_tick = time.ticks_ms()
        return self.scherm_klok
    
    def maak_scherm_1(self):
        self.scherm_1 = lv.obj(0) #de 0 betekent dat dit object geen parent heeft, en dus een scherm is (waar je weer andere dingen in stopt)
        self.achtergrond(kleur = lv.PALETTE.YELLOW, rand = lv.PALETTE.PURPLE, screen = self.scherm_1)
        self.mijn_naam_lijn(kleur = col.lv_colors.PURPLE, screen = self.scherm_1)
        
#         tijd = time.gmtime()
#         uur = tijd[3]
#         minuut = tijd[4]
#         toon_tijd = str(uur) + ":" + str(minuut) 
#         self.maak_label(de_tekst = toon_tijd, screen = self.scherm_1)
        return self.scherm_1 
    
        #de volgende functie zet een tekst op het scherm, in een label
    #er zitten geen grote lettertypes ingebakken, dus deze tekst is heel klein
    def maak_label(self, de_tekst = "Pink",kleur = col.lv_colors.PURPLE, screen = None ):
        if screen is None: screen = lv.screen_active()
        
        label = lv.label(screen)
        label.set_text(de_tekst)
        label.set_style_text_color(kleur, lv.PART.MAIN)
        label.align(lv.ALIGN.CENTER, 0, -80) # lv.ALIGN.TOP_MID, 0, 0 kan ook, dan staat hij tegen de bovenrand van het scherm

    
    #functie die het hele scherm vult
    def achtergrond(self, kleur = lv.PALETTE.YELLOW, rand = lv.PALETTE.PURPLE, screen = None ):
        if screen is None: screen = lv.screen_active()
        style = lv.style_t()
        style.init()

        # Een achtergrondkleur instellen, en de afronding voor de hoeken
        style.set_radius(60) #volg netjes de afronding van het schermpje
        style.set_bg_opa(lv.OPA.COVER)
        style.set_bg_color(lv.palette_lighten(kleur, 1))

        # Een gekleurde rand rondom
        style.set_border_color(lv.palette_main(rand))
        style.set_border_width(15)
        #style.set_border_opa(lv.OPA._50) #opacity: rand beetje doorzichtig
        style.set_border_side(lv.BORDER_SIDE.BOTTOM | lv.BORDER_SIDE.RIGHT | lv.BORDER_SIDE.LEFT | lv.BORDER_SIDE.TOP)

        # Een object maken. Een afgeronde rechthoek, in dit geval
        obj = lv.obj(screen)
        obj.add_style(style, 0)
        obj.set_size(300,240) #Met 300,240 is het scherm precies gevuld
        obj.center()

        ####### Einde van de functie definitie

    #Deze functie tekent mijn naam (Pink) met een paarse lijn op het scherm
    #Pas de line_points aan om een andere naam (of figuur) te maken
    #Je kan natuurlijk ook de lijn_letters uitbreiden, maar ik vind het wel mooi als 'ink' met 1 lijn is
    def mijn_naam_lijn(self, kleur = col.lv_colors.PURPLE, screen = None ):
        if screen is None: screen = lv.screen_active()
        # Een stijl maken om de lijn mee te tekenen
        style_line = lv.style_t()
        style_line.init()
        style_line.set_line_width(10) # 10 is lekker dik
        style_line.set_line_color(kleur)
        style_line.set_line_rounded(True)
        
        # De coördinaten van de punten voor de letter P
        line_points_p = lijn_letters.geef_letter_punten("P")
        
        # Een lijn maken met de punten en de lijnstijl
        line1 = lv.line(screen)
        line1.set_points(line_points_p, len(line_points_p))      #de punten in de lijn stoppen
        line1.add_style(style_line,0)
        line1.align(lv.ALIGN.CENTER, -70, 0) # deze moet een beetje links van het midden komen
        
        # De coördinaten van de punten voor de letters ink (zonder stip)
        line_points_ink = [ 
                            {"x":80, "y":120},
                            {"x":80, "y":60},
                            {"x":80, "y":120},
                            {"x":100, "y":120},
                            {"x":100, "y":120},
                            {"x":100, "y":60},
                            {"x":100, "y":70},
                            {"x":140, "y":60},
                            {"x":140, "y":120},
                            {"x":160, "y":120},
                            {"x":160, "y":10},
                            {"x":160, "y":80},
                            {"x":200, "y":60},
                            {"x":160, "y":80},
                            {"x":200, "y":120},
                            ]
        # Nog een lijn maken met de nieuwe punten en de lijnstijl die we al hadden
        line2 = lv.line(screen)
        line2.set_points(line_points_ink, len(line_points_ink))      #de punten in de lijn stoppen
        line2.add_style(style_line,0)
        line2.align(lv.ALIGN.CENTER, 0, 0)
        
        # Nu nog een puntje op de i
        line_points_puntje = [ 
                            {"x":0, "y":0},
                            {"x":0, "y":5}
                            ]
       
        line3 = lv.line(screen)
        line3.set_points(line_points_puntje, len(line_points_puntje))      # Set the points
        line3.add_style(style_line,0)
        line3.align(lv.ALIGN.CENTER, -20, -20)    
        ####### Einde van de functie definitie


    def schrijf_fried(self, screen = None):
        if screen is None: screen = lv.screen_active()
        
        #Maak letters, allemaal met dezelfde lijnstijl
        letter_style = lijn_letters.geef_letter_style(kleur = col.lv_colors.PURPLE, lijn_dikte = 9)

        #Nu de letters, beetje schuiven tot ze goed staan
        lijn_letters.schrijf_letter("F",-80, 0, letter_style, screen)
        lijn_letters.schrijf_letter("r",-30, 0, letter_style, screen)
        lijn_letters.schrijf_letter("i", 5, 0, letter_style, screen)
        lijn_letters.schrijf_letter("dot_i",5, -20, letter_style, screen)
        lijn_letters.schrijf_letter("3",35, 0, letter_style, screen)
        lijn_letters.schrijf_letter("d",85, 0, letter_style, screen)

    

    #deze functie wisselt het scherm. wordt automatisch aangeroepen vanuit de main loop, en ook met knopje X
    def ander_scherm(self):
        actief = lv.screen_active()
        if actief is self.scherm_1:
            lv.screen_load(self.scherm_2)
        elif actief is self.scherm_2:
            self.scherm_klok = self.maak_klok()
            lv.screen_load(self.scherm_klok)
        elif actief is self.scherm_klok:
            self.scherm_1 = self.maak_scherm_1()
            lv.screen_load(self.scherm_1)

   
    #lvgl heeft regelmatig een schop nodig om goed te werken
    
    def schop(self):
        
        actief = lv.screen_active()
        if actief is self.scherm_klok:
            tick_nu = time.ticks_ms()
            if (tick_nu - self.klok_tick) > 10000:
                self.scherm_klok = self.maak_klok()
                lv.screen_load(self.scherm_klok)
        
        lv.timer_handler_run_in_period(5) #dit is nodig om de naam op het scherm te zien

scherm = Scherm()
