from engine import Engine

class FlaskEngine(Engine):
    '''The flask engine class which implements the specifics to find sources, sinks and sanitizers in flask web applications.'''

    def is_flask_route_function(self, function):
        return any(decorator for decorator in function.decorator_list if decorator.func.value.id == 'app' and decorator.func.attr == 'route')

    def find_flask_route_functions(self, functions):
        for func in functions.items():
            if self.is_flask_route_function(func[1]):
                yield func[1]

    def run(self):
        self.cfg_list.extend(self.find_flask_route_functions(self.cfg_list[0].functions))
