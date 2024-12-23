from DiceSystem.components.game import Game
# from DicePersist.highscore_repo import HighScoreRepo
from datetime import datetime
from DicePersist.factory.persist_kit import PersistKit

class DiceSystem:
    def __init__(self, persistence_type="nosql"):
        self.game_instance = None
        self.game_number = 0  
        self.persistence_type = persistence_type
        self._initialize_repo()

    def _initialize_repo(self):
        factory = PersistKit.get_persistence_kit(self.persistence_type)
        self.highscore_repo = factory.create_highscore()
    
    def switch_persistence(self, new_persistence_type):
        if self.persistence_type != new_persistence_type:
            self.persistence_type = new_persistence_type
            self._initialize_repo()

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

    def get_combined_top_scores(self, limit=10):
        """Повертає топ-10 результатів зі всіх сховищ."""
        all_scores = []

        # Перебір усіх типів сховищ
        for persistence_type in ["nosql", "jdbc", "sr"]:
            self.switch_persistence(persistence_type)
            top_scores = self.get_top_scores(limit=limit)

            # Форматування результатів для уніфікації
            for record in top_scores:
                if isinstance(record, dict):  # MongoDB (NoSQL)
                    all_scores.append({
                        "player_name": record["player_name"],
                        "score": int(record["score"]),
                        "date_obtained": record["date_obtained"]
                    })
                elif isinstance(record, (list, tuple)):  # SQLite (JDBC) або CSV (SR)
                    all_scores.append({
                        "player_name": record[0],
                        "score": int(record[1]),
                        "date_obtained": record[2]
                    })

        unique_scores = {f"{r['player_name']}_{r['score']}_{r['date_obtained']}": r for r in all_scores}

        sorted_scores = sorted(unique_scores.values(), key=lambda x: x["score"], reverse=True)


        return sorted_scores[:limit]