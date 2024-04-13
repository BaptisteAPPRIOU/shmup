class GameManager:
    def __init__(self):
        pass

    def show_leaderboard_page(self):  
        from leaderboard_page import LeaderboardPage
        leaderboard_page = LeaderboardPage()  
        leaderboard_page.run()

    def show_landing_page(self):
        from landing_page import LandingPage
        landing_page = LandingPage()
        landing_page.run()

    def show_tutorial_page(self):
        from tutorial_page import TutorialPage
        tutorial_page = TutorialPage()
        tutorial_page.run()
    
    def show_exit_page(self, parent_screen):
        from exit_page import ExitPage
        exit_page = ExitPage(parent_screen)
        exit_page.run()

    def show_level1_page(self, username):
        from level1 import Level1
        level1_page = Level1(username)
        level1_page.run()

    def show_credits_page(self):
        from credits_page import CreditsPage
        credits_page = CreditsPage()
        credits_page.run()

    def show_user_creation_page(self):
        from user_creation_page import UserCreationPage
        user_creation_page = UserCreationPage()
        user_creation_page.run()

    def show_game_over_page(self, parent_screen, total_score, username):
        from game_over_page import GameOverPage
        game_over_page = GameOverPage(parent_screen, total_score, username)
        game_over_page.run()