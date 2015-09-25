from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from view.layouts.actionmenulayout import ActionMenuLayout
from kivy.uix.label import Label
# from kivy.properties import ObjectProperty


class ItemLabel(Label):
    def set_text(self, text):
        self.text = text
    pass


class TwoHorizontalLayout(GridLayout):
    """Grid for text console screen and item selection menu"""
    Builder.load_file('./view/layouts/twohorizontallayout.kv')

    def __init__(self, **kwargs):
        super(TwoHorizontalLayout, self).__init__(**kwargs)
        label = self.ids.item_label
        action_menu_layout = self.ids.action_menu_layout
        action_menu_layout.set_label(label)
    pass
