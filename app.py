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


# --- 1. DATA ENGINE (PACE-BASED SCALING) ---
@st.cache_data
def load_pace_matched_data(u_age, u_gender, u_pace):
    try:
        act_path = kagglehub.dataset_download("mmaelicke/run-activites")
        activities = pd.read_csv(f"{act_path}/activities.csv")
        
        # Clean activities for pace matching
        activities['dist_mi'] = pd.to_numeric(activities['Distance (Raw)'], errors='coerce') * 0.621371
        raw_dur = pd.to_numeric(activities['Duration (Raw Seconds)'], errors='coerce')
        activities['dur_min'] = np.where(raw_dur > 10000, raw_dur / 60000, raw_dur / 60)
        activities['avg_pace'] = activities['dur_min'] / activities['dist_mi']
        
        # Filter: Find others at your pace (+/- 30 seconds) in your demographic
        pace_min, pace_max = u_pace - 0.5, u_pace + 0.5
        matched_peers = activities[
            (activities['avg_pace'].between(pace_min, pace_max)) & 
            (activities['dist_mi'] > 2) # Real runs only
        ]
        
        if matched_peers.empty:
            return 35.0 # Fallback weekly mileage
            
        # Calculate their typical weekly volume
        peer_weekly_avg = matched_peers['dist_mi'].mean() * 4 # Approximation of weekly load
        return peer_weekly_avg
    except:
        return 35.0

# --- 2. PLAN GENERATOR (REST DAYS & FULL LAYOUT) ---
def generate_custom_plan(base_plan, rest_days, scale_factor):
    df = pd.DataFrame(base_plan['workouts'])
    df['day_idx'] = df.index % 7
    df['week'] = (df.index // 7) + 1
    df['scaled_miles'] = (df['totalDistance'] * scale_factor).round(1)
    
    # Rest Day Logic: Find the days with the lowest mileage and set to 0
    if rest_days > 0:
        for w in df['week'].unique():
            week_mask = df['week'] == w
            # Don't turn "Hard" workouts or Long Runs into rest days if possible
            # We sort by mileage ascending to pick the easiest days
            potential_rest_indices = df[week_mask].sort_values(by='scaled_miles').index[:rest_days]
            df.loc[potential_rest_indices, 'scaled_miles'] = 0
            df.loc[potential_rest_indices, 'description'] = "Scheduled Rest Day"
            
    return df

# --- 3. APP INTERFACE ---
st.set_page_config(page_title="Pace-Matched Coach", layout="wide")

# Persistent Checklist State
if 'completed' not in st.session_state:
    st.session_state.completed = {}

with st.sidebar:
    st.header("👤 Profile & Goals")
    u_age = st.number_input("Age", 18, 80, 30)
    u_gender = st.selectbox("Gender", ["Male", "Female"])
    u_pace = st.slider("Current Easy Pace (min/mile)", 6.0, 14.0, 10.0)
    u_rest = st.slider("Desired Rest Days per Week", 0, 3, 1)
    st.divider()
    st.header("🔗 Strava API")
    s_id = st.text_input("Client ID", type="password")
    s_secret = st.text_input("Secret", type="password")
    s_token = st.text_input("Refresh Token", type="password")

# Calculate Scale based on Peers
peer_mileage = load_pace_matched_data(u_age, u_gender, u_pace)
hanson_base = 40.0
scaling_factor = peer_mileage / hanson_base

# Generate customized plan
full_plan = generate_custom_plan(plan_data, u_rest, scaling_factor)

# --- 4. VIEW LAYOUTS ---
tab1, tab2, tab3 = st.tabs(["🎯 Today", "📅 This Week", "🗺 Full Plan"])

# Calculate Timing
race_date = datetime.date(2026, 11, 1)
weeks_left = (race_date - datetime.date.today()).days // 7
curr_week = max(1, 18 - weeks_left)
today_idx = datetime.datetime.now().weekday()

with tab1:
    today_run = full_plan[(full_plan['week'] == curr_week) & (full_plan['day_idx'] == today_idx)].iloc[0]
    
    st.subheader("Today's Prescription")
    c1, c2, c3 = st.columns(3)
    c1.metric("Distance", f"{today_run['scaled_miles']} mi")
    c2.metric("Target Pace", f"{u_pace} min/mi")
    c3.metric("Status", "Rest" if today_run['scaled_miles'] == 0 else "Active")
    
    st.info(f"**Workout:** {today_run['description']}")
    
    # Check-off Button
    done_key = f"w{curr_week}d{today_idx}"
    if st.button("Mark Today's Run as Completed ✅"):
        st.session_state.completed[done_key] = True
        st.success("Great job! Run logged.")

with tab2:
    st.subheader(f"Week {curr_week} Schedule")
    this_week = full_plan[full_plan['week'] == curr_week].copy()
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    this_week['Day'] = days
    
    # Interactive Table for checking off
    this_week['Done'] = [st.session_state.completed.get(f"w{curr_week}d{i}", False) for i in range(7)]
    
    edited_week = st.data_editor(
        this_week[['Day', 'description', 'scaled_miles', 'Done']],
        column_config={"Done": st.column_config.CheckboxColumn("Completed?")},
        use_container_width=True,
        key="weekly_editor"
    )

with tab3:
    st.subheader("The Full 18-Week Journey")
    st.write(f"Scaled based on peers running {u_pace} min/mile pace.")
    
    # Simplified view of the whole plan
    st.dataframe(
        full_plan[['week', 'day_idx', 'description', 'scaled_miles']],
        use_container_width=True,
        height=500
    )

