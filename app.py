import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime, date
from khayyam import JalaliDate, TehranTimezone
import calendar

st.set_page_config(initial_sidebar_state="collapsed", page_title="دانشگاه جامع علمی کاربردی خراسان رضوی", page_icon="app/img/uast1.png")

conn = st.connection("gsheets", type=GSheetsConnection)

with open("app/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

st.title("فرم ثبت اطلاعات افراد ملاقات کننده باهمکاران دانشگاه جامع علمی کاربردی واحد استان خراسان رضوی")
st.subheader("مشخصات خود را وارد کنید")


col1, col2 = st.columns(2)

with col1:
    fName = st.text_input(label="نام")
    if not fName:
        st.caption(":red[نام خود را وارد کنید]")
with col2:
    lName = st.text_input(label="نام خانوادگی")
    if not lName:
        st.caption(":red[نام خانوادگی خود را وارد کنید]")


col1, col2 = st.columns(2)

with col1:
    nID = st.text_input(label="کد ملی")
    if not nID:
        st.caption(":red[کد ملی خود را وارد کنید]")
with col2:
    pNumber = st.text_input(label="تلفن تماس")
    if not pNumber:
        st.caption(":red[تلفن تماس خود را وارد کنید]")

address = st.text_area(label="آدرس")
if not address:
    st.caption(":red[آدرس خود را وارد کنید]")

visitDate = JalaliDate(datetime.today().astimezone(TehranTimezone()))
visitDay = calendar.day_name[date.today().weekday()]

submit = st.button("ثبت اطلاعات", use_container_width=True, type="primary")
if submit:
    nID = nID+'"'
    pNumber = pNumber+'"'
    if visitDay != "Monday":
        st.error("فقط روز های دوشنبه ملاقات صورت میگیرد.")
    else:
        if not fName or not lName or not nID or not pNumber or not address:
            st.error("لطفا تمام فیلدها را تکمیل کنید.")
        else:
            # Read data from Google Sheets and add a new row
            df = conn.read(worksheet="Sheet1",ttl=5 , usecols=[0, 1, 2, 3, 4, 5]).dropna(how="all")

            # Convert nID to list
            df_nID = df['کد ملی'].tolist()

            # Check if nID already exists
            if nID in df_nID :
                    st.error("کد ملی وارد شده قبلا ثبت شده است.")
                    st.stop()
            else:
                # Create dictionary
                data = {'نام': fName, 'نام خانوادگی': lName, 'کد ملی': nID, 'تلفن تماس': pNumber, 'آدرس': address, 'تاریخ': visitDate}

                # Convert data to DataFrame
                temp_df = pd.DataFrame([data])

                # Concatenate dataframes
                updated_df = pd.concat([df, temp_df])

                # Update Google Sheets
                conn.update(data=updated_df)

                # Display success message
                st.success("اطلاعات شما با موفقیت ثبت شد.")