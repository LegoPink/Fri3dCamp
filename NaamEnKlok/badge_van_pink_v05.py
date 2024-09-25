print("Deze code gebruikt lvgl. Na het runnen moet je een hardreset (knopje rechts naast schermpje) doen op je badge")
print("Dat is nodig omdat anders het scherm het een tweede keer niet doet")

#Dit programma doet een paar dingen:
# -- zet het scherm in een mooie kleur met rand,
# -- zet mijn naam erop in een mooie kleur
# -- zet de ledjes op de badge in mooi kleuren
# -- zet de ledjes in een andere kleur als je op A drukt
# -- speelt een muziekje als je op knop B drukt
# -- start de badge op in het gewone menu als je op Start+Menu drukt
# -- laat een ander scherm met mooie rand en Fri3d zien als je op X druk

#Om dit programma te laten werken moet je ook wat andere bestanden op je badge zetten, gezellig naast dexe file.
# Dat is nodig omdat sommige functies daarin staan, zodat deze file wat korter blijft.
# lv_colors.py
# fs_driver.py
# op_het_scherm.py
# lijn_letters.py

#Je kan https://fri3dcamp.github.io/viper/ (gebruik Chrome of Chromium, niet Firefox!) gebruiken om deze file (of de inhoud) op je badge te zetten en te runnen
#Je kan ook Thonny gebruiken (Thonny is gratis).

#eerst importeren wat we nodig hebben
#voor de ledjes
from fri3d.badge.leds import leds
from fri3d.badge.hardware import hardware_leds
from neopixel import NeoPixel
from machine import Pin

from user.pink.libs.op_het_scherm import scherm


#om te kunnen reageren op de knopjes (A, B, X, Y etc) op de badge
import time
from fri3d.badge.buttons import buttons

# voor de muziekjes (Ring Tone Text Transfer Language) 
from fri3d.rtttl import songs, RTTTL

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

################################################################################
def speel_muziekje():
    never =  "Never Gonna Give You Up:d=4,o=5,b=200:8g,8a,8c6,8a,e6,8p,e6,8p,d6.,p,8p,8g,8a,8c6,8a,d6,8p,d6,8p,c6,8b,a.,8g,8a,8c6,8a,2c6,d6,b,a,g.,8p,g,2d6,2c6.,p,8g,8a,8c6,8a,e6,8p,e6,8p,d6.,p,8p,8g,8a,8c6,8a,2g6,b,c6.,8b,a,8g,8a,8c6,8a,2c6,d6,b,a,g.,8p,g,2d6,2c6."
    RTTTL(never).play(volume=100)

################################################################################
# alles onder "while True:" wordt steeds herhaald
# dat is de 'main loop'
# de code kijkt of je knopjes indrukt en reageert daar op

#knopje A verandert de kleur van de LED-jes, hij gebruik de kleuren uit een lijstje
#lijstje kleuren. stop er jouw lievelingskleuren in! (het mogen er meer of minder zijn)
lijstje_kleuren = [(10,10,10),(0,0,0),(39, 187, 214),(105, 6, 105),  (240, 211, 22),(23, 22, 240),(244, 165, 13)]
welke_kleur = 0

#wat huishuidelijke zaken om het scherm automatisch te kunnen wisselen
vorige_tick = time.ticks_ms() #onthouden wanneer het eerste scherm er stond
wacht_tijd = 1000

#badge is een horloge?
klok_tick = time.ticks_ms() #onthouden wanneer de tijd voor het laatst is getoond

#########################################################################
## Main loop ############################################################
#########################################################################
while True:
    scherm.schop()
      
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
    
    #kies een andere kleur uit het lijstje als Knop B ingedrukt is (andere kant rond)
    if buttons.b.value() != 0: 
        set_leds(lijstje_kleuren[welke_kleur])
        #schuif de kleur op.
        # % is 'modulo' oftewel de 'rest' als je gaat delen (in de geval door het aantal kleuren)
        # door de volgende regel is 'welke_kleur' een juiste waarde om mee in het lijstje_kleuren te prikken
        welke_kleur = (welke_kleur - 1)
        if welke_kleur < 0: welke_kleur = len(lijstje_kleuren) -1
        #en nu heel even niks, want het knopje is natuurlijk niet meteen losgelaten
        #ms = milliseconden. 1000 ms = 1 seconde
        time.sleep_ms(200)
        #als je het knopje ingedrukt blijf houden, blijven de ledjes van kleur veranderen!
    if buttons.y.value() != 0:
        speel_muziekje()
    
    if buttons.x.value() != 0:
        scherm.ander_scherm()
        time.sleep_ms(200)
        
#     #ga gewoon zo nu en dan van scherm wisselen
#     tick_nu = time.ticks_ms() #hoe 'laat' is het nu?
#     if (tick_nu - vorige_tick) > wacht_tijd: #als er meer tijd zit tussen nu en vorige keer: nieuw scherm!
#         scherm.ander_scherm()
#         vorige_tick = tick_nu #en dan de huidige 'tijd' bewaren als vorig
#     
#     if (tick_nu - klok_tick) > 60000:
#         # tijd opvragen
#         tijd = time.gmtime()
#         uur = tijd[3]
#         minuut = tijd[4]
#         toon_tijd = str(uur) + ":" + str(minuut) 
#         print(toon_tijd)
#         klok_tick = tick_nu #en dan de huidige 'tijd' bewaren als vorig
