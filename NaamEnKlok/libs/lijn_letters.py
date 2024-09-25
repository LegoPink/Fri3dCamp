import lvgl as lv
from . import lv_colors as col

#Je kan elke letter een andere stijl (kleur en lijndikte) geven als je wil
def geef_letter_style(kleur = col.lv_colors.PURPLE, lijn_dikte = 8, rounded = True):
    lijn_style = lv.style_t()
    lijn_style.init()
    lijn_style.set_line_width(lijn_dikte)
    lijn_style.set_line_color(kleur)
    lijn_style.set_line_rounded(rounded)
    return lijn_style

#LET OP: nog niet alle letters staan hier bij!
#Heb je andere letters nodig? Breid deze functie uit! Kijk naar een bestaande letter en probeer gewoon!
def geef_letter_punten(letter = "xxx"):
    #print("Letter punten voor ", letter)
    if letter is "F":
        points=  [ {"x":55, "y":5}, {"x":0, "y":5},{"x":0, "y":60},  {"x":45, "y":60},{"x":0, "y":60},{"x":0, "y":120}]
    elif letter is "r":
        points=  [ {"x":0, "y":120}, {"x":0, "y":60},{"x":0, "y":70},  {"x":15, "y":60},{"x":40, "y":60}]
    elif letter is "i":
        points=  [ {"x":0, "y":60},{"x":0, "y":120}]
    elif letter is "dot_i":
        points=  [ {"x":0, "y":0},{"x":0, "y":5}]
    elif letter is "d":
        points=  [ {"x":40, "y":0},{"x":40, "y":120},{"x":0, "y":110},{"x":40, "y":60}]
    elif letter is "P":
        points = [ {"x":0, "y":5}, {"x":0, "y":120}, {"x":0, "y":60}, {"x":55, "y":60}, {"x":0, "y":5} ]
    elif letter is "1":
        points=  [ {"x":0, "y":70},{"x":15, "y":60},{"x":15, "y":120}]
    elif letter is "2":
        points=  [ {"x":0, "y":70},{"x":15, "y":60},{"x":30, "y":60},{"x":40, "y":70},{"x":40, "y":90},{"x":0, "y":120},{"x":40, "y":120}]
    elif letter is "3":
        points=  [ {"x":0, "y":60},{"x":25, "y":60},{"x":40, "y":70},{"x":40, "y":80},{"x":25, "y":90},{"x":40, "y":100},{"x":40, "y":110},{"x":25, "y":120},{"x":0, "y":120}]
    elif letter is "4":
        points=  [ {"x":40, "y":100},{"x":0, "y":100},{"x":30, "y":60},{"x":30, "y":120}]
    elif letter is "5":
        points=  [ {"x":40, "y":60},{"x":0, "y":60},{"x":0, "y":85},{"x":40, "y":90},{"x":40, "y":105},{"x":35, "y":120},{"x":0, "y":120}]
    elif letter is "6":
        points=  [ {"x":35, "y":60},{"x":15, "y":60},{"x":0, "y":70},{"x":0, "y":110},{"x":10, "y":120},{"x":35, "y":120},{"x":40, "y":100},{"x":35, "y":90},{"x":0, "y":90}]
    elif letter is "7":
        points=  [ {"x":0, "y":60},{"x":40, "y":60},{"x":0, "y":120}]
    elif letter is "8":
        points=  [ {"x":0, "y":70},{"x":15, "y":60},{"x":40, "y":60},{"x":0, "y":120},{"x":35, "y":120},{"x":40, "y":110},{"x":0, "y":70}]
    elif letter is "9":
        points=  [ {"x":0, "y":120},{"x":30, "y":120},{"x":40, "y":90},{"x":5, "y":90},{"x":0, "y":70},{"x":15, "y":60},{"x":40, "y":60},{"x":40, "y":90}]
    elif letter is "0":
        points=  [ {"x":0, "y":60},{"x":30, "y":60},{"x":40, "y":70},{"x":40, "y":120},{"x":10, "y":120},{"x":0, "y":110},{"x":0, "y":60}]

    elif letter is ".":
        points=  [ {"x":0, "y":0},{"x":0, "y":5}]
    else:
        points= [{"x":0, "y":0},{"x":0, "y":1}]
    
    return points

#schuif_onder en #schuif_links bepalen hoever naar onder en links op het scherm de letter moet staan
def schrijf_letter(letter = "xxx", schuif_links =0, schuif_onder = 0, lijn_style = None, screen = None):
    points = []
    points = geef_letter_punten(letter)
    if len(points) <= 0: 
        print("Deze letter kan ik niet: ", letter)
        return
    
    if screen is None: screen = lv.screen_active()
    
    if lijn_style is None:
        lijn_style = geef_letter_style()
        
    line = lv.line(screen)
    line.set_points(points, len(points))   
    line.add_style(lijn_style,0)
    line.align(lv.ALIGN.CENTER, schuif_links, schuif_onder)