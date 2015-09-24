from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from view.layouts.actionmenulayout import ActionMenuLayout


class TwoHorizontalLayout(GridLayout):
    """Grid for text console screen and item selection menu"""
    Builder.load_file('./view/layouts/twohorizontallayout.kv')
    pass
