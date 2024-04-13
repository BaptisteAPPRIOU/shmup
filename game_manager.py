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

    def show_level1_page(self):
        from level1 import Level1
        level1_page = Level1()
        level1_page.run()