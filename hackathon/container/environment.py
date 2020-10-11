class Environment:
    def __init__(self, globals=None, allowed_modules=None):
        if allowed_modules is None:
            allowed_modules = []

        if globals is None:
            globals = {}

        self.globals = globals
        self.allowed_modules = allowed_modules
