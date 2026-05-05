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

# --- 1. DATA LOADING & CLEANING ---
@st.cache_data
def load_and_refine_data(u_age, u_gender):
    # Download Kaggle Files
    act_path = kagglehub.dataset_download("mmaelicke/run-activites")
    out_path = kagglehub.dataset_download("likithagedipudi/run-club-marathon-performance-dataset")
    
    activities = pd.read_csv(f"{act_path}/activities.csv")
    outcomes = pd.read_csv(f"{out_path}/train.csv")

    # Clean Activities (from your previous logic)
    activities['miles'] = pd.to_numeric(activities['Distance (Raw)'], errors='coerce') * 0.621371
    raw_dur = pd.to_numeric(activities['Duration (Raw Seconds)'], errors='coerce')
    activities['min'] = np.where(raw_dur > 10000, raw_dur / 60000, raw_dur / 60)
    activities['pace'] = activities['min'] / activities['miles']
    
    # Matching Logic: Find top 10% performers in user's demographic
    demo_outcomes = outcomes[(outcomes['age'] >= u_age - 5) & 
                             (outcomes['age'] <= u_age + 5) & 
                             (outcomes['gender'] == u_gender)]
    
    # Get the "High Performance" threshold (e.g., top 25% finish times)
    perf_threshold = demo_outcomes['performance_score'].quantile(0.75) 
    top_performers = demo_outcomes[demo_outcomes['performance_score'] >= perf_threshold]
    
    # Derive "Ideal" mileage and conditions
    avg_top_mileage = top_performers['weekly_mileage'].mean()
    common_conditions = top_performers['weather_condition'].mode()[0]
    
    return avg_top_mileage, common_conditions, activities

# --- 2. STRAVA API (Zones & Pace) ---
def get_strava_bio_data(c_id, c_secret, r_token):
    auth_url = "https://www.strava.com/oauth/token"
    res = requests.post(auth_url, data={'client_id': c_id, 'client_secret': c_secret, 'refresh_token': r_token, 'grant_type': 'refresh_token'}).json()
    access_token = res['access_token']
    
    # Get Athlete Zones (Heart Rate & Pace)
    header = {'Authorization': f'Bearer {access_token}'}
    zones = requests.get("https://www.strava.com/api/v3/athlete/zones", headers=header).json()
    
    # Get recent activity for baseline pace
    recent = requests.get("https://www.strava.com/api/v3/athlete/activities", headers=header, params={'per_page': 5}).json()
    avg_pace = pd.DataFrame(recent)['average_speed'].mean() * 2.23694 # m/s to mph then converted to pace
    return zones, (60 / avg_pace)

# --- 3. APP UI & ADJUSTMENT LOGIC ---
st.title("🏃‍♂️ Hanson AI: Podium-Optimized Coach")

with st.sidebar:
    u_age = st.number_input("Age", 18, 80, 25)
    u_gender = st.selectbox("Gender", ["Male", "Female"])
    st.divider()
    s_id = st.text_input("Strava Client ID", type="password")
    s_secret = st.text_input("Strava Secret", type="password")
    s_token = st.text_input("Strava Refresh Token", type="password")

# Execute Kaggle Insight
ideal_mileage, best_weather, clean_act = load_and_refine_data(u_age, u_gender)

# Initialize Session Data
if st.button("Sync & Personalize Plan"):
    s_zones, s_pace = get_strava_bio_data(s_id, s_secret, s_token)
    st.session_state['s_zones'] = s_zones
    st.session_state['s_pace'] = s_pace
    st.success("Biological Calibration Complete.")

# --- 4. THE ADJUSTED SCHEDULE ---
st.subheader("Your High-Performance Plan")
st.write(f"💡 *Insights:* Top performers in your demographic focus on **{int(ideal_mileage)} miles/week** and thrive in **{best_weather}** conditions.")

# Map Strava Zones to Plan
hr_zones = st.session_state.get('s_zones', {}).get('heart_rate', {}).get('zones', [])
pace_zones = st.session_state.get('s_zones', {}).get('pace', {}).get('zones', [])

def get_zone_label(desc):
    if "HMP" in desc: return "Zone 4 (Threshold)"
    if "Easy" in desc: return "Zone 2 (Aerobic)"
    return "Zone 1 (Recovery)"

# Display today's detail
weeks_to_race = (datetime.date(2026, 11, 1) - datetime.date.today()).days // 7
curr_week = 18 - weeks_to_race
today_idx = datetime.datetime.now().weekday()

# Base logic: Scale current mileage toward the 'ideal_mileage' found in Outcomes
# If Base Plan says 30mpw but Kaggle Podium says 45mpw, we adjust the scale.
adjustment_factor = ideal_mileage / 40 # Assuming 40 is standard base

plan_df = pd.DataFrame(plan_data['workouts'])
plan_df['scaled_miles'] = (plan_df['totalDistance'] * adjustment_factor).round(1)

st.write(f"### Today's Goal: {plan_df.iloc[today_idx]['scaled_miles']} Miles")
st.metric("Target Heart Rate", hr_zones[1]['max'] if hr_zones else "145 BPM", "Easy Pace")
st.info(f"**Strategy:** {plan_df.iloc[today_idx]['description']}")
