import streamlit as st

def display_highscores(dice_system):
    """Відображення таблиці з топ-результатами зі всіх баз даних."""
    st.title("High Score Board")

    # Отримання топ-результатів зі всіх сховищ
    top_scores = dice_system.get_combined_top_scores(limit=10)

    if not top_scores:
        st.write("No scores yet. Play a game to add scores!")
        return

    # Відображення результатів у вигляді таблиці
    st.table(
        [
            {
                "Player": record["player_name"],
                "Score": record["score"],
                "Date": record["date_obtained"]
            }
            for record in top_scores
        ]
    )
