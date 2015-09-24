from kivy.app import App
from view.layouts.twohorizontallayout import TwoHorizontalLayout


class ExplorerrApp(App):
    """Starting class"""
    def build(self):
        """This stuff will be run"""
        return TwoHorizontalLayout()

if __name__ == '__main__':
    ExplorerrApp().run()
