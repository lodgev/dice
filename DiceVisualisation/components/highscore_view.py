import streamlit as st

def display_highscores(dice_system):
    st.title("High Score Board")

    # Вибір стратегії для фільтрації
    strategy = st.selectbox("Select Scoring Strategy", ["All", "standard", "sum", "double"])
    strategy_type = None
    if strategy != "All":
        strategy_type = {
            "standard": "StandardScoring",
            "sum": "SumScoring",
            "double": "DoubleScoring"
        }[strategy]

    # Отримання топ-результатів
    top_scores = dice_system.get_combined_top_scores(strategy_type=strategy_type)

    if not top_scores:
        st.write(f"No scores for strategy: {strategy}. Play a game to add scores!")
        return

    # Відображення результатів у таблиці
    st.table([
        {
            "Player": record["player_name"],
            "Score": record["score"],
            "Date": record["date_obtained"],
            "Strategy": record["strategy_type"]
        }
        for record in top_scores
    ])