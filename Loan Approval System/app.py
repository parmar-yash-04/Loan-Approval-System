import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open('Model1.pkl', 'rb'))


def run():
    st.title("🏦 Loan Prediction using ML")

    account_no = st.text_input('Account number')

    fn = st.text_input('Full Name')

    gen_display = ('Female', 'Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])

    mar_display = ('No', 'Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    dep_display = ('No', 'One', 'Two', 'More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents", dep_options, format_func=lambda x: dep_display[x])

    edu_display = ('Not Graduate', 'Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education", edu_options, format_func=lambda x: edu_display[x])

    emp_display = ('Job', 'Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status", emp_options, format_func=lambda x: emp_display[x])

    prop_display = ('Rural', 'Semi-Urban', 'Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area", prop_options, format_func=lambda x: prop_display[x])

    cred_display = ('Between 300 to 500', 'Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score", cred_options, format_func=lambda x: cred_display[x])

    mon_income = st.number_input("Applicant's Monthly Income($)", value=0)

    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", value=0)

    loan_amt = st.number_input("Loan Amount", value=0)

    dur_display = ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration", dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                f"❌ Sorry {fn},\n\nAccount No: {account_no}\n\nYour loan **was not approved**."
            )
        else:
            st.success(
                f"🎉 Congratulations {fn}!\n\nAccount No: {account_no}\n\nYour loan **has been approved**."
    )



run()