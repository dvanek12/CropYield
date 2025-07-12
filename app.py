app.py
import streamlit as st
import pandas as pd

# Title and description
st.title("Farm Hedge Helper")
st.write("""
This tool helps farmers calculate their breakeven price per bushel
and compare it to the current hedgeable price using futures and basis.
""")

# Collect user inputs
st.header("Input Your Farm Information")
yield_per_acre = st.number_input("Expected yield per acre (bushels)", min_value=0.0, value=180.0)
total_acres = st.number_input("Total acres", min_value=0.0, value=100.0)
total_costs = st.number_input("Total costs ($)", min_value=0.0, value=50000.0)
current_futures_price = st.number_input("Current futures price ($/bushel)", min_value=0.0, value=5.50)
basis = st.number_input("Local basis ($/bushel, usually negative)", value=-0.20)

# Calculations
total_yield = yield_per_acre * total_acres
breakeven_price = total_costs / total_yield if total_yield != 0 else 0
hedgeable_price = current_futures_price + basis
profit_per_bushel = hedgeable_price - breakeven_price
total_profit = profit_per_bushel * total_yield

# Display Results
st.header("Results")
st.write(f"**Total Expected Yield:** {total_yield:,.2f} bushels")
st.write(f"**Breakeven Price:** ${breakeven_price:,.2f} per bushel")
st.write(f"**Current Hedgeable Price:** ${hedgeable_price:,.2f} per bushel")
st.write(f"**Profit per Bushel:** ${profit_per_bushel:,.2f}")
st.write(f"**Total Projected Profit at Current Hedge:** ${total_profit:,.2f}")

# Simple bar chart
chart_df = pd.DataFrame({
    "Price": [breakeven_price, hedgeable_price]
}, index=["Breakeven", "Hedgeable"])
st.bar_chart(chart_df)
