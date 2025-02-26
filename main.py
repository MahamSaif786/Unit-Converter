import streamlit as st
import random
import pint
import time

ureg = pint.UnitRegistry()

#  unit categories
unit_categories = {
    "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch", "centimeter", "millimeter", "micrometer", "nanometer", "astronomical_unit", "light_year"],
    "Volume": ["liter", "milliliter", "cubic_meter", "cubic_centimeter", "cubic_inch", "cubic_foot", "gallon", "imperial_gallon", "quart", "pint", "fluid_ounce"],
    "Area": ["millimeter**2", "centimeter**2", "meter**2", "kilometer**2", "hectare", "acre"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour", "centimeter/second", "knot"],
    "Acceleration": ["meter/second**2", "centimeter/second**2", "gravity"],
    "Pressure": ["pascal", "kilopascal", "megapascal", "bar", "millibar", "atmosphere", "torr", "psi"],
    "Energy": ["joule", "kilojoule", "megajoule", "calorie", "kilocalorie", "electronvolt", "watt_hour", "kilowatt_hour"],
    "Power": ["watt", "kilowatt", "megawatt", "horsepower"],
    "Voltage": ["volt", "kilovolt", "millivolt"],
    "Data Size": ["bit", "byte", "kilobit", "kilobyte", "megabit", "megabyte", "gigabit", "gigabyte", "terabit", "terabyte", "petabit", "petabyte"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
}

# Fun Facts
unit_facts = {
    "Length": ["The Great Wall of China is 21,196 km long! 🏯", "A light-year is 9.46 trillion km. ✨", "A human hair is about 100 micrometers wide! 🧑‍🔬"],
    "Area": ["One acre is about 16 tennis courts! 🎾", "The Amazon rainforest covers ~5.5 million km²! 🌳", "The Vatican City is the smallest country, only 0.49 km²! 🏛️"],
    "Volume": ["A human drinks ~1,000 liters of water per year! 💧", "The Pacific Ocean holds 710 million cubic kilometers of water! 🌊", "An Olympic swimming pool contains 2,500,000 liters of water! 🏊‍♂️"],
    "Speed": ["The cheetah can run up to 120 km/h! 🐆", "The speed of sound is 1,235 km/h! 🔊", "The International Space Station orbits Earth at 28,000 km/h! 🚀"],
}

if "history" not in st.session_state:
    st.session_state.history = []

st.set_page_config(page_title="Unit Converter", page_icon="⚡", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>⚡ Unit Converter</h1>", unsafe_allow_html=True)
st.write("### Convert units quickly and easily!")

# Sidebar
st.sidebar.title("📌 Quick Tools")
st.sidebar.subheader("🌍 Conversion History")
if st.session_state.history:
    for h in st.session_state.history[-5:][::-1]:
        st.sidebar.markdown(f"✅ **{h}**")
else:
    st.sidebar.write("No conversions yet!")

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox("Choose a category:", list(unit_categories.keys()))
    from_unit = st.selectbox("Convert from:", unit_categories[category])
    to_unit = st.selectbox("Convert to:", unit_categories[category])
    value = st.number_input("Enter value:", min_value=0.0, format="%.4f")

with col2:
    st.write("### Conversion Result")
    if st.button("Convert 🔄"):
        try:
            result = ureg.Quantity(value, from_unit).to(to_unit).magnitude
            conversion_text = f"{value} {from_unit} = {result:.4f} {to_unit}"
            st.session_state.history.append(conversion_text)

            st.success(f"✅ {conversion_text}")

            # Fun Fact
            st.sidebar.subheader("🎉 Fun Fact!")
            st.sidebar.write(random.choice(unit_facts.get(category, ["Did you know conversions make life easy? 🔢"])))

            # Balloons Animation
            st.balloons()
            time.sleep(1)

        except Exception as e:
            st.error(f"⚠️ Conversion Error: {e}")

st.sidebar.subheader("🚀 Popular Conversions")
popular_conversions = {
    "10 kilometers → miles": (10, "kilometer", "mile"),
    "5 liters → cubic foot": (5, "liter", "cubic_foot"),
    "100 Celsius → Fahrenheit": (100, "celsius", "fahrenheit"),
}

for label, (val, from_u, to_u) in popular_conversions.items():
    if st.sidebar.button(label):
        value, from_unit, to_unit = val, from_u, to_u



# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("✨ **Created by Maham Saif**")








