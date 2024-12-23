import streamlit as st

def display_rules():
    """Відображає правила гри."""
    st.title("Rules of Dice Game")

    st.markdown("""
    ### How to Play:
    1. Enter your name and start the game.
    2. Roll two dice in each round.
    3. Your score increases based on the sum of the dice:
        - If the sum is **7**, you gain **10 points**.
        - Otherwise, no points are awarded for that round.
    4. The game consists of 10 rounds.

    ### Objectives:
    - Maximize your score by rolling strategic combinations.
    - Aim for the **High Score Board**!

    ### Game End:
    - The game ends after 10 rounds.
    - Your final score is saved and added to the High Score Board.

    ### Additional Rules:
    - If there’s a tie in scores, the earlier game takes precedence.
    - You can start a new game or quit after the game ends.

    ### Enjoy the game and good luck!
    """)

