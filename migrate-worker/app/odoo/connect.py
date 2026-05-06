import json
from app.config.app_environment import env
import xmlrpc.client

url = env.ODOO_URL
db = env.ODOO_DB
user = env.ODOO_USER
password = env.ODOO_PASSWORD

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
common.version()

uid = common.authenticate(db, user, password, {})

models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

[record] = models.execute(db, uid, password, 'product.template', 'read', [22572])

# record = models.execute_kw(db, uid, password, 'product.product', 'fields_get', [], {'attributes': ['string', 'help', 'type']})

print(json.dumps(record, indent=4))