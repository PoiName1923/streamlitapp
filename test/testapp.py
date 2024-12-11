import streamlit as st

st.title("🎵 Search Songs by Mood and Genre 🎵")
with open("test/style.css", encoding='utf-8') as f:
    style = f.read()
st.markdown(f'<style>{style}</style>', unsafe_allow_html=True)

song = "https://images.pexels.com/photos/45853/grey-crowned-crane-bird-crane-animal-45853.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
song_name = "ádasdasd"
art_name = "sadasdad"
link = "https://images.pexels.com/photos/45853/grey-crowned-crane-bird-crane-animal-45853.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
link_audio = "https://commondatastorage.googleapis.com/codeskulptor-assets/week7-button.m4a"




with st.container():
    st.image(song,width=200)
    st.markdown(f'<a class="song-title" href="{song}" target="_blank">{song}</a>', unsafe_allow_html=True)
    st.markdown(f'<p class="artist-name"><strong>Artist</strong>: {art_name}</p>', unsafe_allow_html=True)
    st.markdown(f'<a href="{link}" class="spotify-link" target="_blank">Spotify Link</a>', unsafe_allow_html=True)
    st.markdown(f'<div class="audio-player">', unsafe_allow_html=True)
    st.audio(link_audio, format="audio/mp3")
    st.markdown('</div>', unsafe_allow_html=True)