class Route:
    def __init__(self, path=None, resource=None, methods=None):
        if path is None:
            path = getattr(self, 'path', '')
        self.path = path

        if resource is None:
            try:
                resource = getattr(self, 'resource')
            except AttributeError:
                raise TypeError("Missing resource specification.")
        self.resource = resource

        if methods is None:
            methods = getattr(self, 'methods', None)
        self.methods = methods
