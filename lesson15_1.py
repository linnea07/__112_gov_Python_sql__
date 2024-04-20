from dotenv import load_dotenv
import psycopg2
import os
import streamlit as st
load_dotenv()

def getCity()->list[str]:
    with psycopg2.connect(os.environ['POSTGRE_PASSWORD']) as conn:
        with conn.cursor() as curcsor:
            sql=''' 
                SELECT DISTINCT SUBSTRING(地址,1,3) AS conuty
                FROM station;
            '''
            curcsor.execute(sql)
            queryDatas:list[tuple[str]]=curcsor.fetchall
            city_name:list[str] = [item[0] for item in queryDatas]
            return city_name
        
# def getStation(city_name:str)->list[str]:
#     with psycopg2.connect(os.environ['POSTGRE_PASSWORD']) as conn:
#         with conn.cursor() as cursor:
#             sql='''
#                 SELECT DISTINCT 名稱
#                 FROM station
#                 WHERE SUBSTRING(地址,1,3) = %(city)s;
#             '''
#             cursor.execute(sql,{'city':city_name})
#             queryDatas:list[tuple[str]] = cursor.fetchall()
#             station_names:list[str] = [item[0] for item in queryDatas]
#             return station_names
        
with st.sidebar:    
    source_data:list[str]= getCity()
    selected_city:str = st.selectbox('選擇縣市',options=source_data)
    # selected_station:list[str] = getStation(selected_city)
    # st.selectbox('選擇車站', selected_station)