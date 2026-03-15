class Theme:

    def __init__(self):

        # Classic Pip-Boy green
        self.primary = (0.18, 1.0, 0.18, 1)

        # Text color
        self.text = (0.3, 1, 0.3, 1)
        # self.text = (0.18, 1.0, 0.18, 1)

        # Dark screen background
        self.background = (0.02, 0.02, 0.02, 1)

        # Font path
        self.font = "app/assets/fonts/Share-TechMono.ttf"

        # Dark Green
        self.inverse_green = (0.15, 0.5, 0.15, 1)


theme = Theme()
