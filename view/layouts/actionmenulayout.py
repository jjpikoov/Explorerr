from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
# from jnius import autoclass
import jnius


class ActionMenuLayout(GridLayout):
    """Layout of actions menu, where user can tap on item"""
    Builder.load_file('./view/layouts/actionmenulayout.kv')

    def set_label(self, label):
        self.item_label = label


    def vibrate(self, seconds):
        try:
            PythonActivity = jnius.autoclass('org.renpy.android.PythonActivity')
            Context = jnius.autoclass('android.content.Context')
            activity = PythonActivity.mActivity
            vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
            vibrator.vibrate(seconds)
        except jnius.JavaException:
                print("(Explorerr): Vibration not avaiable, are you on computer?")
