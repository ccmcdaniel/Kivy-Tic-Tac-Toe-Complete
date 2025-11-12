from kivy.uix.screenmanager import Screen

class MainMenuScreen(Screen):
    def on_click_start_game(self):
        self.manager.current = 'setup_players'
        self.manager.current_screen.setup_screen()