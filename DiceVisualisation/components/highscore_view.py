import streamlit as st
import pandas as pd

def display_highscores(dice_system):
    st.title("🏆 High Score Board")

    strategy = st.selectbox("Select Scoring Strategy", ["All", "standard", "sum", "double"])
    strategy_type = None
    if strategy != "All":
        strategy_type = {
            "standard": "StandardScoring",
            "sum": "SumScoring",
            "double": "DoubleScoring"
        }[strategy]

    # Get top scores
    top_scores = dice_system.get_combined_top_scores(strategy_type=strategy_type)

    if not top_scores:
        st.write(f"No scores for strategy: {strategy}. Play a game to add scores!")
        return

    df = pd.DataFrame(top_scores)

    if "_id" in df.columns:
        df = df.drop(columns=["_id"])

    df = df.rename(columns={
        "player_name": "Player",
        "score": "Score",
        "date_obtained": "Date",
        "strategy_type": "Strategy"
    })

    df.insert(0, "Rank", range(1, len(df) + 1))

    medals = ["🥇", "🥈", "🥉"]
    df["Rank"] = [medals[i] if i < 3 else str(i + 1) for i in range(len(df))]

    st.table(df.style.hide(axis="index"))



