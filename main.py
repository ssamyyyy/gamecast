import streamlit as st

st.set_page_config(page_title="GameCastAI", page_icon="🎮")

# --- Page Title ---
st.title("🎮 GameCastAI – Sports Prediction Menu")
st.write("Select a sport to start predictions:")

# --- Menu Buttons ---
col1, col2, col3 = st.columns(3)

with col1:
    football_btn = st.button("⚽ Football")

with col2:
    cricket_btn = st.button("🏏 Cricket")

with col3:
    f1_btn = st.button("🏎 Formula 1")


# --- Display Selected Mode ---
if football_btn:
    st.subheader("⚽ Football Mode Selected")
    st.write("Add football prediction logic here.")
    # Example input:
    team_strength = st.number_input("Team Strength", 0, 100, 80)
    opp_strength = st.number_input("Opponent Strength", 0, 100, 75)
    form = st.number_input("Recent Form (last 5 matches)", 0, 5, 3)
    goals = st.number_input("Average Goals Scored", 0, 5, 2)

    if st.button("Predict Football Result"):
        st.success("⚽ Prediction: Team Win Probability = 65%")
        # Replace with real model prediction


elif cricket_btn:
    st.subheader("🏏 Cricket Mode Selected")
    st.write("Add cricket prediction logic here.")
    # Example inputs:
    run_rate = st.number_input("Run Rate", 0.0, 15.0, 8.2)
    overs = st.number_input("Overs Completed", 0, 50, 12)
    wickets = st.number_input("Wickets Lost", 0, 10, 2)
    pitch = st.number_input("Pitch Rating (1-10)", 1, 10, 7)

    if st.button("Predict Cricket Score"):
        st.success("🏏 Prediction: Expected Total = 178 runs")
        # Replace with real model prediction


elif f1_btn:
    st.subheader("🏎 Formula 1 Mode Selected")
    st.write("Add F1 prediction logic here.")
    # Example inputs:
    rating = st.number_input("Driver Rating", 0, 100, 92)
    car_perf = st.number_input("Car Performance", 0, 100, 88)
    track_diff = st.number_input("Track Difficulty", 1, 10, 6)
    lap = st.number_input("Average Lap Time (s)", 40.0, 120.0, 78.5)

    if st.button("Predict Lap Time"):
        st.success("🏎 Prediction: Lap Time = 77.9 sec")
        # Replace with real model prediction
