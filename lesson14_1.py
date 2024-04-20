from dotenv import dotenv_values
import psycopg2
import os
import streamlit as st
dotenv_values()

def get_contacts() -> list:
    with psycopg2.connect(os.environ['POSTGRE_PASSWORD']) as conn:
        with conn.cursor() as cursor:
            sql='''
             SELECT * from student
            '''
            cursor.execute(sql)
            datas:list = cursor.fetchmany(10)
            contacts =[]
            for item in datas:
                contacts.append({
                    'id':item[0],
                    'name':item[1],
                    'chinese':item[2],
                    'english':item[3],
                    'math':item[4],
                })
            return contacts
        
source_data = get_contacts()
st.dataframe(source_data,width=1200)