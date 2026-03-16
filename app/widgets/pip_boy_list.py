from kivy.uix.boxlayout import BoxLayout
from app.widgets.pip_boy_list_item import PipBoyListItem
from app.core.sound_manager import sound_manager


class PipBoyList(BoxLayout):

    def __init__(self, items, on_select=None, auto_select=True, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint_y = None
        self.bind(minimum_height=self.setter("height"))
        self.spacing = 4

        self.rows = []
        self.on_select = on_select  # callback from screen

        for text in items:

            row = PipBoyListItem(text=text)

            row.bind(on_touch_down=self.on_row_click)

            self.rows.append(row)
            self.add_widget(row)

        if self.rows and auto_select:
            self.on_select(self.rows[0].text)

    def on_row_click(self, row, touch):

        if row.collide_point(*touch.pos):
            sound_manager.play_click()
            self.select_row(row)

            if self.on_select:
                self.on_select(row.text)

    def select_row(self, selected_row):

        for row in self.rows:
            row.set_selected(row == selected_row)
