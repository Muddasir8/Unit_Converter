import streamlit as st
import time

# Set Streamlit page configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")


# Custom CSS
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        html, body, [class*="st-"] {
            font-family: 'Poppins', sans-serif;
            background-color:rgba(53, 78, 133, 0.74);
            color: white;
            text-align: center;

        }

        .result-box {
            font-size: 22px;
            font-weight: bold;
            padding: 15px;
            border-radius: 10px;
            background: linear-gradient(135deg, #ff7e5f, #feb47b);
            color: white;
            display: inline-block;
            margin-top: 15px;
        }

        .formula-box {
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.1);
            display: inline-block;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Conversion factors & functions
conversion_factors = {
    "Length": {
        "Meters to Kilometers": (0.001, "km = m × 0.001"),
        "Kilometers to Meters": (1000, "m = km × 1000"),
        "Feet to Meters": (0.3048, "m = ft × 0.3048"),
        "Meters to Feet": (3.28084, "ft = m × 3.28084"),
        "Miles to Kilometers": (1.60934, "km = mi × 1.60934"),
        "Kilometers to Miles": (0.621371, "mi = km × 0.621371"),
    },
    "Weight": {
        "Kilograms to Grams": (1000, "g = kg × 1000"),
        "Grams to Kilograms": (0.001, "kg = g × 0.001"),
        "Pounds to Kilograms": (0.453592, "kg = lb × 0.453592"),
        "Kilograms to Pounds": (2.20462, "lb = kg × 2.20462"),
    },
    "Temperature": {
        "Celsius to Fahrenheit": (lambda c: (c * 9/5) + 32, "°F = (°C × 9/5) + 32"),
        "Fahrenheit to Celsius": (lambda f: (f - 32) * 5/9, "°C = (°F - 32) × 5/9"),
    }
}

# Title
st.title("🔄 Unit Converter")

# Select category and conversion type
category = st.selectbox("Select a category", list(conversion_factors.keys()))
conversion_type = st.selectbox("Select conversion", list(conversion_factors[category].keys()))

# Input value 
value = st.number_input("Enter value", format="%.5f", step=0.1)

# Convert button
if st.button("Convert"):
    with st.status("Converting...", expanded=False) as status:
        time.sleep(1)  # Simulate processing time

        conversion_data = conversion_factors[category][conversion_type]
        conversion_formula = conversion_data[1]

        if callable(conversion_data[0]):
            result = conversion_data[0](value)
        else:
            result = value * conversion_data[0]

        status.update(label="", state="complete", expanded=False)

        # Show result and formula
        st.markdown(f'<div class="result-box">🎯 {value} → {round(result, 5)}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="formula-box">📚 Formula: {conversion_formula}</div>', unsafe_allow_html=True)


# Footer
st.markdown("---")
st.markdown("💡 Created with Python using [Streamlit](https://streamlit.io/) 🚀")
st.markdown("---")