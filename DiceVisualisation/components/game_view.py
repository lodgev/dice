import streamlit as st
from .dice_view import display_dice


def display_game(dice_system):
    """Відображає поточний стан гри."""
    
    # Перевірка завершення гри
    if dice_system.game_instance.is_game_over():
        st.write("Game over! No more rounds left.")

        col1, col2 = st.columns(2)

        # Кнопка "Start New Game"
        if col1.button("Start New Game", key="start_new_game"):
            dice_system.start_game(st.session_state["player_name"])  # Перезапускаємо гру
            st.session_state["game_initialized"] = True
            st.experimental_rerun()  # Перезавантаження сторінки для нової гри

        # Кнопка "Quit"
        if col2.button("Quit", key="quit_game"):
            st.session_state.clear()  # Очищає весь session_state
            st.experimental_rerun()  # Перезапускає сторінку
    else:
        # Логіка гри, якщо гра не завершена
        if st.button("Roll Dice"):
            result = dice_system.roll_dice()
            if isinstance(result, str):
                st.write(result)  # Наприклад, "Game over! No more rounds left."
            else:
                rolls, round_score, current_round = result
                st.subheader(f"Round {current_round} Results:")

                # Відображення кубиків у динамічних колонках
                columns = st.columns(len(rolls))
                for roll, col in zip(rolls, columns):
                    display_dice(roll, col)

                # Відображення результатів
                st.write(f"Score this round: {round_score}")
                st.write(f"Total Score: {dice_system.get_total_score()}")


