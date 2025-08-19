import streamlit as st
import random

# --- Element Info Sidebar ---
element_names = {
    20: "Calcium", 21: "Scandium", 22: "Titanium", 23: "Vanadium", 24: "Chromium",
    25: "Manganese", 26: "Iron", 27: "Cobalt", 28: "Nickel", 29: "Copper", 30: "Zinc",
    31: "Gallium", 32: "Germanium", 33: "Arsenic", 34: "Selenium", 35: "Bromine",
    36: "Krypton", 37: "Rubidium", 38: "Strontium", 39: "Yttrium", 40: "Zirconium",
    41: "Niobium", 42: "Molybdenum", 43: "Technetium", 44: "Ruthenium", 45: "Rhodium",
    46: "Palladium", 47: "Silver", 48: "Cadmium", 49: "Indium", 50: "Tin"
}

# --- Electron Orbitals Order ---
orbitals_order = [
    {"name": "1s", "max": 2}, {"name": "2s", "max": 2}, {"name": "2p", "max": 6},
    {"name": "3s", "max": 2}, {"name": "3p", "max": 6}, {"name": "4s", "max": 2},
    {"name": "3d", "max": 10}, {"name": "4p", "max": 6}, {"name": "5s", "max": 2},
    {"name": "4d", "max": 10}, {"name": "5p", "max": 6}
]

# --- Special Exceptions for Aufbau ---
exceptions = {
    24: {"3d": 5, "4s": 1},   # Chromium
    29: {"3d": 10, "4s": 1},  # Copper
    42: {"4d": 5, "5s": 1},   # Molybdenum
    47: {"4d": 10, "5s": 1},  # Silver
    41: {"4d": 4, "5s": 1},   # Niobium
    43: {"4d": 5, "5s": 2},   # Technetium
}

# --- Initialize session state ---
if "current" not in st.session_state:
    st.session_state.current = random.randint(20, 50)
if "text_input" not in st.session_state:
    st.session_state.text_input = ""
if "visual_state" not in st.session_state:
    st.session_state.visual_state = {}

st.title("Electron Configuration Game (Atomic numbers 20–50)")

# Sidebar Element Info
atomic_number = st.sidebar.slider("Select Atomic Number", 20, 50, st.session_state.current)
st.sidebar.write(f"Element: **{element_names[atomic_number]}**")
st.sidebar.write(f"Atomic Number: **{atomic_number}**")

# Update session_state when slider changes
if atomic_number != st.session_state.current:
    st.session_state.current = atomic_number
    st.session_state.visual_state = {}
    st.session_state.text_input = ""

# --- Generate correct electron configuration ---
def get_correct_config(Z):
    config = {}
    remaining = Z
    for orb in orbitals_order:
        name = orb["name"]
        if remaining <= 0:
            config[name] = 0
        else:
            electrons = min(orb["max"], remaining)
            config[name] = electrons
            remaining -= electrons
    # Apply exceptions
    if Z in exceptions:
        for k, v in exceptions[Z].items():
            config[k] = v
    return config

correct_config = get_correct_config(st.session_state.current)

# --- Display visual electron input ---
st.subheader("Enter your electron configuration")
visual_inputs = {}
cols = st.columns(len(orbitals_order))
for i, orb in enumerate(orbitals_order):
    visual_inputs[orb["name"]] = cols[i].number_input(
        orb["name"], min_value=0, max_value=orb["max"], value=st.session_state.visual_state.get(orb["name"], 0), step=1
    )
st.session_state.visual_state = visual_inputs

# --- Text input alternative ---
text_input = st.text_input("Or enter configuration (e.g., 1s2 2s2 2p6 ...)", value=st.session_state.text_input)
st.session_state.text_input = text_input

# --- Check Answer ---
def check_answer():
    user_config = {}
    if st.session_state.text_input.strip():
        # parse text input
        try:
            parts = st.session_state.text_input.strip().split()
            for p in parts:
                orb = ''.join(filter(str.isalpha, p))
                e = int(''.join(filter(str.isdigit, p)))
                user_config[orb] = e
        except:
            st.error("Invalid text format. Use e.g., 1s2 2s2 2p6")
            return False
    else:
        user_config = st.session_state.visual_state

    # Compare
    for orb in orbitals_order:
        name = orb["name"]
        if user_config.get(name, 0) != correct_config.get(name, 0):
            st.warning("Incorrect, try again!")
            return False

    st.success("Correct!")
    return True

if st.button("Check Answer"):
    if check_answer():
        # Automatically show next element
        st.session_state.current = random.randint(20, 50)
        st.session_state.visual_state = {}
        st.session_state.text_input = ""

# --- Optional: display correct answer ---
if st.checkbox("Show correct configuration"):
    correct_str = ' '.join(f"{k}{v}" for k, v in correct_config.items() if v > 0)
    st.info(correct_str)

