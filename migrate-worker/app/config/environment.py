from os import getenv
from dotenv import load_dotenv
load_dotenv()

class Environment:
    def __init__(self):
        annotations = {}
        for class_name in reversed(type(self).__mro__):
            annotations.update(getattr(class_name, '__annotations__', {}))

        defaults = {}
        for class_name in reversed(type(self).__mro__):
            defaults.update({
                k: v for k, v in vars(class_name).items()
                if not k.startswith('_') and k in annotations
            })

        for name, ann in annotations.items():
            var = getenv(name)

            if var is None:
                if name in defaults:
                    setattr(self, name, defaults[name])
                    continue
                raise EnvironmentError(f"Missing required environment variable '{name}'")

            if ann is str:
                setattr(self, name, var)
            elif ann is int or ann is float:
                try:
                    setattr(self, name, ann(var))
                except ValueError:
                    raise EnvironmentError(f"Expected '{name}' to be {ann.__name__}, got '{var}'")
            elif ann is bool:
                setattr(self, name, var.strip().lower() == 'true')
            else:
                raise EnvironmentError(f"Unsupported type '{ann}' for variable '{name}'")