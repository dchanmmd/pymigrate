from app.core.testing.populate import randbool, randbranch, randcat, randfloat, randname, randpawn, randbarcode

def get_inventory_list() -> list[dict]:
    table = []
    for _ in range(10):
        b = randbool()
        dict = {
            'barcode': randbarcode(8, 12),
            'name': randname(),
            'uom': 'Unidades',
            'purchase_uom': 'Unidades',
            'weight': randfloat(0, 20, 1),
            'sellable': b,
            'buyable': not b,
            'product_type': 'Producto Almacenable',
            'provider_tax': 'ITBMS',
            'customer_tax': 'ITBMS',
            'tags': 'LOGICA DE ETIQUETAS',
            'rp': f"{randfloat(100, 450, 2):.2f}",
            'cost': f"{randfloat(100, 450, 2):.2f}",
            'observations': 'lorem ipsum dolor sit amet' if randbool() else '',
            'pawn_no': randpawn(),
            'stone_wght': 0 if randbool() else 0 if randbool() else randfloat(0, 20, 1),
            'brand': 'OTRAS' if randbool() else 'OTRAS' if randbool() else '',
            'model': '',
            'series': '',
            'branch': randbranch(),
            'category': randcat(),
        }

        table.append(dict)
    return table