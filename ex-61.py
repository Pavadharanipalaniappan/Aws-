class Tomato:
    def type(self):
        return "Tomato"
    def color(self):
        return "Tomato color is red"
class Apple:
    def type(self):
        return "Apple"
    def color(self):
        return "Apple color is green"
def func(obj):
    if isinstance(obj, Tomato):
        print(obj.type())
        print(obj.color())
    elif isinstance(obj, Apple):
        print(obj.type())
        print(obj.color())
    else:
        print("Unknown object")
tomato_obj = Tomato()
apple_obj = Apple()
func(tomato_obj)
func(apple_obj)
