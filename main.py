import suntime
from suntime import Sun
import datetime
import streamlit as st
from datetime import timedelta


sun=Sun(35.534230,139.779020)
sunrise=sun.get_local_sunrise_time()
sunset=sun.get_local_sunset_time()

# タイムゾーンを考慮して時刻を修正
sunrise += datetime.timedelta(hours=9)
sunset += datetime.timedelta(hours=9)

st.write(f"{sunrise.hour}{sunrise.minute}")