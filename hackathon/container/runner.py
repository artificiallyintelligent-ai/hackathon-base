import copy
import importlib
import sys
import traceback

from RestrictedPython import safe_builtins, PrintCollector

limited_builtins = {}


def import_call(allowed_modules):
    def inner(name, *args):
        assert (isinstance(name, str))

        if name in allowed_modules and name in sys.modules:
            sys.modules.pop(name, None)
            return importlib.import_module(name)

        if 'stubs' in name:
            class Empty:
                __all__ = []

            return Empty()

        raise Exception('Disallowed import call: {}'.format(name))

    return inner


builts = safe_builtins
extra_builtins = {
    'print': PrintCollector,
    'super': super,
    'min': min,
    'max': max,
    'sorted': sorted,
    'reversed': reversed,
    'map': map,
    'sum': sum,
    'any': any,
    'all': all,
    'list': list,
    'dict': dict,
    'enumerate': enumerate,
}
builts.update(extra_builtins)
restricted_globals = {
    '__builtins__': builts,
    '__name__': '__main__'
}


def build_globals(env):
    rglobals = copy.copy(restricted_globals)
    rglobals['__builtins__']['__import__'] = import_call(allowed_modules=env.allowed_modules)

    rglobals.update(env.globals)

    return rglobals


class CodeRunner:
    def __init__(self, env, code: str):
        self.code = code

        self.globals = build_globals(env)

    def init_code(self):
        try:
            exec(self.code, self.globals)
        except:
            traceback.print_exc()

    def run(self, funcname='turn'):
        try:
            if funcname in self.globals.keys():
                code = self.globals[funcname].__code__
                exec(code, self.globals)
            else:
                raise NotImplementedError(f'Function {funcname} is not implemented')
        except:
            traceback.print_exc()
