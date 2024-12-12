import streamlit as st
from fontend.screens import mananger_page 


# Khởi tạo session state
if "page" not in st.session_state or st.session_state.page is None:
    st.session_state.page = "home"  # Trang mặc định là home
if "search_by_mood" not in st.session_state:
    st.session_state.search_by_mood = {'selected_songs': []}
if "search" not in st.session_state:
    st.session_state.search = {}
    
# Hiển thị trang tương ứng
if st.session_state.page == "home":
    mananger_page.home_page()
elif st.session_state.page == "search_by_name":
    mananger_page.search_by_name_page()
elif st.session_state.page == "search_by_mood":
    mananger_page.search_by_mood_page()
