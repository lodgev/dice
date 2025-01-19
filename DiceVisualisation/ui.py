import streamlit as st

from components.game_view import GameView
from components.highscore_view import display_highscores
from components.rules_view import display_rules
from components.config_settings import configure_settings

from DiceSystem.dice_system import DiceSystem


def add_custom_css():
    """Додає кастомні стилі через CSS."""
    st.markdown("""
        <style>

        /* Таблиці */
        th, td {
            border: 1px solid #ddd;
            padding: 12px 15px;
            text-align: left;
        }

        th {
            color: white;
            font-weight: bold;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2; /* Світло-сірий фон для парних рядків */
        }

        tr:hover {
            background-color: #d1ecf1; /* Підсвічування рядка при наведенні */
            transition: background-color 0.3s ease-in-out;
        }

        td {
            text-align: center; /* Центруємо текст у комірках */
        }

        caption {
            margin-top: 10px;
            font-size: 18px;
            font-weight: bold;
            color: #004d99;
        }

        </style>
    """, unsafe_allow_html=True)

def run_ui():
    # Add custom CSS
    add_custom_css()

    # Initialize DiceSystem through Singleton
    dice_system = DiceSystem()

    game_view = GameView()

    st.sidebar.title("Menu")

    # Select menu option
    option = st.sidebar.selectbox("Choose an option", ["Play", "View scoreboard", "View rules", "Configure settings"])

    # Select storage type
    if "persistence_type" not in st.session_state:
        st.session_state["persistence_type"] = "nosql"  # Default value

    persistence_type = st.sidebar.selectbox("Select Storage Type", ["nosql", "jdbc", "sr"])

    # Update persistence type in DiceSystem
    if st.session_state["persistence_type"] != persistence_type:
        st.session_state["persistence_type"] = persistence_type
        dice_system.switch_persistence(persistence_type)

    # Select scoring strategy
    if "scoring_strategy" not in st.session_state:
        st.session_state["scoring_strategy"] = "standard"  # Default value

    strategy = st.sidebar.selectbox("Select Scoring Strategy", ["standard", "sum", "double"])

    # Update scoring strategy in DiceSystem
    if st.session_state["scoring_strategy"] != strategy:
        st.session_state["scoring_strategy"] = strategy
        dice_system.set_scoring_strategy(strategy)

    # Display current strategy
    st.sidebar.write(f"Current Scoring Strategy: {strategy}")

    # Menu logic
    if option == "Play":
        if "game_initialized" not in st.session_state:
            st.session_state["game_initialized"] = False

        if not st.session_state["game_initialized"]:
            player_name = st.text_input("Enter your name:")
            if st.button("Start Game"):
                st.session_state["game_initialized"] = True
                st.session_state["player_name"] = player_name
                st.session_state["game_message"] = dice_system.start_game(player_name)

        if st.session_state["game_initialized"]:
            st.write(st.session_state["game_message"])
            game_view.display_game(dice_system)

    elif option == "View scoreboard":
        display_highscores(dice_system)

    elif option == "View rules":
        display_rules()

    elif option == "Configure settings":
        configure_settings()

