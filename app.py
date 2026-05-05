import streamlit as st
import pandas as pd
import numpy as np
import datetime
import requests

# --- 1. DATA PREPARATION (Your Hanson Plan) ---
plan_data = {
    'title': "Hansons Beginner Half Marathon",
    'workouts': [
        { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
        { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
        { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
        { 'description': "Easy 3 miles", 'totalDistance': 3 },
        # ... (Include all 126 workouts from your script here)
    ]
}

# --- 2. CLEANING & PROCESSING FUNCTIONS ---
def load_hanson_plan(data):
    df_daily = pd.DataFrame(data['workouts'])
    df_daily['day_idx'] = df_daily.index % 7  # 0=Mon, 1=Tue...
    df_daily['week'] = (df_daily.index // 7) + 1
    
    df_weekly = df_daily.groupby('week').agg({
        'totalDistance': 'sum'
    }).rename(columns={'totalDistance': 'weekly_mileage'}).reset_index()
    
    return df_daily, df_weekly

def get_strava_readiness(c_id, c_secret, r_token):
    """Fetches real data and calculates ACWR"""
    try:
        auth_res = requests.post('https://www.strava.com/oauth/token', data={
            'client_id': c_id, 'client_secret': c_secret,
            'refresh_token': r_token, 'grant_type': 'refresh_token'
        }).json()
        
        access_token = auth_res['access_token']
        header = {'Authorization': f'Bearer {access_token}'}
        res = requests.get("https://www.strava.com/api/v3/athlete/activities", 
                           headers=header, params={'per_page': 28}).json()
        
        df = pd.DataFrame(res)
        df['miles'] = df['distance'] * 0.000621371
        df['date'] = pd.to_datetime(df['start_date_local'])
        
        # Calculate ACWR
        df = df.set_index('date').sort_index()
        acute = df['miles'].rolling('7D').sum().iloc[-1]
        chronic = df['miles'].rolling('28D').sum().iloc[-1] / 4
        return round(acute / chronic, 2) if chronic > 0 else 1.0
    except:
        return 1.0 # Default if API fails

# --- 3. APP UI ---
st.set_page_config(page_title="AI Run Coach", layout="centered")
st.title("🏃‍♂️ AI Hanson Coach")

# SIDEBAR: User Inputs
with st.sidebar:
    st.header("Profile & Goal")
    age = st.number_input("Age", 18, 80, 22)
    gender = st.selectbox("Gender", ["Male", "Female"])
    race_date = st.date_input("Race Date", datetime.date(2026, 11, 1))
    rest_hr = st.number_input("Resting HR", 30, 100, 55)
    
    st.header("Strava Connection")
    client_id = st.text_input("Client ID", type="password")
    client_secret = st.text_input("Client Secret", type="password")
    refresh_token = st.text_input("Refresh Token", type="password")

# --- 4. ENGINE: SCALING & PERSONALIZATION ---
df_daily, df_weekly = load_hanson_plan(plan_data)

# Scaling Factors
weeks_to_race = (race_date - datetime.date.today()).days // 7
age_factor = 1.0 - (max(0, age - 40) * 0.005)
gender_factor = 0.9 if gender == "Female" else 1.0
intensity_mult = 1.2 if weeks_to_race < 12 else 1.0
master_multiplier = age_factor * gender_factor * intensity_mult

# --- 5. DASHBOARD ---
if st.button("Sync Strava & Generate Plan"):
    acwr = get_strava_readiness(client_id, client_secret, refresh_token)
    
    # Readiness logic
    readiness_mult = 0.8 if acwr > 1.3 else 1.0
    
    # Today's Workout Logic
    current_week = max(1, min(18, 18 - weeks_to_race))
    today_idx = datetime.datetime.now().weekday()
    
    today_row = df_daily[(df_daily['week'] == current_week) & (df_daily['day_idx'] == today_idx)].iloc[0]
    final_dist = round(today_row['totalDistance'] * master_multiplier * readiness_mult, 1)

    # UI Metrics
    col1, col2 = st.columns(2)
    col1.metric("Readiness (ACWR)", acwr, delta="Fatigue Detected" if acwr > 1.3 else "Optimal")
    col2.metric("Today's Run", f"{final_dist} Miles")

    st.success(f"**Workout:** {today_row['description']}")
    
    # HR Targets
    max_hr = 211 - (0.64 * age)
    target_hr = round(((max_hr - rest_hr) * 0.65) + rest_hr)
    st.write(f"⏱ **Target Heart Rate:** Keep under {target_hr} BPM")

    # The Roadmap
    st.subheader("Your Personalized Roadmap")
    df_weekly['Scaled'] = df_weekly['weekly_mileage'] * master_multiplier
    st.area_chart(df_weekly.set_index('week')['Scaled'])
