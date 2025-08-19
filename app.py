import streamlit as st
import random

# Electron configurations for elements 1–50
elements = {
    1: "1s1", 2: "1s2", 3: "1s2 2s1", 4: "1s2 2s2", 5: "1s2 2s2 2p1",
    6: "1s2 2s2 2p2", 7: "1s2 2s2 2p3", 8: "1s2 2s2 2p4", 9: "1s2 2s2 2p5", 10: "1s2 2s2 2p6",
    11: "1s2 2s2 2p6 3s1", 12: "1s2 2s2 2p6 3s2", 13: "1s2 2s2 2p6 3s2 3p1", 14: "1s2 2s2 2p6 3s2 3p2",
    15: "1s2 2s2 2p6 3s2 3p3", 16: "1s2 2s2 2p6 3s2 3p4", 17: "1s2 2s2 2p6 3s2 3p5", 18: "1s2 2s2 2p6 3s2 3p6",
    19: "1s2 2s2 2p6 3s2 3p6 4s1", 20: "1s2 2s2 2p6 3s2 3p6 4s2",
    21: "1s2 2s2 2p6 3s2 3p6 4s2 3d1", 22: "1s2 2s2 2p6 3s2 3p6 4s2 3d2",
    23: "1s2 2s2 2p6 3s2 3p6 4s2 3d3", 24: "1s2 2s2 2p6 3s2 3p6 4s2 3d5",
    25: "1s2 2s2 2p6 3s2 3p6 4s2 3d5", 26: "1s2 2s2 2p6 3s2 3p6 4s2 3d6",
    27: "1s2 2s2 2p6 3s2 3p6 4s2 3d7", 28: "1s2 2s2 2p6 3s2 3p6 4s2 3d8",
    29: "1s2 2s2 2p6 3s2 3p6 4s1 3d10", 30: "1s2 2s2 2p6 3s2 3p6 4s2",
    31: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1", 32: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2",
    33: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3", 34: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4",
    35: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5", 36: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6",
    37: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1", 38: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2",
    39: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1", 40: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2",
    41: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d3", 42: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d4",
    43: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5", 44: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d7",
    45: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d7", 46: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d8",
    47: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10", 48: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10",
    49: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p1", 50: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p2"
}

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_element" not in st.session_state:
    st.session_state.current_element = random.randint(1, 50)

st.title("Electron Configuration Game (Elements 1–50)")

st.write(f"**Element to configure:** Atomic Number {st.session_state.current_element}")

# Student input
user_input = st.text_input("Write the electron configuration (spdf notation)")

# Check answer
if st.button("Check Answer"):
    correct_config = elements[st.session_state.current_element]
    # Normalize input: remove spaces for comparison
    if user_input.replace(" ", "") == correct_config.replace(" ", ""):
        st.success("✅ Correct!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Incorrect! Correct configuration: {correct_config}")
    
    # Pick a new random element
    st.session_state.current_element = random.randint(1, 50)

st.write(f"Score: {st.session_state.score}")

# Optional: Show hint table
with st.expander("Orbital Capacities Hint"):
    st.write("s = 2 electrons, p = 6 electrons, d = 10 electrons, f = 14 electrons")
