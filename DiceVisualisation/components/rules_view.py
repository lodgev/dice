import streamlit as st


def display_rules():
    """Відображає правила гри з вкладками для стратегій."""
    st.title("Game Rules")

    # Вкладки для різних стратегій
    tabs = st.tabs(["General Rules", "Standard Strategy", "Sum Strategy", "Double Strategy"])

    with tabs[0]:
        st.header("General Rules")
        st.write("""
        - The game involves rolling two dice for a series of rounds.
        - The goal is to maximize your total score based on the selected scoring strategy.
        - Each game consists of 10 rounds by default.
        - After each game, your total score is recorded in the scoreboard.
        """)

    with tabs[1]:
        st.header("Standard Strategy")
        st.write("""
        - In the Standard Strategy:
            - You score **10 points** if the sum of the dice equals **7**.
            - Otherwise, you score **0 points** for the round.
        - This strategy rewards players who aim for the "lucky 7."
        """)

    with tabs[2]:
        st.header("Sum Strategy")
        st.write("""
        - In the Sum Strategy:
            - Your score for each round is the **sum of the two dice**.
            - This strategy rewards high rolls and consistent performance across rounds.
        """)

    with tabs[3]:
        st.header("Double Strategy")
        st.write("""
        - In the Double Strategy:
            - If either dice roll is a **6**, your score for the round is **doubled**.
            - Otherwise, you score the **sum of the two dice**.
        - This strategy rewards risky plays with high potential payoffs.
        """)

