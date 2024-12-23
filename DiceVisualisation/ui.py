import streamlit as st
from DiceVisualisation.components.game_view import display_game
from DiceVisualisation.components.highscore_view import display_highscores
from DiceVisualisation.components.rules_view import display_rules
from DiceVisualisation.components.config_settings import configure_settings
from DiceSystem.dice_system import DiceSystem

def run_ui():
    # st.sidebar.title("Menu")
    
    # option = st.sidebar.selectbox("Choose an option", ["Play", "View scoreboard", "View rules", "Configure settings"])

    # # Ініціалізація DiceSystem у session_state
    # if "dice_system" not in st.session_state:
    #     st.session_state["dice_system"] = DiceSystem(persistence_type=st.session_state["persistence_type"])
    #     # st.session_state["dice_system"] = DiceSystem()
    # if "game_number" not in st.session_state:
    #     st.session_state["game_number"] = 1  

    # dice_system = st.session_state["dice_system"]
    
    st.sidebar.title("Menu")
    
    option = st.sidebar.selectbox("Choose an option", ["Play", "View scoreboard", "View rules", "Configure settings"])

    # Зберігаємо обраний тип сховища
    if "persistence_type" not in st.session_state:
        st.session_state["persistence_type"] = "nosql"  # Значення за замовчуванням

    persistence_type = st.sidebar.selectbox("Select Storage Type", ["nosql", "jdbc", "sr"])
    
    # Якщо тип сховища змінився, очищуємо і оновлюємо DiceSystem
    if st.session_state["persistence_type"] != persistence_type:
        st.session_state["persistence_type"] = persistence_type
        if "dice_system" in st.session_state:
            del st.session_state["dice_system"]

    # Ініціалізація DiceSystem у session_state
    if "dice_system" not in st.session_state:
        st.session_state["dice_system"] = DiceSystem(persistence_type=st.session_state["persistence_type"])

    dice_system = st.session_state["dice_system"]

    st.write(f"Current persistence type: {st.session_state['persistence_type']}")
    # st.write(f"Initialized with persistence type: {dice_system.highscore_repo.__class__.__name__}")
    
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
            display_game(dice_system)

    elif option == "View scoreboard":
        display_highscores(dice_system)
    
    elif option == "View rules":
        display_rules()
        
    elif option == "Configure settings":
        configure_settings()