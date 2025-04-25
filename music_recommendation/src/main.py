import streamlit as st
from recommend import df, recommend_songs

st.set_page_config(
    page_title="Music Recommender 🎵",
    page_icon="🎧",  # You can also use a path to a .ico or .png file
    layout="centered"
)

st.title("🎶 Instant Music Recommender")

song_list = sorted(df['song'].dropna().unique())
selected_song = st.selectbox("🎵 Select a song:",song_list)

if st.button("🚀 Recommend Similar Songs"):
    with st.spinner("Finding Similar Songs..."):
        recommendations = recommend_songs(selected_song)
        if recommendations is None:
            st.warning("Sorry, song not found.")
        else:
            st.success("Top Similar songs:")
            st.table(recommendations)