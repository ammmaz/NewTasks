import importlib
import os

def load_parsers():
    parsers = {}
    for fname in os.listdir('parsers'):
        if fname.endswith('.py') and fname != '__init__.py':
            mod = importlib.import_module(f'parsers.{fname[:-3]}')
            parsers[mod.name] = mod.Parser()
    return parsers
