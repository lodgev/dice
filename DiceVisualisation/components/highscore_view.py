import streamlit as st

def display_highscores(dice_system):
    st.title("High Score Board")

    top_scores = dice_system.get_top_scores()

    if not top_scores:
        st.write("No scores yet. Play a game to add scores!")
        return

    # Відображення результатів у таблиці
    st.table(
        [{
            "Player": record["player_name"],
            "Score": record["score"],
            "Date": record["date_obtained"]
        } for record in top_scores]
    )

