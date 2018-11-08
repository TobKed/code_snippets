# CLOSURES
def html_tag(tag):
    def wrap_text(msg):
        return "<{0}>{1}</{0}".format(tag, msg)
    return wrap_text


print_h1 = html_tag('h1')

print(print_h1('First header'))
print(print_h1('Another header'))
print()


# DECORATORS

# decorator function
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

# decorator class
class decorator_class(object):
    
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_function     # display = decorator_function(display)
def display():
    print('display function ran')

@decorator_function     # display_info = decorator_function(display_info)
def display_info(name, age):
    print('display_info ran with arguments {}, {}'.format(name, age))

@decorator_class
def display_2():
    print('display_2 function ran')

@decorator_class
def display_info_2(name, age):
    print('display_info_2 ran with arguments {}, {}'.format(name, age))


display()
display_info('John', 25)
print()
display_2()
display_info_2('John', 25)


# STACK OF DECORATORS WITH ARGUMENTS
from functools import wraps


def html_tag(tag):
    def decorator(orig_func):
        @wraps(orig_func)
        def wrapper(*args, **kwargs):
            text = orig_func(*args, **kwargs)
            return f"<{tag}>{text}</{tag}>"
        return wrapper
    return decorator


@html_tag("div")
@html_tag("p")
def get_span(text):
    """ doc string test"""
    return f"<span>{text}</span>"


print(get_span("sample text"))
print(get_span.__doc__)
