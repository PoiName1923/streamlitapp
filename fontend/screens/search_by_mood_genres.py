import streamlit as st
from backend.search_song import search_rcm_mood_genres
from streamlit_lottie import st_lottie as lt
class SearchByMood:
    def __init__(self):
        # Initialize search_by_mood state in session_state
        if 'search_by_mood' not in st.session_state:
            st.session_state.search_by_mood = {'selected_songs': []}
    def search_page(self):
        st.title("🔍 Search Songs by Mood and Genre 🔍")
        # Input fields for genres and mood
        genres = st.text_input("Choose your favourite genres:", placeholder="e.g., pop, jazz")
        mood = st.radio("Choose your mood today!", options=["Happy", "Sad", "Neutral"])

        if st.button("Go!"):
            with st.spinner("We are finding your track!🕛"):
                if genres:
                    st.session_state.search_by_mood['selected_songs'] = []  # Reset previous search results
                    songs = search_rcm_mood_genres(mood, genres)
                    if songs.empty:
                        st.warning("No songs found for your search.")
                    else:
                        for _, song in songs.iterrows():
                            st.session_state.search_by_mood['selected_songs'].append(song.to_dict())
                        st.rerun()
        # Back button to return to the home page
        if st.button("Back to Home",key="back_to_home"):
            st.session_state.page = "home"
            st.rerun()

    def display_results(self):
        st.title("🎶 Search Results")
        songs = st.session_state.search_by_mood['selected_songs']
        if not songs:
            st.warning("No songs to display.")
            return
        
        # Loop through and display each song
        for song in songs:
                picture_line, info_line = st.columns([1, 4])

                with picture_line:
                    st.image(song['LINK_IMAGE'])

                with info_line:
                    st.write(f"### {song['NAME']}")
                    st.write(f"**Artist**: {song['ARTIST_NAME']}")
                    st.write(f"**Spotify**: [Link]({song['URL']})")
                st.audio(song['PREVIEW'], format="audio/mp3")

        # Back button to return to search page
        if st.button("Back to Search",key = "back_to_search"):
            if 'search_by_mood' in st.session_state:
                del st.session_state.search_by_mood
            st.session_state.page = "search_by_mood"
            st.rerun()
        if st.button("Back to Home",key="back_to_home_results"):
            del st.session_state.search_by_mood
            st.session_state.page = "home"
            st.rerun()
