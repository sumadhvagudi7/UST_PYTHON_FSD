"""
Exercise: Build an Interactive Heart Disease Dashboard
Using Matplotlib + Panel
---------------------------------------------------------------
Complete the TODO sections to make the dashboard functional.

"""

# =========================
# 📦 1. Import Libraries
# =========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import panel as pn
import matplotlib
import os

# Set Matplotlib backend for Panel
matplotlib.use('agg')

# Initialize Panel extension (required for widgets)
pn.extension()

# ====
# 📂 2. Load Dataset
# =========================
# TODO: Load 'heart.csv' into a DataFrame
# Example: df = pd.read_csv("heart.csv")
# Read the CSV relative to this script's directory so the script can be run
# from any working directory.
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "heart.csv")
# The CSV includes a leading unnamed index column, so use index_col=0
df = pd.read_csv(csv_path, index_col=0)


# =========================
# 🎛 3. Create Filter Widgets
# =========================
# TODO: Create a RadioButtonGroup for Sex filter
sex_filter = pn.widgets.RadioButtonGroup(
    name="Sex",
    options=["All", "Male", "Female"],
    button_type="success",
    value="All",
)

# TODO: Create a Select widget for Chest Pain Type filter
cp_options = sorted(df["ChestPain"].dropna().unique().tolist())
cp_filter = pn.widgets.Select(
    name="Chest Pain",
    options=["All"] + cp_options,
    value="All",
)


# =========================
# 🔍 4. Define Data Filter Function
# =========================
def filter_data(sex_choice, cp_choice):
    """
    Filters the dataset based on user widget choices.

    Parameters:
    -----------
    sex_choice : str
        "All", "Male", or "Female"
    cp_choice : str
        "All" or one of the Chest Pain categories

    Returns:
    --------
    DataFrame : Filtered data
    """
    # Start with a copy of the DataFrame
    data = df.copy()

    # Filter by Sex (1 = Male, 0 = Female)
    if sex_choice is not None and sex_choice != "All":
        if sex_choice == "Male":
            data = data[data["Sex"] == 1]
        elif sex_choice == "Female":
            data = data[data["Sex"] == 0]

    # Filter by Chest Pain type
    if cp_choice is not None and cp_choice != "All":
        data = data[data["ChestPain"] == cp_choice]

    return data


# =========================
# 📊 5. Define Dashboard Plot Function
# =========================
def plot_dashboard(sex_choice, cp_choice):
    """
    Creates a 2x2 dashboard of charts based on filtered data.
    """
    data = filter_data(sex_choice, cp_choice)

    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    # Chart 1: Age Distribution
    axs[0, 0].hist(data["Age"].dropna(), bins=15, color="#5DA5FF")
    axs[0, 0].set_title("Age Distribution")
    axs[0, 0].set_xlabel("Age")

    # Chart 2: Average Cholesterol by Heart Disease Target
    if not data.empty and "AHD" in data.columns:
        chol_mean = data.groupby("AHD")["Chol"].mean()
        axs[0, 1].bar(chol_mean.index, chol_mean.values, color=["#FFAA33", "#33CC99"])
        axs[0, 1].set_title("Avg Cholesterol by Heart Disease (AHD)")
        axs[0, 1].set_ylabel("Mean Cholesterol")
    else:
        axs[0, 1].text(0.5, 0.5, "No data", ha="center")

    # Chart 3: Resting Blood Pressure Distribution
    axs[1, 0].hist(data["RestBP"].dropna(), bins=15, color="#FFA3B1")
    axs[1, 0].set_title("Resting Blood Pressure Distribution")
    axs[1, 0].set_xlabel("RestBP")

    # Chart 4: Heart Disease Case Counts
    if not data.empty and "AHD" in data.columns:
        counts = data["AHD"].value_counts()
        axs[1, 1].bar(counts.index, counts.values, color=["#6699CC", "#CC6666"])
        axs[1, 1].set_title("Heart Disease Case Counts")
    else:
        axs[1, 1].text(0.5, 0.5, "No data", ha="center")

    # Styling and layout
    plt.tight_layout()
    plt.close(fig)
    return fig


# =========================
# 🖥 6. Create Panel Layout
# =========================
dashboard = pn.Column(
    "# ❤️ Heart Disease Interactive Dashboard (Matplotlib + Panel)",
    pn.Row(sex_filter, cp_filter),
    pn.bind(plot_dashboard, sex_choice=sex_filter, cp_choice=cp_filter)
)

# =========================
# 🚀 7. Run the App
# =========================
# If in Jupyter, display with:
# dashboard

# If running as a standalone web app:
dashboard.servable()
