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

    def show_upgrade_page(self, parent_screen, username, total_score, health, life):
        from upgrade_page import UpgradePage
        upgrade_page = UpgradePage(parent_screen, username, total_score, health, life)
        upgrade_page.run()

    def show_level2_page(self, username, total_score, health, life, upgrade):
        from level2 import Level2
        level2_page = Level2(username, total_score, health, life, upgrade)
        level2_page.run()

    def show_level3_page(self, parent_screen, username, total_score, health, life, damage_lvl2, speed_lvl2, health_lvl2):
        from level3 import Level3
        level3_page = Level3(parent_screen, username, total_score, health, life, damage_lvl2, speed_lvl2, health_lvl2)
        level3_page.run()

    def show_upgrade_page2(self, parent_screen, username, total_score, health, life, original_damage, original_speed, original_health):
        from upgrade_page2 import UpgradePage2
        upgrade_page2 = UpgradePage2(parent_screen, username, total_score, health, life, original_damage, original_speed, original_health)
        upgrade_page2.run()