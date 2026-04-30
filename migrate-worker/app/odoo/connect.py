import json

from app.config.app_environment import env
import xmlrpc.client
common = xmlrpc.client.ServerProxy(f"{env.ODOO_URL}/xmlrpc/2/common")
uid = common.authenticate(env.ODOO_DB, env.ODOO_USER, env.ODOO_PASSWORD, {})

models = xmlrpc.client.ServerProxy(f"{env.ODOO_URL}/xmlrpc/2/object")