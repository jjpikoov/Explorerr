from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from buttons.actionsmenu import make_buttons
from kivy.uix.widget import Widget

# Later to delete
class ItemLabel(Label):
    def __init__(self, txt):
        self.text = txt

    def set_text(self, text):
        self.text = text
    pass


class DividedByToLayout(GridLayout):
    """Grid for text console and inventory menu"""
    def __init__(self):
        super(DividedByToLayout, self).__init__()
        self.rows = 2


class ActionsLayout(GridLayout):
    """Grid for menu with possible actions"""
    def __init__(self):
        super(ActionsLayout, self).__init__()
        self.rows = 4
        self.cols = 3


class MainLayout(Widget):
    """DividedByToLayout with ActionsLayout in one with all action buttons"""
    def __init__(self):
        self.al = ActionsLayout()
        self.al.add_widget(make_buttons())

        self.dbtl = DividedByToLayout()

        self.dbtl.add_widget(self.al)

    def return_layout(self):
        return self.dbtl
