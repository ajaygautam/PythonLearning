'''
Create the scaffolding for a Flask-like framework.

>>> app = WebApp()
>>> @app.route("/")
... def index():
...     return 'Index Page'
...
>>> @app.route("/contact/")
... def contact():
...     return 'Contact Page'
...
>>> app.get("/")
'Index Page'
>>> app.get("/contact/")
'Contact Page'
>>> app.get("/no-such-page/")
'ERROR - no such page'


'''

# Write your code here:
class WebApp:
    functions_for_route = dict()

    def route(self, route_path):
        def decorator(func):
            self.functions_for_route[route_path] = func
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def get(self, route_path):
        function_for_route = self.functions_for_route.get(route_path)
        if function_for_route is None:
            return 'ERROR - no such page'
        return function_for_route()



# Do not edit any code below this line!
if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
