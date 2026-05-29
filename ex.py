import streamlit as st
import pandas as pd

# Initialize the expense dataframe
if 'expenses'  not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['Company name','Customer name', 'Policy expiry date', 'Month','Policy no','Model code',
                                                      'Engine no','Chassis no','Vehicle idv','Invoice date','Vehicle class','Age','Mfg Year','Vehicle registration no','Full type','Collection date ','Reference'])
def add_expense(category1,description1,date1,month,description2,category2,box1,box2,box3,date2,category3,category4,date3,box4,category5,date4,re):
    new_expense = pd.DataFrame([[category1,description1,date1,month,description2,category2,box1,box2,box3,date2,category3,category4,date3,box4,category5,date4,re]], columns=st.session_state.expenses.columns)
    st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)


st.title('TOYOTA')

with st.sidebar:
    st.header('Customer Information')
    category1 = st.selectbox('Company name', ['Cholamandalam MS General Insurance Co. Ltd.', 'BAJAJ GENERAL INSURANCE LIMITED', 'SBI General Insurance Company Limited',
                                             'Reliance General Insurance Co.Ltd.', 'ICICI Lombard General Insurance Company Limited','IFFCO Tokio General Insurance Co. Ltd.','The New India Assurance Co. Ltd.'])
    description1 = st.text_input('Customer name')
    date1= st.date_input('Policy expiry date')
    month=st.selectbox('Month',['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    description2 = st.text_input('Policy no')
    category2=st.selectbox('Model code',['FORTUNER','GLANZA','INNOVA','RUMION','URBAN CRUISER HYRYDER',
                                        'INNOVA HYCROSS','URBAN CRUISER TAISOR','ETIOS CROSS'])
    box1=st.text_input('Engine no')
    box2=st.text_input('Chassis no')
    box3=st.text_input('Vehicle idv')
    date2=st.date_input('Invoice date')
    category3=st.selectbox('Vehicle class',['private','commercial'])
    category4=st.selectbox('Age',['first ren','second ren','third ren','fourth ren','fifth ren','sixth ren','seventh ren','eighth ren','nineth ren','tenth ren','tenth ren and above'])
    date3=st.selectbox('Mfg Year',['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030'])
    box4=st.text_input('Vehicle registration no')
    category5=st.selectbox('Full type',['Diesel','Petrol','Hybrid'])
    date4=st.date_input('Collection date')
    re=st.text_input('Reference')
    if st.button('Add'):
        add_expense(category1,description1,date1,month,description2,category2,box1,box2,box3,date2,category3,category4,date3,box4,category5,date4,re)
        st.success('Data added!')

   
st.header('Data Sheet')
st.write(st.session_state.expenses)

