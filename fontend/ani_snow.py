import streamlit as st

def snow_ani(snow_icon):
    with open("fontend/css/snow_animation.css", encoding='utf-8') as f:
        style = f.read()
    st.markdown(f'<style>{style}</style>', unsafe_allow_html=True)
    st.markdown(f"""<div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            <div class = "snowflake">{snow_icon}</div>
            """,unsafe_allow_html=True)