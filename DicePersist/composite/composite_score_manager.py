from DicePersist.composite.score_component import ScoreComponent

class CompositeScoreManager(ScoreComponent):
    """Composite-клас для об'єднання кількох джерел даних."""

    def __init__(self):
        self.children = {}
        self.active_component = None

    def add(self, persistence_type, component):
        """Додає компонент у Composite."""
        self.children[persistence_type] = component

    def set_active(self, persistence_type):
        """Встановлює активний компонент для роботи."""
        if persistence_type in self.children:
            self.active_component = self.children[persistence_type]
            print(f"Active persistence set to: {persistence_type}")  
        else:
            raise ValueError(f"Persistence type '{persistence_type}' not found in CompositeScoreManager.")

    def add_score(self, player_name, score, date_obtained, strategy_type):
        """Додає рахунок у вибрану базу даних."""
        if not self.active_component:
            raise ValueError("Active persistence component not set.")
        self.active_component.add_score(player_name, score, date_obtained, strategy_type)


    def get_scores(self):
        """Отримує результати з усіх баз даних."""
        all_scores = []
        for child in self.children.values():  # Перебираємо всі бази
            scores = child.get_scores()
            for record in scores:
                if isinstance(record, dict):  # MongoDB (NoSQL)
                    all_scores.append(record)
                elif isinstance(record, (list, tuple)):  # SQLite (JDBC) або CSV (SR)
                    all_scores.append({
                        "player_name": record[0],
                        "score": int(record[1]),
                        "date_obtained": record[2],
                        "strategy_type": record[3] if len(record) > 3 else None
                    })
                else:
                    raise ValueError(f"Unexpected record format: {record}")

        # Сортування за рахунком
        return sorted(all_scores, key=lambda x: x["score"], reverse=True)

