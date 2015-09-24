from kivy.app import App
from kivy.app import Widget


class Foo(Widget):
    pass


class ExplorerrApp(App):
    """Starting class"""
    def build(self):
        """This stuff will be run"""
        return Foo()

if __name__ == '__main__':
    ExplorerrApp().run()
