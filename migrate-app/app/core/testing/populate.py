from datetime import datetime, timezone
from random import choice, randint , random
from string import ascii_letters, digits

items = ['Anillo', 'Dije', 'Collar', 'Pulsera', 'Arete', 'Reloj']
gender = ['Hombre', 'Mujer']
branches = ['LOS ANDES', 'CC SAN MIGUELITO METRO', 'VILLA LUCRE', 'MONTE OSCURO', 'EL BOSQUE TUMBA MUERTO', 'LOS ANDES METRO', 'SAN MIGUELITO']
metal = ['Oro', 'Plata']
gold_k = [8, 10, 12, 14 ,18, 20]
silver_f = [925, 999, 958, 900]

def randbarcode(min: int, max: int) -> str:
    length = randint(min, max)
    chars = ascii_letters + digits
    return ''.join(choice(chars) for _ in range(length)).upper()

def randname():

    return f"{choice(items)} {choice(gender)} {randint(4, 20)}kg"

def randfloat(min: float, max: float, s: int) -> float:
    return round(random() * (max - min) + min, s)

def randbool():
    return random() >= 0.5

def randbranch():
    return choice(branches)

def randcat():
    randmet = choice(metal)
    return f"{randmet}/{choice(gold_k if randmet == 'Oro' else silver_f)}/{choice(items)}"

def randpawn():
    return f"EM{''.join([s[0] for s in choice(branches).split(' ')])}-{randint(19, 26)}-{str(randint(0, 99999)).zfill(5)}"