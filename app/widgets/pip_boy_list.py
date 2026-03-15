from kivy.uix.boxlayout import BoxLayout
from app.widgets.pip_boy_list_item import PipBoyListItem
from app.core.sound_manager import sound_manager


class PipBoyList(BoxLayout):

    def __init__(self, items, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint_y = None
        self.bind(minimum_height=self.setter("height"))
        self.spacing = 4

        self.rows = []

        for i, text in enumerate(items):

            row = PipBoyListItem(text=text)

            row.bind(on_touch_down=self.on_row_click)

            self.rows.append(row)
            self.add_widget(row)

        if self.rows:
            self.select_row(self.rows[0])

    def on_row_click(self, row, touch):

        if row.collide_point(*touch.pos):
            sound_manager.play_click()
            self.select_row(row)

    def select_row(self, selected_row):

        for row in self.rows:
            row.set_selected(row == selected_row)
