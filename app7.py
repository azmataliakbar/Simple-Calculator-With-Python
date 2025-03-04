import streamlit as st

# Set page config - using centered layout which works better with Streamlit's defaults
st.set_page_config(
    page_title="Calculator App",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Define HTML constants to avoid duplication
DIV_END = '</div>'
NUMBER_BTN_START = '<div class="number-btn">'
OPERATION_BTN_START = '<div class="operation-btn">'
CLEAR_BTN_START = '<div class="clear-btn">'
EQUALS_BTN_START = '<div class="equals-btn">'

# Custom CSS that works with Streamlit's default settings
st.markdown("""
<style>
    /* Main container styling */
    .main-container {
        max-width: 100%;
        margin: 0 auto;
        padding: 0;
    }
    
    /* Calculator card */
    .calculator-card {
        background: linear-gradient(145deg, #1e2130, #171b29);
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 10px;
    }
    
    /* Display screen */
    .calculator-display {
        background-color: rgba(0, 0, 0, 0.3);
        color: #ffffff;
        border-radius: 10px;
        padding: 10px 15px;
        margin-bottom: 15px;
        font-size: 24px;
        text-align: right;
        font-family: 'Courier New', monospace;
        border: 1px solid rgba(255, 255, 255, 0.1);
        min-height: 50px;
    }
    
    /* App title */
    .app-title {
        color: #ffffff;
        text-align: center;
        font-size: 24px;
        margin-bottom: 5px;
        font-weight: bold;
    }
    
    /* Calculator title */
    .calculator-title {
        color: #9fa8da;
        text-align: center;
        font-size: 16px;
        margin-bottom: 15px;
    }
    
    /* Reduce default padding in Streamlit */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    
    /* Make columns more compact */
    div[data-testid="column"] {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
        height: 60px; /* Increased height for better touch interaction */
        margin: 2px 0;
        transition: all 0.2s ease;
        border: none !important;
    }
    
    /* Number buttons */
    .number-btn > button {
        background-color: #2d3250 !important;
        color: white !important;
    }
    .number-btn > button:hover {
        background-color: #3d4270 !important;
        transform: translateY(-2px);
    }
    
    /* Operation buttons */
    .operation-btn > button {
        background-color: #ff9800 !important;
        color: white !important;
    }
    .operation-btn > button:hover {
        background-color: #ffb74d !important;
        transform: translateY(-2px);
    }
    
    /* Clear button */
    .clear-btn > button {
        background-color: #f44336 !important;
        color: white !important;
    }
    .clear-btn > button:hover {
        background-color: #ef5350 !important;
        transform: translateY(-2px);
    }
    
    /* Equals button */
    .equals-btn > button {
        background-color: #4caf50 !important;
        color: white !important;
    }
    .equals-btn > button:hover {
        background-color: #66bb6a !important;
        transform: translateY(-2px);
    }
    
    /* History section */
    .history-title {
        color: #9fa8da;
        font-size: 14px;
        margin-top: 10px;
        margin-bottom: 5px;
        text-align: center;
    }
    
    .history-item {
        color: #b0bec5;
        font-size: 12px;
        text-align: right;
        padding: 2px 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #78909c;
        font-size: 12px;
        margin-top: 10px;
    }
    
    /* Mobile optimization */
    @media (max-width: 768px) {
        .main-container {
            max-width: 100%;
        }
        
        .calculator-card {
            padding: 10px;
        }
        
        .calculator-display {
            font-size: 20px;
            min-height: 40px;
            padding: 8px 12px;
        }
        
        .stButton > button {
            height: 50px; /* Adjusted height for mobile */
            font-size: 16px; /* Increased font size for better readability */
        }
        
        .app-title {
            font-size: 20px;
        }
        
        .calculator-title {
            font-size: 14px;
            margin-bottom: 10px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'display' not in st.session_state:
    st.session_state.display = '0'
if 'first_number' not in st.session_state:
    st.session_state.first_number = None
if 'operation' not in st.session_state:
    st.session_state.operation = None
if 'reset_next' not in st.session_state:
    st.session_state.reset_next = False
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to update display
def update_display(value):
    if st.session_state.reset_next or st.session_state.display == '0':
        st.session_state.display = str(value)
        st.session_state.reset_next = False
    else:
        st.session_state.display += str(value)

# Function to handle operations
def handle_operation(op):
    try:
        st.session_state.first_number = float(st.session_state.display)
        st.session_state.operation = op
        st.session_state.reset_next = True
    except ValueError:
        pass

# Helper function to perform calculation
def perform_calculation(first_number, operation, second_number):
    if operation == 'add':
        return first_number + second_number
    elif operation == 'subtract':
        return first_number - second_number
    elif operation == 'multiply':
        return first_number * second_number
    elif operation == 'divide':
        if second_number != 0:
            return first_number / second_number
        return 0
    return 0

# Helper function to get operation symbol
def get_operation_symbol(operation):
    symbols = {
        'add': '+',
        'subtract': '-',
        'multiply': '×',
        'divide': '÷'
    }
    return symbols.get(operation, '')

# Function to calculate result with reduced complexity
def calculate_result():
    if st.session_state.first_number is None or st.session_state.operation is None:
        return
        
    try:
        second_number = float(st.session_state.display)
        operation_symbol = get_operation_symbol(st.session_state.operation)
        
        calculation = f"{st.session_state.first_number} {operation_symbol} {second_number}"
        
        result = perform_calculation(
            st.session_state.first_number,
            st.session_state.operation,
            second_number
        )
        
        # Format result to avoid unnecessary decimal places
        if result == int(result):
            result = int(result)
        
        # Add to history
        st.session_state.history.append(f"{calculation} = {result}")
        if len(st.session_state.history) > 3:  # Keep only last 3 calculations
            st.session_state.history.pop(0)
        
        st.session_state.display = str(result)
        st.session_state.first_number = None
        st.session_state.operation = None
        st.session_state.reset_next = True
    except ValueError:
        pass

# Function to clear calculator
def clear_calculator():
    st.session_state.display = '0'
    st.session_state.first_number = None
    st.session_state.operation = None
    st.session_state.reset_next = False

# Function to handle backspace
def backspace():
    if st.session_state.display != '0' and len(st.session_state.display) > 1:
        st.session_state.display = st.session_state.display[:-1]
    else:
        st.session_state.display = '0'

# Helper function to create a button with styling
def create_button(col, button_text, on_click_func, args=None, key=None, button_type="number"):
    button_types = {
        "number": NUMBER_BTN_START,
        "operation": OPERATION_BTN_START,
        "clear": CLEAR_BTN_START,
        "equals": EQUALS_BTN_START
    }
    
    with col:
        st.markdown(button_types.get(button_type, NUMBER_BTN_START), unsafe_allow_html=True)
        if args:
            st.button(button_text, on_click=on_click_func, args=args, key=key)
        else:
            st.button(button_text, on_click=on_click_func, key=key)
        st.markdown(DIV_END, unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# App title
st.markdown('<div class="app-title">🧮 Simple Calculator �</div>', unsafe_allow_html=True)
st.markdown('<div class="calculator-title">Calculator with History</div>', unsafe_allow_html=True)

# Display
st.markdown(f'<div class="calculator-display">{st.session_state.display}</div>', unsafe_allow_html=True)

# Button rows
# Row 1: Clear and Backspace
col1, col2 = st.columns(2)
create_button(col1, "C", clear_calculator, key="clear", button_type="clear")
create_button(col2, "⌫", backspace, key="backspace", button_type="clear")

# Row 2: 7, 8, 9, ÷
col1, col2, col3, col4 = st.columns(4)
create_button(col1, "7", update_display, args=(7,), key="7")
create_button(col2, "8", update_display, args=(8,), key="8")
create_button(col3, "9", update_display, args=(9,), key="9")
create_button(col4, "÷", handle_operation, args=("divide",), key="divide", button_type="operation")

# Row 3: 4, 5, 6, ×
col1, col2, col3, col4 = st.columns(4)
create_button(col1, "4", update_display, args=(4,), key="4")
create_button(col2, "5", update_display, args=(5,), key="5")
create_button(col3, "6", update_display, args=(6,), key="6")
create_button(col4, "×", handle_operation, args=("multiply",), key="multiply", button_type="operation")

# Row 4: 1, 2, 3, -
col1, col2, col3, col4 = st.columns(4)
create_button(col1, "1", update_display, args=(1,), key="1")
create_button(col2, "2", update_display, args=(2,), key="2")
create_button(col3, "3", update_display, args=(3,), key="3")
create_button(col4, "-", handle_operation, args=("subtract",), key="subtract", button_type="operation")

# Row 5: 0, ., =, +
col1, col2, col3, col4 = st.columns(4)
create_button(col1, "0", update_display, args=(0,), key="0")
create_button(col2, ".", lambda: update_display('.') if '.' not in st.session_state.display else None, key="dot")
create_button(col3, "=", calculate_result, key="equals", button_type="equals")
create_button(col4, "+", handle_operation, args=("add",), key="add", button_type="operation")

# History section
if st.session_state.history:
    st.markdown('<div class="history-title">Recent Calculations</div>', unsafe_allow_html=True)
    for calc in reversed(st.session_state.history):
        st.markdown(f'<div class="history-item">{calc}</div>', unsafe_allow_html=True)

st.markdown(DIV_END, unsafe_allow_html=True)  # Close calculator card

# Footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)

st.markdown(DIV_END, unsafe_allow_html=True)  # Close main container

# Add sidebar navigation (collapsed by default on mobile)
with st.sidebar:
    st.title("Python Apps")
    st.write("Navigate to other apps:")
    
    st.markdown("[🍰 Birthday Greeting](https://birthday-wish.streamlit.app/)")
    st.markdown("[💻 BMI Calculator](https://bmi-calculator2.streamlit.app/)")
    st.markdown("[⏳ Countdown Counter](https://countdown-counter.streamlit.app/)")
    st.markdown("[💱 Currency Converter](https://currency-converter2.streamlit.app/)")
    st.markdown("[🕒 Digital Clock](https://simple-digital-clock.streamlit.app/)")
    st.markdown("[🖼️ File Converter](https://convert-file-into-csv-xlxs-unpmjpc5yezf5bt8jfurgs.streamlit.app/)")