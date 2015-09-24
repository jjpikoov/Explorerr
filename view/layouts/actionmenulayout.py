from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


class ActionMenuLayout(GridLayout):
    """Layout of actions menu, where user can tap on item"""
    Builder.load_file('./view/layouts/actionmenulayout.kv')
    pass
