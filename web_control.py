import streamlit as st
from mqtt_func import *

# Define a function to be executed when a button is pressed
def on_button_press(button_number, button_name):
    print(f"Button '{button_name}' pressed!")


    # Increment the count for the specific button
    st.session_state[f'count_{button_number}'] += 1
    # Determine message based on count and button number
    message = (button_number * 2) - 1 + st.session_state[f'count_{button_number}']
    # Send message
    publish_data("eyantra", str(int(message - 1)))
    # Reset the count after sending the second message
    if st.session_state[f'count_{button_number}'] == 2:
        st.session_state[f'count_{button_number}'] = 0

# Initialize counts using session_state
for button_number in range(1, 5):
    if f'count_{button_number}' not in st.session_state:
        st.session_state[f'count_{button_number}'] = 0

# Add a title above the buttons
# st.title("Eyantra Lab Automation")

# Center-align the title
st.markdown("<h1 style='text-align: center;'>Eyantra Lab Automation</h1>", unsafe_allow_html=True)

# Define CSS for styling the buttons
button_style = """
    <style>
        .stButton>button {
            width: 200px;  /* Adjust the width as needed */
            height: 50px;  /* Adjust the height as needed */
            font-size: 18px;
            margin: auto;  /* Center-align the button */
            display: block;  /* Make the button a block element */
        }
    </style>
"""

# Apply the CSS for button styling
st.markdown(button_style, unsafe_allow_html=True)

# Create Streamlit buttons with names
button_names = ["light", "cubical Fan", "   Cubical Light  ", "  Fan  "]
for button_number, button_name in enumerate(button_names, start=1):
    if st.button(button_name):
        on_button_press(button_number, button_name)
