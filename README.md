# Recommendation Systems: Movies and Music 🎬🎵

This repository contains two content-based recommendation systems: one for movies and another for music. Both systems leverage **TF-IDF (Term Frequency-Inverse Document Frequency)** and **cosine similarity** to provide personalized recommendations based on content.

---

## 1. Movie Recommendation System 🎬

### Overview
The **Movie Recommendation System** is a content-based recommender that suggests movies similar to a given movie. It uses metadata such as genres, keywords, and overviews to compute similarity between movies.

### Key Features
- **Content-Based Filtering**: Recommends movies based on their content similarity.
- **TF-IDF Vectorization**: Converts textual data (genres, keywords, overviews) into numerical vectors.
- **Cosine Similarity**: Measures the similarity between movies based on their vectorized content.
- **Interactive Interface**: Built with Python and Streamlit for a user-friendly experience.

### Workflow
1. **Data Preprocessing**:
   - Combines metadata fields (e.g., genres, keywords, overview) into a single text field.
   - Cleans and tokenizes text data.
2. **TF-IDF Vectorization**:
   - Converts the combined text into a matrix of TF-IDF features.
3. **Cosine Similarity Calculation**:
   - Computes pairwise cosine similarity between movies.
4. **Recommendation**:
   - Retrieves the top `N` most similar movies for a given input movie.

### Example
Input: *"Batman v Superman: Dawn of Justice"*  
Output:
- Man of Steel
- Superman II
- Batman Returns
- Superhero Movie
- Defendor

---

## 2. Music Recommendation System 🎵

### Overview
The **Music Recommendation System** is a content-based recommender that suggests songs similar to a given song. It uses song lyrics to compute similarity between tracks.

### Key Features
- **Content-Based Filtering**: Recommends songs based on their lyrical similarity.
- **TF-IDF Vectorization**: Converts song lyrics into numerical vectors.
- **Cosine Similarity**: Measures the similarity between songs based on their vectorized lyrics.
- **Interactive Interface**: Built with Python and Streamlit for fast and interactive song suggestions.

### Workflow
1. **Data Preprocessing**:
   - Cleans and tokenizes song lyrics.
2. **TF-IDF Vectorization**:
   - Converts lyrics into a matrix of TF-IDF features.
3. **Cosine Similarity Calculation**:
   - Computes pairwise cosine similarity between songs.
4. **Recommendation**:
   - Retrieves the top `N` most similar songs for a given input song.

---

## Shared Methodology: Content-Based Cosine Similarity

Both systems rely on **cosine similarity**, a metric that measures the cosine of the angle between two vectors in a multi-dimensional space. This approach ensures that recommendations are based on the relative similarity of content, regardless of the magnitude of the vectors.

### Why Cosine Similarity?
- **Efficient**: Works well with sparse data like TF-IDF matrices.
- **Content-Focused**: Ensures recommendations are based on the actual content rather than user behavior.

### Formula
Cosine similarity is calculated as:

**cos(θ) = (A · B) / (||A|| ||B||)**

Where:
- `A` and `B` are TF-IDF vectors of two items (movies or songs).
- `A · B` is the dot product of the vectors.
- `||A||` and `||B||` are the magnitudes of the vectors.

---

## Installation and Usage

### Prerequisites
- Python 3.x
- Required libraries: `numpy`, `pandas`, `scikit-learn`, `nltk`, `matplotlib`, `streamlit`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/recommendation-systems.git
   cd recommendation-systems

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

recommendation_systems/
│
├── movie_recommendation/
│   ├── src/
│   │   ├── main.py          # Streamlit app for movies
│   │   ├── recommend.py     # Recommendation logic
│   │   ├── preprocess.py    # Data preprocessing
│   │   ├── movies.csv       # Movie dataset
│   │   └── config.json      # Configuration file
│   ├── [README.md](http://_vscodecontentref_/0)            # Movie recommendation README
│   └── requirements.txt     # Dependencies for movies
│
├── music_recommendation/
│   ├── src/
│   │   ├── main.py          # Streamlit app for music
│   │   ├── recommend.py     # Recommendation logic
│   │   ├── preprocess.py    # Data preprocessing
│   │   ├── spotify_millsongdata.csv  # Music dataset
│   └── [README.md](http://_vscodecontentref_/1)            # Music recommendation README
│
└── [README.md](http://_vscodecontentref_/2)                # Combined README

