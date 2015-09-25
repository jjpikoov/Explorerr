from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from plyer.facades.vibrator import Vibrator


class ActionMenuLayout(GridLayout):
    """Layout of actions menu, where user can tap on item"""
    Builder.load_file('./view/layouts/actionmenulayout.kv')

    def set_label(self, label):
        self.item_label = label

    def vibrate(self, seconds):
        vibrator = Vibrator()
        try:
            vibrator.vibrate(seconds)
        except NotImplementedError:
            print "I can't vibrate, are you on computer?"
    pass
