import streamlit as st
from fontend import search_by_mood_genres
from fontend import search_by_name
from fontend.ani_snow import snow_ani

# Khởi tạo session state
if "page" not in st.session_state or st.session_state.page is None:
    st.session_state.page = "home"  # Trang mặc định là home

if "search_by_mood" not in st.session_state:
    st.session_state.search_by_mood = {'selected_songs': []}

if "search" not in st.session_state:
    st.session_state.search = {}
    
def home_page():
    ## Apply .css 
    with open("fontend/css/style_main_page.css", encoding='utf-8') as f:
        style = f.read()
    st.markdown(f'<style>{style}</style>', unsafe_allow_html=True)
    snow_ani('❄️')
    st.markdown("<h1>🎶 Welcome to Music Recommendation App! 🎶</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Discover your favorite songs and artists here!</h2>", unsafe_allow_html=True)

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
    """Trang tìm kiếm theo tâm trạng và thể loại."""
    st.title("🎵 Search Songs by Mood and Genre 🎵")
    with open("fontend/css/style_search_by_mg.css", encoding='utf-8') as f:
        style = f.read()
    st.markdown(f'<style>{style}</style>', unsafe_allow_html=True)
   
    search_app = search_by_mood_genres.SearchByMood()  # Tạo đối tượng từ lớp SearchByMood
    if st.session_state.search_by_mood['selected_songs']:
        snow_ani('❄️')
        search_app.display_results()  # Hiển thị kết quả tìm kiếm
    else:
        snow_ani('❄️')
        search_app.search_page()  # Hiển thị giao diện tìm kiếm
def search_by_name_page():
    """Trang tìm kiếm bài hát theo tên."""
    st.title("🔍 Search Songs by Name")
    with open("fontend/css/style_search_by_n.css", encoding='utf-8') as f:
        style = f.read()
    st.markdown(f'<style>{style}</style>', unsafe_allow_html=True)
    
    search_app = search_by_name.SearchByName()  # Tạo đối tượng từ lớp SearchByName
    if "selected_song" in st.session_state.search:
        snow_ani('❄️')
        search_app.display_results()  # Hiển thị bài hát đã chọn
    else:
        snow_ani('❄️')
        search_app.search_page()  # Hiển thị giao diện tìm kiếm bài hát

# Hiển thị trang tương ứng
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "search_by_name":
    search_by_name_page()
elif st.session_state.page == "search_by_mood":
    search_by_mood_page()
