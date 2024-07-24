import streamlit as st
from datetime import datetime, date
from khayyam import JalaliDate, TehranTimezone
import calendar

st.title("date time test")

st.write(JalaliDate(datetime.now(TehranTimezone())))

my_date = date.today()
st.write(calendar.day_name[my_date.weekday()])