class Version:
    def __init__(self, name=None, routes=None):
        if name is None:
            name = getattr(self, 'name', '')
        self.name = name

        self.routes = []
        if routes is None:
            try:
                routes = getattr(self.__class__, 'routes')
            except AttributeError:
                raise TypeError("Version must have routes.")

        actions = set()
        for route in routes:
            for action in route.actions:
                action = (route.path, action.request.verb)
                if action in actions:
                    raise AttributeError('Ambiguous route and action request definition.')
                actions.add(action)
            self.append(route)

    def append(self, child):
        self.routes.append(child)
        child.parent = self
