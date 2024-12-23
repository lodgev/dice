from DiceSystem.components.game import Game
from DicePersist.highscore_repo import HighScoreRepo
from datetime import datetime

class DiceSystem:
    def __init__(self):
        self.game_instance = None
        self.game_number = 0  
        self.highscore_repo = HighScoreRepo() 

    def start_game(self, player_name):
        """Ініціалізує нову гру для гравця."""
        self.game_instance = Game(player_name)
        self.game_number += 1 
        return f"Game {self.game_number} initialized! Let's start."


    def roll_dice(self):
        """Кидає кубики та обробляє результат."""
        if not self.game_instance:
            raise ValueError("Game not initialized. Call start_game first.")
        # print(f"Before rolling: Current round = {self.game_instance.current_round}, Max rounds = {self.game_instance.nrounds}")
        if self.game_instance.is_game_over():
            # print("Game is over. Saving score...")
            self._save_score()
            return "Game over! No more rounds left."
        
        result = self.game_instance.roll_dices()
        # print(f"After rolling: Current round = {self.game_instance.current_round}, Max rounds = {self.game_instance.nrounds}")
        
        if self.game_instance.is_game_over():
            # print("Game is now over after this roll. Saving score...")
            self._save_score()
        return result

    def _save_score(self):
        """Зберігає фінальний рахунок у базу даних із додаванням дати."""
        final_score = self.game_instance.total_score
        date_obtained = datetime.now().strftime("%d.%m.%Y")  # Формат дати: день.місяць.рік
        self.highscore_repo.add_score(
            self.game_instance.player_name,
            final_score,
            date_obtained
        )

    def get_top_scores(self, limit=10):
        """Повертає топ-результати з таблиці рекордів."""
        return self.highscore_repo.get_top_scores(limit=limit)

    def get_current_round(self):
        """Повертає номер поточного раунду."""
        return self.game_instance.current_round if self.game_instance else 0

    def get_total_score(self):
        """Повертає загальний рахунок."""
        return self.game_instance.total_score if self.game_instance else 0

    def get_game_number(self):
        """Повертає номер поточної гри."""
        return self.game_number
