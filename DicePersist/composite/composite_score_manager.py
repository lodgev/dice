from .score_component import ScoreComponent

class CompositeScoreManager(ScoreComponent):
    """Manages multiple persistence components with observer support."""

    def __init__(self):
        self.children = {}
        self.active_component = None
        self.observers = []  # List of observers (UI, logs, etc.)

    def add_observer(self, observer):
        """Registers an observer."""
        self.observers.append(observer)

    def remove_observer(self, observer):
        """Removes an observer."""
        self.observers.remove(observer)

    def notify_observers(self):
        """Notifies all observers when high scores update."""
        high_scores = self.get_scores()
        for observer in self.observers:
            observer.update(high_scores)


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


    def __iter__(self):
        """Returns an iterator for iterating over scores."""
        return ScoreIterator(self.get_scores())



class ScoreIterator:
    """Iterator for iterating through multiple score components."""
    def __init__(self, scores):
        # Sorting scores in descending order
        self._scores = sorted(scores, key=lambda x: x["score"], reverse=True)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._scores):
            score = self._scores[self._index]
            self._index += 1
            return score
        else:
            raise StopIteration

class ScoreObserver:
    """Interface for observing high score updates."""
    def update(self, high_scores):
        """This method will be called when high scores update."""
        pass

