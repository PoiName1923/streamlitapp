import streamlit as st
from backend.search_song import search_track_Snowflake  # Import chức năng tìm kiếm bài hát

class SearchByName:
    def __init__(self):
        # Khởi tạo trạng thái tìm kiếm trong session_state nếu chưa có
        if 'search' not in st.session_state:
            st.session_state.search = {}

    def search_page(self):
        """Hiển thị giao diện tìm kiếm bài hát"""
        song_name = st.text_input("Search for a song:", placeholder="Enter song name here...")
        if song_name:
            data = search_track_Snowflake(song_name.strip())  # Gọi hàm tìm kiếm
            if data.empty:
                st.warning("No songs found!")
            else:
                st.write("### Search Results:")
                for _, song in data.iterrows():
                    # Tạo một nút cho mỗi bài hát
                    if st.button(f"{song['TRACK_NAME']} - {song['ARTIST_NAME']}", key=song['TRACK_ID']):
                        st.session_state.search['selected_song'] = song.to_dict()  # Lưu bài hát được chọn
                        st.rerun()  # Làm mới trang để hiển thị kết quả

        if st.button("Back to Home",key="back_home_search_home"):
            del st.session_state.search
            st.session_state.page = "home"
            st.rerun()
            
    def display_results(self):
        """Hiển thị thông tin bài hát đã chọn"""
        if 'selected_song' not in st.session_state.search:
            st.error("No song selected! Please go back to search for a song.")
            return

        song = st.session_state.search['selected_song']
        picture_line, info_line = st.columns([1, 4])

        with picture_line:
            st.image(song['LINK_IMAGE'], use_column_width=True)

        with info_line:
            st.write(f"### {song['TRACK_NAME']}")
            st.write(f"**Artist**: {song['ARTIST_NAME']}")
            st.write(f"**Followers**: {song['FOLLOWERS']}")
            st.write(f"**Spotify Link**: [Click here]({song['URL']})")
        st.audio(song['PREVIEW'], format="audio/mp3")


        if st.button("Back",key = "back_search_name"):
            if 'search' in st.session_state:
                del st.session_state.search
            st.session_state.page = "search_by_name"
            st.rerun()
        if st.button("Back to Home",key="back_home_search_home"):
            del st.session_state.search
            st.session_state.page = "home"
            st.rerun()
