import streamlit as st

from DiceSystem.components.game import GameObserver
from .dice_view import display_dice


# def display_game(dice_system):
#     """Відображає поточний стан гри."""
#
#     # Перевірка завершення гри
#     if dice_system.game_instance.is_game_over():
#         st.write("Game over! No more rounds left.")
#
#         col1, col2 = st.columns(2)
#
#         # Кнопка "Start New Game"
#         if col1.button("Start New Game", key="start_new_game"):
#             dice_system.start_game(st.session_state["player_name"])  # Перезапускаємо гру
#             st.session_state["game_initialized"] = True
#             st.rerun()  # Перезавантаження сторінки для нової гри
#
#         # Кнопка "Quit"
#         if col2.button("Quit", key="quit_game"):
#             st.session_state.clear()  # Очищає весь session_state
#             st.rerun()  # Перезапускає сторінку
#     else:
#         # Логіка гри, якщо гра не завершена
#         if st.button("Roll Dice"):
#             result = dice_system.roll_dice()
#             if isinstance(result, str):
#                 st.write(result)  # Наприклад, "Game over! No more rounds left."
#             else:
#                 rolls, round_score, current_round = result
#                 st.subheader(f"Round {current_round} Results:")
#
#                 # Відображення кубиків у динамічних колонках
#                 columns = st.columns(len(rolls))
#                 for roll, col in zip(rolls, columns):
#                     display_dice(roll, col)
#
#                 # Відображення результатів
#                 st.write(f"Score this round: {round_score}")
#                 st.write(f"Total Score: {dice_system.get_total_score()}")


import streamlit as st
from .dice_view import display_dice


class GameView(GameObserver):
    """Streamlit-based view for displaying the game state."""
    def __init__(self):
        self.latest_game_state = None

    def update(self, game_state):
        """Update the view when the game state changes."""
        self.latest_game_state = game_state
        self.display_game_state()

    def display_game_state(self):
        """Display the updated game state."""
        game_state = self.latest_game_state
        if game_state:
            st.write(f"Player: {game_state['player_name']}")
            st.write(f"Round: {game_state['current_round']}/{game_state['nrounds']}")
            st.write(f"Total Score: {game_state['total_score']}")

    def display_game(self, dice_system):
        """Display the game UI and handle user actions."""
        if dice_system.game_instance.is_game_over():
            st.write("Game over! No more rounds left.")

            col1, col2 = st.columns(2)

            if col1.button("Start New Game", key="start_new_game"):
                dice_system.start_game(st.session_state["player_name"])
                st.session_state["game_initialized"] = True
                st.rerun()

            if col2.button("Quit", key="quit_game"):
                st.session_state.clear()
                st.rerun()
        else:
            if st.button("Roll Dice"):
                result = dice_system.roll_dice()
                if isinstance(result, str):
                    st.write(result)
                else:
                    rolls, round_score, current_round = result
                    st.subheader(f"Round {current_round} Results:")
                    columns = st.columns(len(rolls))
                    for roll, col in zip(rolls, columns):
                        display_dice(roll, col)

                    st.write(f"Score this round: {round_score}")
                    st.write(f"Total Score: {dice_system.get_total_score()}")
