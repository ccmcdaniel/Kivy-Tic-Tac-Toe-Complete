from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.app import App

class GameResultScreen(Screen):
    winner_name = StringProperty("")

    player1_name = StringProperty("")
    player2_name = StringProperty("")

    player1_score = StringProperty("")
    player2_score = StringProperty("")
    
    def setup_screen(self):
        app = App.get_running_app()
        winner = app.game_session.GetWinnerName()

        if(winner != ""):
            self.winner_name  = f"{winner} won the game!"
        else:
            self.winner_name = "A Tie Occurred."

        self.player1_name = app.game_session.player1.name
        self.player2_name = app.game_session.player2.name

        self.player1_score = f"{app.game_session.player1.score}"
        self.player2_score = f"{app.game_session.player2.score}"

    def on_clicked_new_game(self):
        app = App.get_running_app()
        app.game_session.StartNewGame()
        self.manager.current = 'game'
        self.manager.current_screen.setup_screen()