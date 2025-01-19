import streamlit as st

class ConfigMemento:
    def __init__(self, nrounds, score_threshold, points_per_round):
        self.nrounds = nrounds
        self.score_threshold = score_threshold
        self.points_per_round = points_per_round

class ConfigSettingsManager:

    def __init__(self):
        if "config_history" not in st.session_state:
            st.session_state["config_history"] = []  


        if "nrounds" not in st.session_state:
            st.session_state["nrounds"] = 10
        if "score_threshold" not in st.session_state:
            st.session_state["score_threshold"] = 7
        if "points_per_round" not in st.session_state:
            st.session_state["points_per_round"] = 10

    def save_state(self):
        memento = ConfigMemento(
            st.session_state["nrounds"],
            st.session_state["score_threshold"],
            st.session_state["points_per_round"],
        )
        st.session_state["config_history"].append(memento)

    def restore_last_configuration(self):

        if st.session_state["config_history"]:
            memento = st.session_state["config_history"].pop()
            st.session_state["nrounds"] = memento.nrounds
            st.session_state["score_threshold"] = memento.score_threshold
            st.session_state["points_per_round"] = memento.points_per_round
            st.warning("🔄 Settings restored to the previous state!")
        else:
            st.error("⚠️ No previous configurations to restore.")

def configure_settings():

    st.title("⚙️ Game Settings")

    manager = ConfigSettingsManager()

    nrounds = st.slider(
        "Number of Rounds", min_value=1, max_value=20, value=st.session_state["nrounds"], step=1,
        key="slider_nrounds"
    )


    score_threshold = st.slider(
        "Score Threshold for Points", min_value=2, max_value=12, value=st.session_state["score_threshold"], step=1,
        key="slider_score_threshold"
    )


    points_per_round = st.slider(
        "Points for Winning a Round", min_value=1, max_value=50, value=st.session_state["points_per_round"], step=1,
        key="slider_points_per_round"
    )


    if (
        nrounds != st.session_state["nrounds"]
        or score_threshold != st.session_state["score_threshold"]
        or points_per_round != st.session_state["points_per_round"]
    ):
        manager.save_state()  

        st.session_state["nrounds"] = nrounds
        st.session_state["score_threshold"] = score_threshold
        st.session_state["points_per_round"] = points_per_round
        st.success("✅ Settings updated successfully!")


    st.subheader("📋 Current Settings:")
    st.write(f"**Number of Rounds:** {st.session_state['nrounds']}")
    st.write(f"**Score Threshold:** {st.session_state['score_threshold']}")
    st.write(f"**Points per Round:** {st.session_state['points_per_round']}")


    if st.button("Undo Last Change"):
        manager.restore_last_configuration()
        st.rerun()  


class ConfigMemento:
    def __init__(self, nrounds, score_threshold, points_per_round):
        self.nrounds = nrounds
        self.score_threshold = score_threshold
        self.points_per_round = points_per_round
