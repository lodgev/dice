import streamlit as st

def configure_settings():
    """Відображає інтерфейс для налаштування параметрів гри."""
    st.title("Game Settings")

    # Кількість раундів
    if "nrounds" not in st.session_state:
        st.session_state["nrounds"] = 10  # Значення за замовчуванням

    nrounds = st.slider("Number of Rounds", min_value=1, max_value=20, value=st.session_state["nrounds"], step=1)
    st.session_state["nrounds"] = nrounds

    # Поріг очок для виграшу раунду
    if "score_threshold" not in st.session_state:
        st.session_state["score_threshold"] = 7  # Значення за замовчуванням

    score_threshold = st.slider("Score Threshold for Points", min_value=2, max_value=12, value=st.session_state["score_threshold"], step=1)
    st.session_state["score_threshold"] = score_threshold

    # Очки за раунд
    if "points_per_round" not in st.session_state:
        st.session_state["points_per_round"] = 10  # Значення за замовчуванням

    points_per_round = st.slider("Points for Winning a Round", min_value=1, max_value=50, value=st.session_state["points_per_round"], step=1)
    st.session_state["points_per_round"] = points_per_round

    # Відображення налаштувань
    st.subheader("Current Settings:")
    st.write(f"Number of Rounds: {st.session_state['nrounds']}")
    st.write(f"Score Threshold: {st.session_state['score_threshold']}")
    st.write(f"Points per Round: {st.session_state['points_per_round']}")

    st.success("Settings updated successfully!")
