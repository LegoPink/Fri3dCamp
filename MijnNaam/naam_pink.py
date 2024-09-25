print("Deze code gebruikt lvgl. Na het runnen moet je een hardreset (knopje rechts naast schermpje) doen op je badge")
print("Dat is nodig omdat anders het scherm het een tweede keer niet doet")

#Dit programma doet een paar dingen:
# -- zet het scherm in een mooie kleur met rand,
# -- zet mijn naam erop in een mooie kleur
# -- zet de ledjes op de badge in mooi kleuren
# -- zet de ledjes in een andere kleur als je op A drukt
# -- start de badge op in het gewone menu als je op Start+Menu drukt

#Ik heb alles in 1 file gezet en in het Nederlands geschreven, zodat het hopelijk ook door (jonge) beginners gebruikt kan worden
#Je kan https://fri3dcamp.github.io/viper/ gebruiken om deze file (of de inhoud) op je badge te zetten en te runnen
#Je kan ook 

#eerst importeren wat we nodig hebben
#voor de ledjes
from fri3d.badge.leds import leds
from fri3d.badge.hardware import hardware_leds
from neopixel import NeoPixel
from machine import Pin

#om dingen op het scherm te kunnen zetten
import lvgl as lv
import lvgl_esp32
from fri3d.badge.display import display
wrapper = lvgl_esp32.Wrapper(display)
wrapper.init()

#om te kunnen reageren op de knopjes (A, B, X, Y etc) op de badge
import time
from fri3d.badge.buttons import buttons

#from lv_colors import lv_colors
#de code hieronder kan je ook in een bestand lv_colors.py stoppen en dan from lv_colors import lv_colors doen
#(Het staat hier zodat je alleen deze file hoeft te hebben)
##########################################lv_colors.py############################################################
def LV_COLOR_MAKE(r,g,b):
    return lv.color_make(r,g,b)

class lv_colors:
    WHITE=LV_COLOR_MAKE(0xFF, 0xFF, 0xFF)
    SILVER=LV_COLOR_MAKE(0xC0, 0xC0, 0xC0)
    GRAY=LV_COLOR_MAKE(0x80, 0x80, 0x80)
    BLACK=LV_COLOR_MAKE(0x00, 0x00, 0x00)
    RED=LV_COLOR_MAKE(0xFF, 0x00, 0x00)
    MAROON=LV_COLOR_MAKE(0x80, 0x00, 0x00)
    YELLOW=LV_COLOR_MAKE(0xFF, 0xFF, 0x00)
    OLIVE=LV_COLOR_MAKE(0x80, 0x80, 0x00)
    LIME=LV_COLOR_MAKE(0x00, 0xFF, 0x00)
    GREEN=LV_COLOR_MAKE(0x00, 0x80, 0x00)
    CYAN=LV_COLOR_MAKE(0x00, 0xFF, 0xFF)
    AQUA=CYAN
    TEAL=LV_COLOR_MAKE(0x00, 0x80, 0x80)
    BLUE=LV_COLOR_MAKE(0x00, 0x00, 0xFF)
    NAVY=LV_COLOR_MAKE(0x00, 0x00, 0x80)
    MAGENTA=LV_COLOR_MAKE(0xFF, 0x00, 0xFF)
    PURPLE=LV_COLOR_MAKE(0x80, 0x00, 0x80)
    ORANGE=LV_COLOR_MAKE(0xFF, 0xA5, 0x00)
############################################einde lv_colors.py##########################################################

#Het volgende stukje code zet de 5 ledjes op de badge aan
neopixel_aantal = 5
pixels =NeoPixel(Pin(hardware_leds.pinout.pin),neopixel_aantal)

def set_leds(color = (100,100,100)):
    for pixel_id in range(len(pixels)):
        pixels[pixel_id] = color
    pixels.write()
    ####### Einde van de functie definitie

#zet de ledjes op je lievelingskleur, roep de functie aan!
# gebruik bijvoorbeeld https://colorpicker.me/ om de RGB waarde van je lievelingskleur te vinden 
set_leds((105, 6, 105)) #RGB (Rood, Groen, Blauw) maximaal 255

##############################################################################################
### Dingen op het scherm

#functie die het hele scherm vult
def achtergrond(kleur = lv.PALETTE.YELLOW, rand = lv.PALETTE.PURPLE ):
    style = lv.style_t()
    style.init()

    # Set a background color and a radius
    style.set_radius(60)
    style.set_bg_opa(lv.OPA.COVER)
    style.set_bg_color(lv.palette_lighten(kleur, 1))

    # Add border to the bottom+right
    style.set_border_color(lv.palette_main(rand))
    style.set_border_width(15)
    #style.set_border_opa(lv.OPA._50)
    style.set_border_side(lv.BORDER_SIDE.BOTTOM | lv.BORDER_SIDE.RIGHT | lv.BORDER_SIDE.LEFT | lv.BORDER_SIDE.TOP)

    # Create an object with the new style
    obj = lv.obj(lv.screen_active())
    obj.add_style(style, 0)
    obj.set_size(300,240)
    obj.center()
    
    ####### Einde van de functie definitie
    
achtergrond() #functie moet natuurlijk ook aangeroepen worden...

#Deze functie tekent mijn naam (Pink) met een paarse lijn op het scherm
#Pas de line_points aan om een andere naam (of figuur) te maken
def mijn_naam_lijn(kleur = lv_colors.PURPLE):
    # Create an array for the points of the line
    line_points = [ {"x":5, "y":5}, 
                {"x":5, "y":120}, 
                {"x":5, "y":60}, 
                {"x":60, "y":60}, 
                {"x":5, "y":5}, 
                {"x":5, "y":120},
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

    # Create new style (thick dark blue)
    style_line = lv.style_t()
    style_line.init()
    style_line.set_line_width(10)
    style_line.set_line_color(kleur)
    style_line.set_line_rounded(True)

    # Copy the previous line and apply the new style
    line1 = lv.line(lv.screen_active())
    line1.set_points(line_points, len(line_points))      # Set the points
    line1.add_style(style_line,0)
    line1.align(lv.ALIGN.CENTER, 0, 0)
    ####### Einde van de functie definitie

mijn_naam_lijn() #functie moet natuurlijk ook aangeroepen worden... 

#de volgende functie zet mijn naam op het scherm, in een label
#er zitten geen grote lettertypes ingebakken, dus deze tekst is heel klein
def mijn_naam_label(de_naam = "Pink",kleur = lv_colors.PURPLE):
    screen = lv.screen_active()
    label = lv.label(screen)
    label.set_text(de_naam)
    #label.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN)
    label.set_style_text_color(kleur, lv.PART.MAIN)
    label.align(lv.ALIGN.CENTER, 0, -80)

#mijn_naam_label("Jouw naam") #Gebruik deze functie ipv mijn_naam_lijn() als je SNEL je eigen naam (klein) op het scherm wil

################################################################################
# alles onder "while True:" wordt steeds herhaald
# de code kijkt of je knopjes indrukt en reageert daar op

#knopje A verandert de kleur van de LED-jes, hij gebruik de kleuren uit een lijstje
#lijstje kleuren. stop er jouw lievelingskleuren in! (het mogen er meer of minder zijn)
lijstje_kleuren = [(39, 187, 214),(105, 6, 105),  (240, 211, 22),(23, 22, 240),(244, 165, 13)]
welke_kleur = 0

while True:
    lv.timer_handler_run_in_period(5) #dit is nodig om de naam op het scherm te zien
    
    #als Start en Menu beide ingedrukt zijn, reboot dan de badge naar het gewone menu
    # (OTA, Hello, MicroPython, Retro-Go Gaming)
    if buttons.start.value() != 0 and buttons.menu.value() != 0:
        from fri3d import boot
        boot.main_menu()
    
    #kies een andere kleur uit het lijstje als Knop A ingedrukt is
    if buttons.a.value() != 0: 
        set_leds(lijstje_kleuren[welke_kleur])
        #schuif de kleur op.
        # % is 'modulo' oftewel de 'rest' als je gaat delen (in de geval door het aantal kleuren)
        # door de volgende regel is 'welke_kleur' een juiste waarde om mee in het lijstje_kleuren te prikken
        welke_kleur = (welke_kleur + 1) % len(lijstje_kleuren)
        #en nu heel even niks, want het knopje is natuurlijk niet meteen losgelaten
        #ms = milliseconden. 1000 ms = 1 seconde
        time.sleep_ms(200)
        #als je het knopje ingedrukt blijf houden, blijven de ledjes van kleur veranderen!
        
