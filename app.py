import streamlit as st
import pandas as pd
import datetime
import requests
import numpy as np

plan_data = {
  'id': "1f16b01b-3dd4-498b-96b8-17b6c304288b",
  'title': "Hansons Beginner Half Marathon",
  'workouts': [
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "Easy 3 miles",
      'totalDistance': 3,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "Easy 3 miles",
      'totalDistance': 3,
    },
    {
      'description': "Easy 4 miles",
      'totalDistance': 4,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "Easy 2 miles",
      'totalDistance': 2,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "Easy 3 miles",
      'totalDistance': 3,
    },
    {
      'description': "Easy 3 miles",
      'totalDistance': 3,
    },
    {
      'description': "Easy 3 miles",
      'totalDistance': 3,
    },
    {
      'description': "Easy 4 miles",
      'totalDistance': 4,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "Easy 4 miles",
      'totalDistance': 4,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "Easy 4 miles",
      'totalDistance': 4,
    },
    {
      'description': "Easy 4 miles",
      'totalDistance': 4,
    },
    {
      'description': "Easy 4 miles",
      'totalDistance': 4,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "Easy 3 miles",
      'totalDistance': 3,
    },
    {
      'description': "Easy 3 miles",
      'totalDistance': 3,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "1.5 miles Warm Up\n3 miles @ HMP\n1.5 miles Cool Down",
      'totalDistance': 6,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "Easy 4 miles",
      'totalDistance': 4,
    },
    {
      'description': "8 miles Long Run",
      'totalDistance': 8,
    },
    {
      'description': "Easy 4 miles",
      'totalDistance': 4,
    },
    {
      'description':
        "1.5 miles Warm Up\n12x400m @ 5k-10k pace w. 400m jog rest\n1.5 miles Cool Down",
      'totalDistance': 9,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "1.5 miles Warm Up\n3 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 6,
    },
    {
      'description': "Easy 4 miles",
      'totalDistance': 4,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "9 miles Long Run",
      'totalDistance': 9,
    },
    {
      'description': "Easy 4 miles",
      'totalDistance': 4,
    },
    {
      'description':
        "1.5 miles Warm Up\n8x600m @ 5k-10k pace w. 400m jog rest\n1.5 miles Cool Down",
      'totalDistance': 7,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "1.5 miles Warm Up\n3 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 6,
    },
    {
      'description': "Easy 4 miles",
      'totalDistance': 4,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description': "10 miles Long Run",
      'totalDistance': 0,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description':
        "1.5 miles Warm Up\n6x800m @ 5k-10k pace w. 400m jog rest\n1.5 miles Cool Down",
      'totalDistance': 7,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "1.5 miles Warm Up\n4 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 7,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description': "10 miles Long Run",
      'totalDistance': 10,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description':
        "1.5 miles Warm Up\n5x1k @ 5k-10k pace w. 600m jog rest\n1.5 miles Cool Down",
      'totalDistance': 8,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "1.5 miles Warm Up\n4 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 7,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "10 miles Long Run",
      'totalDistance': 10,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description':
        "1.5 miles Warm Up\n4x1,200m @ 5k-10k pace w. 600m jog rest\n1.5 miles Cool Down",
      'totalDistance': 8,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance': 0 },
    {
      'description': "1.5 miles Warm Up\n4 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 7,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "12 miles Long Run",
      'totalDistance': 12,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description':
        "1.5 miles Warm Up\n6x1 miles @ HMP -10s w. 400m jog rest\n1.5 miles Cool Down",
      'totalDistance': 10,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance' : 0 },
    {
      'description': "1.5 miles Warm Up\n5 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 8,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "10 miles Long Run",
      'totalDistance': 10,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description':
        "1.5 miles Warm Up\n4x1.5 miles @ HMP -10s w. 800m jog rest\n1.5 miles Cool Down",
      'totalDistance': 10,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance' : 0 },
    {
      'description': "1.5 miles Warm Up\n5 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 8,
    },  
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description': "12 miles Long Run",
      'totalDistance': 12,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description':
        "1.5 miles Warm Up\n3x2 miles @ HMP -10s w. 800m jog rest\n1.5 miles Cool Down",
      'totalDistance': 10,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance' : 0 },
    {
      'description': "1.5 miles Warm Up\n5 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 8,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "10 miles Long Run",
      'totalDistance': 10,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description':
        "1.5 miles Warm Up\n2x3 miles @ HMP -10s w. 1 miles jog rest\n1.5 miles Cool Down",
      'totalDistance': 10,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance' : 0 },
    {
      'description': "1.5 miles Warm Up\n6 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 9,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description': "12 miles Long Run",
      'totalDistance': 12,
    },
    {
      'description': "Easy 7 miles",
      'totalDistance': 7,
    },
    {
      'description':
        "1.5 miles Warm Up\n3x2 miles @ HMP -10s w. 800m jog rest\n1.5 miles Cool Down",
      'totalDistance': 10,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance' : 0 },
    {
      'description': "1.5 miles Warm Up\n6 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 9,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "10 miles Long Run",
      'totalDistance': 10,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description':
        "1.5 miles Warm Up\n4x1.5 miles @ HMP -10s w. 800m jog rest\n1.5 miles Cool Down",
      'totalDistance': 10,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance' : 0 },
    {
      'description': "1.5 miles Warm Up\n6 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 9,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description': "12 miles Long Run",
      'totalDistance': 12,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description':
        "1.5 miles Warm Up\n6x1 miles @ HMP -10s w. 400m jog rest\n1.5 miles Cool Down",
      'totalDistance': 10,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance' : 0 },
    {
      'description': "1.5 miles Warm Up\n5 miles@ HMP\n1.5 miles Cool Down",
      'totalDistance': 8,
    },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "Easy 8 miles",
      'totalDistance': 8,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    { 'description': "Rest or Cross-Train", 'totalDistance' : 0 },
    {
      'description': "Easy 6 miles",
      'totalDistance': 6,
    },
    {
      'description': "Easy 5 miles",
      'totalDistance': 5,
    },
    {
      'description': "Easy 3 miles",
      'totalDistance': 3,
    },
    { 'description': "Race Day!", 'totalDistance': 13.1 },
  ],
} 

import streamlit as st
import pandas as pd
import numpy as np
import datetime
import requests
import kagglehub

# --- 1. DATA LOADING & ROBUST CLEANING ---
@st.cache_data
def load_and_refine_data(u_age, u_gender):
    try:
        # Download Kaggle Files
        act_path = kagglehub.dataset_download("mmaelicke/run-activites")
        out_path = kagglehub.dataset_download("likithagedipudi/run-club-marathon-performance-dataset")
        
        activities = pd.read_csv(f"{act_path}/activities.csv")
        outcomes = pd.read_csv(f"{out_path}/train.csv") # This is the marathon results file

        # Clean Activities (Kaggle Dataset 1)
        activities['miles'] = pd.to_numeric(activities['Distance (Raw)'], errors='coerce') * 0.621371
        raw_dur = pd.to_numeric(activities['Duration (Raw Seconds)'], errors='coerce')
        activities['min'] = np.where(raw_dur > 10000, raw_dur / 60000, raw_dur / 60)
        
        # Demographic Matching (Kaggle Dataset 2: Outcomes)
        # We look for people similar to you
        demo_mask = (outcomes['age'].between(u_age-5, u_age+5)) & (outcomes['gender'].str.lower() == u_gender.lower())
        demo_outcomes = outcomes[demo_mask]

        if demo_outcomes.empty:
            return 40.0, "Cool", activities # Fallback defaults

        # Identify 'High Performance' (The fastest 25% of your demographic)
        # Using 'finish_time' because 'performance_score' was missing
        time_col = 'finish_time' if 'finish_time' in outcomes.columns else outcomes.columns[1] 
        perf_threshold = demo_outcomes[time_col].quantile(0.25) 
        top_performers = demo_outcomes[demo_outcomes[time_col] <= perf_threshold]
        
        # Derive Ideal Mileage (Looking at what the fast people in your age group do)
        # Note: If 'weekly_mileage' is missing, we use a calculated baseline
        mile_col = 'weekly_mileage' if 'weekly_mileage' in outcomes.columns else 'mileage'
        avg_top_mileage = top_performers[mile_col].mean() if mile_col in top_performers.columns else 45.0
        
        return avg_top_mileage, "Optimal", activities
    except Exception as e:
        st.error(f"Data Alignment Error: {e}")
        return 40.0, "Variable", pd.DataFrame()

# --- 2. STRAVA BIO-DATA FETCH ---
def get_strava_bio_data(c_id, c_secret, r_token):
    try:
        auth_url = "https://www.strava.com/oauth/token"
        res = requests.post(auth_url, data={
            'client_id': c_id, 'client_secret': c_secret, 
            'refresh_token': r_token, 'grant_type': 'refresh_token'
        }).json()
        access_token = res['access_token']
        header = {'Authorization': f'Bearer {access_token}'}
        
        # Get Athlete Zones (Heart Rate and Pace)
        zones = requests.get("https://www.strava.com/api/v3/athlete/zones", headers=header).json()
        return zones
    except Exception as e:
        st.warning("Could not connect to Strava. Using base HR formulas.")
        return None

# --- 3. UI & COACHING ENGINE ---
st.set_page_config(page_title="AI Podium Coach", layout="wide")
st.title("🏆 AI Hanson Coach")

with st.sidebar:
    st.header("1. Personal Specs")
    u_age = st.number_input("Age", 18, 80, 25)
    u_gender = st.selectbox("Gender", ["Male", "Female"])
    u_rest_hr = st.number_input("Resting HR", 30, 100, 55)
    
    st.header("2. Strava Link")
    s_id = st.text_input("Client ID", type="password")
    s_secret = st.text_input("Secret", type="password")
    s_token = st.text_input("Refresh Token", type="password")
    
    sync = st.button("Sync Biological Data")

# Load Global Insights
ideal_mileage, cond, activities = load_and_refine_data(u_age, u_gender)

# Session State for Strava
if sync:
    st.session_state['zones'] = get_strava_bio_data(s_id, s_secret, s_token)

# --- 4. THE ADJUSTED PLAN ---
# Baseline Hanson Week (Simplified for example)
hanson_base_mileage = 35.0 
# Scaling Factor: Ratio of what elites in your demo do vs base plan
scaling_factor = ideal_mileage / hanson_base_mileage if ideal_mileage > 0 else 1.0

st.info(f"📊 **Data Insight:** High-performers in the {u_age}yo {u_gender} demographic average **{ideal_mileage:.1f} miles/week**. Your plan has been scaled by **{scaling_factor:.2f}x** to match.")

# Get Today's Workout from JSON (Mocking a row for logic)
today_base_dist = 6.0 
today_desc = "6 miles Easy Run with 4x100m Strides"
scaled_dist = round(today_base_dist * scaling_factor, 1)

# Zone Calculation
strava_zones = st.session_state.get('zones')
if strava_zones and 'heart_rate' in strava_zones:
    # Use real Strava Zone 2 for Easy, Zone 4 for Tempo
    z2 = strava_zones['heart_rate']['zones'][1]
    z4 = strava_zones['heart_rate']['zones'][3]
    target_hr = f"{z2['min']} - {z2['max']} BPM" if "Easy" in today_desc else f"{z4['min']} - {z4['max']} BPM"
else:
    # Fallback Karvonen
    max_hr = 211 - (0.64 * u_age)
    target_hr = f"{int((max_hr-u_rest_hr)*0.6 + u_rest_hr)} BPM (Generic)"

# Dashboard
col1, col2, col3 = st.columns(3)
col1.metric("Today's Distance", f"{scaled_dist} mi")
col2.metric("Target HR", target_hr)
col3.metric("Demo Peak Mileage", f"{int(ideal_mileage)} mpw")

st.success(f"**Workout:** {today_desc}")

# --- 5. WEEKLY VIEW & CHECKLIST ---
st.divider()
st.subheader("This Week's Schedule")

# Creating a mock weekly dataframe for demonstration
week_data = pd.DataFrame({
    'Day': ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    'Workout': ["Easy Run", "Strength", "Tempo Run", "Easy Run", "Rest", "Long Run", "Easy Run"],
    'Base Miles': [6, 0, 8, 6, 0, 10, 6],
    'Done': [False] * 7
})
week_data['Scaled Miles'] = (week_data['Base Miles'] * scaling_factor).round(1)

st.data_editor(
    week_data[['Day', 'Workout', 'Scaled Miles', 'Done']],
    column_config={"Done": st.column_config.CheckboxColumn("Completed?")},
    use_container_width=True,
    disabled=["Day", "Workout", "Scaled Miles"]
)
