import streamlit as st

# Set up page config
st.set_page_config(page_title="Calculator", layout="centered")

# Custom CSS for dark theme, card design, and sidebar title alignment
st.markdown("""
    <style>
    /* Global styles */
    body {
        background-color: #0E1117 !important;
        color: white !important;
    }
    .title1 {
    color: red;
    font-size: 25px;
    font-weight: bold;
    text-align: center;
}
    .title2 {
    color: blue;
    font-size: 25px;
    font-weight: bold;
    text-align: center;
}


    
    .stApp {
        background-color: #0E1117 !important;
    }
    
    /* Calculator Card */
    .calculator-card {
        background-color: #262730;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 20px auto;
        max-width: 400px;
        width: 90%; /* Make it responsive on mobile */
    }
    
    /* Display */
    .calculator-display {
        background-color: #1E1E1E;
        color: red !important;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        font-size: 30px; /* Reduced font size for mobile */
        text-align: right;
        border: 2px solid lightgray !important;
        word-break: break-all; /* Prevent overflow */
    }
    
    /* Buttons */
    .stButton button {
        background-color: #363940 !important;
        color: orange !important;
        border: 2px solid lightgray !important;
        border-radius: 8px !important;
        padding: 10px 0px !important; /* Reduced padding for mobile */
        font-size: 1.5rem !important;  /* Reduced font size for mobile */
        font-weight: bold !important;
        margin: 5px !important;
        width: 100% !important;
        height: 50px !important;  /* Reduced height for mobile */
        transition: background-color 0.3s !important;
    }
    
    .stButton button:hover {
        background-color: #4A4D55 !important;
    }
    
    /* Operator buttons */
    .stButton button[data-baseweb="button"]:nth-of-type(4n) {
        background-color: #4CAF50 !important;
    }
    
    .stButton button[data-baseweb="button"]:nth-of-type(4n):hover {
        background-color: #45a049 !important;
    }
    
    /* Result text */
    .result-text {
        color: #02f733;
        font-size: 30px; /* Reduced font size for mobile */
        text-align: center;
        margin-top: 15px;
    }
    
    /* Media Queries for Mobile Devices */
    @media screen and (max-width: 768px) {
        .calculator-card {
            max-width: 100%;
            padding: 10px;
        }
        .calculator-display {
            font-size: 25px;
            padding: 10px;
        }
        .stButton button {
            font-size: 1.2rem !important;
            height: 45px !important;
        }
    }
    
    @media screen and (max-width: 480px) {
        .calculator-display {
            font-size: 20px;
        }
        .stButton button {
            font-size: 1rem !important;
            padding: 5px 0px !important;
            height: 40px !important;
        }
    }
    </style>
""", unsafe_allow_html=True)




st.markdown("<div class='title1'>🐍 Learn Python 🐍</div>", unsafe_allow_html=True)
st.markdown("<div class='title2'>🌠💻 Simple Calculator 🌠💻</div>", unsafe_allow_html=True)

# Sidebar for navigation
def main():
    st.sidebar.markdown("<h2 class='sidebar-title'>🐍 Python Apps 🐍</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<h2 class='sidebar-title'>🔍 Navigate Apps 🔍 :</h2>", unsafe_allow_html=True)
    
    # Use markdown for links instead of buttons for deployment compatibility
    st.sidebar.markdown("<a class='sidebar-link' href='https://birthday-wish.streamlit.app/' target='_blank'>🍰 Birthday Greeting 🍰</a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a class='sidebar-link' href='https://bmi-calculator2.streamlit.app/' target='_blank'>💻 BMI Calculator 💻</a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a class='sidebar-link' href='https://countdown-counter.streamlit.app/' target='_blank'>⏳ Countdown Counter ⏳</a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a class='sidebar-link' href='https://currency-converter2.streamlit.app/' target='_blank'>💱 Currency Converter 💱</a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a class='sidebar-link' href='https://simple-digital-clock.streamlit.app/' target='_blank'>🕒 Digital Clock 🕒</a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a class='sidebar-link' href='https://convert-file-into-csv-xlxs-unpmjpc5yezf5bt8jfurgs.streamlit.app/' target='_blank'>🖼️ File Converter 🖼️</a>", unsafe_allow_html=True)

# Call main to render the sidebar
main()



# Initialize session state
if 'display' not in st.session_state:
    st.session_state.display = '0'
if 'first_number' not in st.session_state:
    st.session_state.first_number = None
if 'operation' not in st.session_state:
    st.session_state.operation = None
if 'reset_next' not in st.session_state:
    st.session_state.reset_next = False

# Function to update display
def update_display(value):
    if st.session_state.reset_next or st.session_state.display == '0':
        st.session_state.display = str(value)
        st.session_state.reset_next = False
    else:
        st.session_state.display += str(value)

# Function to handle operations
def handle_operation(op):
    st.session_state.first_number = float(st.session_state.display)
    st.session_state.operation = op
    st.session_state.reset_next = True

# Function to calculate result
def calculate_result():
    if st.session_state.first_number is not None and st.session_state.operation:
        second_number = float(st.session_state.display)
        if st.session_state.operation == 'add':
            result = st.session_state.first_number + second_number
        elif st.session_state.operation == 'subtract':
            result = st.session_state.first_number - second_number
        elif st.session_state.operation == 'multiply':
            result = st.session_state.first_number * second_number
        elif st.session_state.operation == 'divide':
            if second_number != 0:
                result = st.session_state.first_number / second_number
            else:
                st.error("Cannot divide by zero!")
                result = 0
        
        st.session_state.display = str(result)
        st.session_state.first_number = None
        st.session_state.operation = None
        st.session_state.reset_next = True

# Function to clear calculator
def clear_calculator():
    st.session_state.display = '0'
    st.session_state.first_number = None
    st.session_state.operation = None
    st.session_state.reset_next = False

# Calculator card
with st.container():
    # Display
    st.markdown(f'<div class="calculator-display">{st.session_state.display}</div>', unsafe_allow_html=True)
    
    # Calculator buttons
    cols = st.columns(4)
    
    # Row 1
    cols[0].button('7', on_click=update_display, args=(7,))
    cols[1].button('8', on_click=update_display, args=(8,))
    cols[2].button('9', on_click=update_display, args=(9,))
    cols[3].button('DIVIDE', on_click=handle_operation, args=('divide',))
    
    # Row 2
    cols[0].button('4', on_click=update_display, args=(4,))
    cols[1].button('5', on_click=update_display, args=(5,))
    cols[2].button('6', on_click=update_display, args=(6,))
    cols[3].button('MULTIPLY', on_click=handle_operation, args=('multiply',))
    
    # Row 3
    cols[0].button('1', on_click=update_display, args=(1,))
    cols[1].button('2', on_click=update_display, args=(2,))
    cols[2].button('3', on_click=update_display, args=(3,))
    cols[3].button('SUBTRACT', on_click=handle_operation, args=('subtract',))
    
    # Row 4
    cols[0].button('0', on_click=update_display, args=(0,))
    cols[1].button('.', on_click=lambda: update_display('.') if '.' not in st.session_state.display else None)
    cols[2].button('=', on_click=calculate_result)
    cols[3].button('ADD', on_click=handle_operation, args=('add',))
    
    # Clear button
    st.button('Clear', on_click=clear_calculator)
