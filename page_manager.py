
class PageManager():
    @staticmethod
    def show_menu():
        from menu import Menu
        Menu()
    
    @staticmethod
    def show_user_choice():
        from user_choice import UserChoice
        UserChoice()
        
    @staticmethod
    def show_tutorial():
        from tutorial import Tutorial
        Tutorial()
