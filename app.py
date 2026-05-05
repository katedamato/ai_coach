import streamlit as st
import pandas as pd
import datetime
import requests
import numpy as np

# --- 1. DATA & CONSTANTS ---
# (Keep your plan_data dictionary here)

def load_and_scale_plan(data, age, gender, weeks_to_race):
    df = pd.DataFrame(data['workouts'])
    df['day_idx'] = df.index % 7
    df['week'] = (df.index // 7) + 1
    
    # Scaling Logic
    age_f = 1.0 - (max(0, age - 40) * 0.005)
    gen_f = 0.9 if gender == "Female" else 1.0
    time_f = 1.2 if weeks_to_race < 12 else 1.0
    master_mult = age_f * gen_f * time_f
    
    df['scaled_miles'] = (df['totalDistance'] * master_mult).round(2)
    return df, master_mult

# --- 2. HR ZONE LOGIC (Karvonen Formula) ---
def get_hr_zones(age, resting_hr):
    max_hr = 211 - (0.64 * age)
    hrr = max_hr - resting_hr
    zones = {
        "Easy (Recovery)": (f"{int(hrr * 0.60 + resting_hr)}-{int(hrr * 0.70 + resting_hr)} BPM"),
        "Moderate (Aerobic)": (f"{int(hrr * 0.70 + resting_hr)}-{int(hrr * 0.80 + resting_hr)} BPM"),
        "Hard (Tempo)": (f"{int(hrr * 0.80 + resting_hr)}-{int(hrr * 0.90 + resting_hr)} BPM")
    }
    return zones

# --- 3. APP INTERFACE ---
st.set_page_config(page_title="AI Coach", layout="wide")
st.title("🏃‍♂️ Hanson AI Dashboard")

# Sidebar Configuration
with st.sidebar:
    st.header("Personal Data")
    age = st.number_input("Age", 18, 80, 22)
    gender = st.selectbox("Gender", ["Male", "Female"])
    rest_hr = st.number_input("Resting HR (from Watch/Strava)", 30, 100, 55)
    race_date = st.date_input("Race Date", datetime.date(2026, 11, 1))

# Initialize Plan
weeks_left = (race_date - datetime.date.today()).days // 7
df_plan, multiplier = load_and_scale_plan(plan_data, age, gender, weeks_left)
current_week_num = max(1, min(18, 18 - weeks_left))

# --- 4. TODAY'S VIEW ---
st.subheader("📍 Today's Prescription")
today_idx = datetime.datetime.now().weekday()
today_data = df_plan[(df_plan['week'] == current_week_num) & (df_plan['day_idx'] == today_idx)].iloc[0]

# Mocking Strava ACWR for display - (Replace with your actual Strava function call)
acwr = 1.15 
adj = 0.8 if acwr > 1.3 else 1.0

col1, col2, col3 = st.columns(3)
col1.metric("Distance", f"{round(today_data['scaled_miles'] * adj, 2)} mi", delta=f"{adj*100}% Load")
col2.metric("Target Zone", "Hard (Tempo)" if "HMP" in today_data['description'] else "Easy")
col3.metric("Status", "🟢 Optimal" if adj == 1.0 else "🟡 Fatigue Warning")

st.info(f"**Workout:** {today_data['description']}")

# --- 5. WEEKLY CHECKLIST ---
st.divider()
st.subheader(f"📅 Week {current_week_num} Schedule")

# Filter for current week
weekly_view = df_plan[df_plan['week'] == current_week_num][['day_idx', 'description', 'scaled_miles']].copy()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekly_view['Day'] = [days[i] for i in weekly_view['day_idx']]
weekly_view['Done'] = False # Initial state

# Interactive Table with Checkboxes
edited_df = st.data_editor(
    weekly_view[['Day', 'description', 'scaled_miles', 'Done']],
    column_config={
        "Done": st.column_config.CheckboxColumn("Completed?", default=False),
        "scaled_miles": "Miles",
        "description": "Workout Details"
    },
    disabled=["Day", "description", "scaled_miles"],
    hide_index=True,
)

# --- 6. HR ZONES & FULL PLAN ---
st.divider()
tab1, tab2 = st.tabs(["💓 Heart Rate Zones", "🗺 Full 18-Week Roadmap"])

with tab1:
    zones = get_hr_zones(age, rest_hr)
    st.table(pd.DataFrame(zones.items(), columns=["Zone", "Range"]))

with tab2:
    st.write("Full training progression scaled to your profile:")
    st.dataframe(df_plan[['week', 'day_idx', 'description', 'scaled_miles']], height=400)
