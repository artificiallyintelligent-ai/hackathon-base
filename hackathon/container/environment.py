class Environment:
    def __init__(self, globals_=None, allowed_modules=None):
        if allowed_modules is None:
            allowed_modules = []

        if globals_ is None:
            globals_ = {}

        self.globals = globals_
        self.allowed_modules = allowed_modules
