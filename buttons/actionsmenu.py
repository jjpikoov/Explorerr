from kivy.uix.image import Image
from kivy.uix.button import Button


def make_buttons():
    yes_button = Button()
    yes_button.background_color = [10, 100, 205, 0.5]
    yes_button.image = Image(
            source='./images/yes.png',
#            x=self.parent.x,
#            y=self.parent.y,
#            size=(self.parent.width, self.parent.height),
            allow_stretch=True)

    # self.add_widget(yes_button)

    return yes_button


