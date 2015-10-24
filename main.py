from kivy.app import App
from view.layouts.layouts import MainLayout


class ExplorerrApp(App):
    """Starting class"""
    def build(self):
        """This stuff will be run"""
        ml = MainLayout()
        return ml.return_layout()

if __name__ == '__main__':
    ExplorerrApp().run()
