import json
import streamlit as st
from recommend import df, recommend_movies
from omdb_utils import get_movie_details

config = json.load(open("config.json"))

OMBD_API_KEY = config["OMDB_API_KEY"]

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommender")

movie_list = sorted(df['title'].dropna().unique())

selected_movie = st.selectbox("🎬 Select a movie:", movie_list)

if st.button("🚀 Recommend Similar Movies"):
    with st.spinner("Finding Similar Movies..."):
        recommendations = recommend_movies(selected_movie)
        if recommendations is None or recommendations.empty:
            st.warning("No recommendations found.")
        else:
            st.success("Top Similar Movies:")
            for _, row in recommendations.iterrows():
                movie_title = row['title']
                genres = row['genres']
                director = row['director']
                cast = row['cast']
                crew = row['crew']
                plot, poster = get_movie_details(movie_title, OMBD_API_KEY)

                with st.container():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if poster != "N/A":
                            st.image(poster, width=100)
                        else:
                            st.write("❌ No Poster Found")
                    with col2:
                        st.markdown(f"### {movie_title}")
                        st.markdown(f"*{plot}*" if plot != "N/A" else "_Plot not available_")
                        st.write(f"**Genres:** {genres}")
                        st.write(f"**Director:** {director}")
                        st.write(f"**Cast:** {cast}")
                        st.write(f"**Crew:** {crew}")
                        st.markdown("---")