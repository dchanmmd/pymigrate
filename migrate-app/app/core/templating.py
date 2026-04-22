from os import path
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='app/template')
templates.env.globals['layout'] = lambda p: path.join('layouts', p)
templates.env.globals['partial'] = lambda p: path.join('partials', p)