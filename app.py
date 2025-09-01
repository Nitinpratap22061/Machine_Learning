import streamlit as st
import pickle
import pandas as pd

st.title('IPL Win Predictor')
city = ['Hyderabad', 'Bangalore', 'Indore', 'Mumbai', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'Johannesburg', 'East London', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Kolkata', 'Sharjah', 'Abu Dhabi', 'Ranchi',
       'Pune', 'Raipur', 'Mohali', 'Bengaluru']

teams = ['Royal Challengers Bangalore', 'Delhi Daredevils',
       'Kings XI Punjab', 'Mumbai Indians', 'Sunrisers Hyderabad',
       'Rajasthan Royals', 'Deccan Chargers', 'Chennai Super Kings',
       'Delhi Capitals']

##  req 2 column for batting and balling team selection side by side
col1 , col2 = st.columns(2)

with col1:
    batting_team=st.selectbox('Select the batting team',sorted(teams))

teams1=[]
for team in teams:
   if team not in batting_team:
      teams1.append(team)
with col2:
    bowling_team=st.selectbox("select the bowling team",sorted(teams1))

selected_city = st.selectbox('select the host city',sorted(city))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)
with col3:
   score= st.number_input('score')

with col4:
    overs=st.number_input('over completed')

with col5:
    wickets = st.number_input('wickets-Left')




if st.button('Predict Probability'):


# input jo  le  rhe ho usko transform kro apne dataset model m jo tum le rhe ho bnaye ho
 runs_left = target - score
 balls_left = 120-(overs*6)
 if overs > 0:
  crr=score/overs
 else:
   crr=0
 rrr = runs_left*6/balls_left

 input_df=pd.DataFrame({'batting_team':[batting_team] , 'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'total_runs_x':[target],'wickets_left':[wickets],'crr':[crr],'rrr':[rrr]})
 pipe = pickle.load(open('pipe.pkl', 'rb'))
 result=pipe.predict_proba(input_df)
 loss= result[0][0]
 win= result[0][1]
 st.text(batting_team + " - " + str(round(win*100)) + "%")
 st.text(bowling_team + " - " + str(round(loss*100)) + "%")



