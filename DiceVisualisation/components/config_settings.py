import streamlit as st

class ConfigMemento:
    """Stores a snapshot of game settings at a specific point in time."""
    def __init__(self, nrounds, score_threshold, points_per_round):
        self.nrounds = nrounds
        self.score_threshold = score_threshold
        self.points_per_round = points_per_round

class ConfigSettingsManager:
    """Manages game settings with save and restore functionality."""

    def __init__(self):
        if "config_history" not in st.session_state:
            st.session_state["config_history"] = []  # Stack for storing previous configurations

        # Initialize default settings if not present
        if "nrounds" not in st.session_state:
            st.session_state["nrounds"] = 10
        if "score_threshold" not in st.session_state:
            st.session_state["score_threshold"] = 7
        if "points_per_round" not in st.session_state:
            st.session_state["points_per_round"] = 10

    def save_state(self):
        """Saves the current settings state before modification."""
        memento = ConfigMemento(
            st.session_state["nrounds"],
            st.session_state["score_threshold"],
            st.session_state["points_per_round"],
        )
        st.session_state["config_history"].append(memento)

    def restore_last_configuration(self):
        """Restores the last saved settings and updates UI elements."""
        if st.session_state["config_history"]:
            memento = st.session_state["config_history"].pop()
            st.session_state["nrounds"] = memento.nrounds
            st.session_state["score_threshold"] = memento.score_threshold
            st.session_state["points_per_round"] = memento.points_per_round
            st.warning("🔄 Settings restored to the previous state!")
        else:
            st.error("⚠️ No previous configurations to restore.")

def configure_settings():
    """Displays the UI for configuring game settings."""
    st.title("⚙️ Game Settings")

    manager = ConfigSettingsManager()

    # Number of rounds
    nrounds = st.slider(
        "Number of Rounds", min_value=1, max_value=20, value=st.session_state["nrounds"], step=1,
        key="slider_nrounds"
    )

    # Score threshold per round
    score_threshold = st.slider(
        "Score Threshold for Points", min_value=2, max_value=12, value=st.session_state["score_threshold"], step=1,
        key="slider_score_threshold"
    )

    # Points per round
    points_per_round = st.slider(
        "Points for Winning a Round", min_value=1, max_value=50, value=st.session_state["points_per_round"], step=1,
        key="slider_points_per_round"
    )

    # Save new settings only if changed
    if (
        nrounds != st.session_state["nrounds"]
        or score_threshold != st.session_state["score_threshold"]
        or points_per_round != st.session_state["points_per_round"]
    ):
        manager.save_state()  # Save the previous state before modifying

        st.session_state["nrounds"] = nrounds
        st.session_state["score_threshold"] = score_threshold
        st.session_state["points_per_round"] = points_per_round
        st.success("✅ Settings updated successfully!")

    # Display current settings
    st.subheader("📋 Current Settings:")
    st.write(f"**Number of Rounds:** {st.session_state['nrounds']}")
    st.write(f"**Score Threshold:** {st.session_state['score_threshold']}")
    st.write(f"**Points per Round:** {st.session_state['points_per_round']}")

    # Undo Button
    if st.button("Undo Last Change"):
        manager.restore_last_configuration()
        st.rerun()  # Forces UI to refresh with updated slider values


class ConfigMemento:
    """Stores a snapshot of game settings at a specific point in time."""
    def __init__(self, nrounds, score_threshold, points_per_round):
        self.nrounds = nrounds
        self.score_threshold = score_threshold
        self.points_per_round = points_per_round
