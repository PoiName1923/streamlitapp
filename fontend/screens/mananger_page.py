import streamlit as st
from fontend.screens import search_by_mood_genres
from fontend.screens import search_by_name
from fontend.animations.ani_snow import snow_ani


def home_page():
    ## Apply .css 
    with open("fontend/css/style_main.css", encoding='utf-8') as f:
        style = f.read()
    st.markdown(f'<style>{style}</style>', unsafe_allow_html=True)
    snow_ani('❄')
    st.markdown("<h1>🎶 Welcome to Music Recommendation App! 🎶</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Discover your favorite songs and artists here!</h2>", unsafe_allow_html=True)
    
    ## Hiển thị các nút và nhận biết nút được bấm để chuyển trang
    with st.form(key='my_form'):
        search_by_name = st.form_submit_button("Tìm kiếm theo tên của bài nhạc")
        search_by_mod_and_geners = st.form_submit_button("Tìm kiếm theo tâm trạng và thể loại")
    if search_by_name:
        st.session_state.page = "search_by_name"
        st.rerun()
    elif search_by_mod_and_geners:
        st.session_state.page = "search_by_mood"
        st.rerun()

def search_by_mood_page():
    ## Dùng để thêm các đối tượng css vào trong trang này
    st.title("🎵 Search Songs by Mood and Genre 🎵")
    with open("fontend/css/style_search_by_mg.css", encoding='utf-8') as f:
        style = f.read()
    st.markdown(f'<style>{style}</style>', unsafe_allow_html=True)
    
    ## Tạo đối tượng từ lớp SearchByMood
    search_app = search_by_mood_genres.SearchByMood()
    if st.session_state.search_by_mood['selected_songs']:
        snow_ani('❄')
        search_app.display_results()
    else:
        snow_ani('❄')
        search_app.search_page()
        
def search_by_name_page():
    
    ## Dùng để thêm các đối tượng css vào trong trang này
    st.title("🔍 Search Songs by Name")
    with open("fontend/css/style_search_by_n.css", encoding='utf-8') as f:
        style = f.read()
    st.markdown(f'<style>{style}</style>', unsafe_allow_html=True)
    
    ## Tạo đối tượng từ lớp SearhcByName
    search_app = search_by_name.SearchByName()
    if "selected_song" in st.session_state.search:
        snow_ani('❄')
        search_app.display_results()
    else:
        snow_ani('❄')
        search_app.search_page()
