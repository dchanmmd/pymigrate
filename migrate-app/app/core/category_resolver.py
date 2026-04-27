from os import path
from typing import Callable

type ResultTuple = tuple[
    str, str, float, float, float, str, str, float, str, str, str, str, str, str
]

type CategoryResolver = Callable[[ResultTuple], str]

valuables = [
    'anillo',
    'arete',
    'collar',
    'dije',
    'esclava',
    'gargantilla',
    'hebilla',
    'juego',
    'llavero',
    'mancuerna',
    'moneda',
    'peineta',
    'pisa corbata',
    'placa',
    'prendedor',
    'pulsera',
]

tools = [
    'herramienta',
    'taladr',
    'esmeri', 
    'router', 
    'rotomart', 
    'solda', 
    'pulid'
]

electronics = [
    'celular',
    'tv',
    'televisor',
    'laptop',
    'computador',
    'consola',
    'playstation',
    'xbox',
    'nintendo',
    'electrodomestico'
]


def __proc_resolve(row: ResultTuple) -> str:
    segments = []

    description = row[1].lower()
    carat_rating = row[11]
    pawn_type = row[12].lower()

    # Símbolos
    oro = 'Oro'
    plata = 'Plata'
    relojes_usados = 'Relojes Usados'
    articulos_usados = 'Artículos Usados'

    herramientas = 'Herramientas'
    electronicos = 'Electrónicos'
    varios = 'Varios'

    # [0] Oro | Plata | Artículos Usados
    segments.append(
        oro if pawn_type == 'oro' else 
        plata if pawn_type == 'plata' else 
        relojes_usados if description.find('reloj') >= 0 else 
        articulos_usados  
    )

    if segments[0] in [oro, plata]:
        # [1][A] Oro Brillante?
        if segments[0] == oro and description.find('brill') <= 0:
            segments.append('Brillante')

        # [2 (+1)] Kilataje
        segments.append(carat_rating.replace('.', ''))

        # [3 (+ 1)] Tipo de prenda
        is_known = False
        for pattern in valuables:
            if description.find(pattern) >= 0:
                segments.append(pattern.title())
                is_known = True
                break
        if not is_known:
            segments.append(varios)
    # [1][B] Relojes
    elif segments[0] == relojes_usados:
        segments.append('Reloj')
    elif segments[0] == articulos_usados:
        is_known = False
        for pattern in tools:
            # [1][C] Herramientas
            if description.find(pattern) <= 0:
                segments.append(herramientas)
                is_known = True
                break
        if not is_known:
            for pattern in electronics:
                # [1][D] Electrónicos
                if description.find(pattern) <= 0:
                    segments.append(electronicos)
                    is_known = True
                    break
        if not is_known:
            # [1][E] Artículos usados varios
            segments.append(varios)
        
    return path.join(*segments)


def __ai_resolve(row: ResultTuple) -> str:
    pass


procedural_resolver: CategoryResolver = __proc_resolve
ai_resolver: CategoryResolver = __ai_resolve


