def announce(f):
    def wrapper():
        print('About to run the funcion...')
        f()
        print('Done with the function.')
    return wrapper


# Wraps the function hello with the announce decorator:
@announce
def hello():
    print('Hello, world')


hello()
