import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Mock Data (Replace with database query)
def get_progress_data():
    return pd.DataFrame({
        "Date": pd.date_range(start="2024-11-01", periods=30),
        "Weight (kg)": [75 - (x * 0.1) for x in range(30)],  # Simulated weight loss
        "Calories Consumed": [2000 - (x * 5) for x in range(30)],
        "Steps": [5000 + (x * 100) for x in range(30)]
    })

def show():
    st.title("Your Progress")
    progress_data = get_progress_data()

    st.markdown("### Weight Progress")
    fig, ax = plt.subplots()
    ax.plot(progress_data["Date"], progress_data["Weight (kg)"], label="Weight (kg)", color="green")
    ax.set_xlabel("Date")
    ax.set_ylabel("Weight (kg)")
    ax.legend()
    st.pyplot(fig)

    st.markdown("### Activity Progress")
    st.line_chart(progress_data[["Calories Consumed", "Steps"]])

    st.markdown("### Weekly Summary")
    weekly_summary = progress_data.resample("W", on="Date").mean()
    st.bar_chart(weekly_summary[["Weight (kg)", "Calories Consumed"]])
