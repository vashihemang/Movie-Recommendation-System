import streamlit as st
import pandas as pd

# Load datasets
movies = pd.read_csv("movies.csv")

# Load precomputed matrices
user_similarity_df = pd.read_pickle("user_similarity_df.pkl")
item_similarity_df = pd.read_pickle("item_similarity_df.pkl")
user_movie_fill_values = pd.read_pickle("user_movie_fill_values.pkl")

# ----------------------------------
# User-Based Recommendation Function
# ----------------------------------

def get_user_recommendations(user_id, n=5):

    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:11]
    sim_user_ratings = user_movie_fill_values.loc[similar_users.index]

    weights = similar_users.values.reshape(-1, 1)

    weighted_scores = (sim_user_ratings * weights).sum(axis=0) / weights.sum()

    user_seen_movies = user_movie_fill_values.loc[user_id]

    unseen_movies_scores = weighted_scores[user_seen_movies == 0]

    top_movies = unseen_movies_scores.sort_values(ascending=False).head(n)

    top_movies.index = top_movies.index.astype(int)

    recommended_movies = movies[movies["movieId"].isin(top_movies.index)][["movieId", "title", "genres"]].copy()

    recommended_movies["predicted_rating"] = (recommended_movies["movieId"].map(top_movies).round(2))

    return recommended_movies.sort_values(by="predicted_rating",ascending=False)


# ----------------------------------
# Item-Based Recommendation Function
# ----------------------------------

def item_based_recommendation_simplest(user_id, n=5):

    user_ratings = user_movie_fill_values.loc[user_id]

    rated_movies = user_ratings[user_ratings > 0]

    similarities = item_similarity_df[rated_movies.index]

    multiplied_scores = similarities * rated_movies

    total_scores = multiplied_scores.sum(axis=1)

    sum_of_similarities = similarities.sum(axis=1)

    predicted_ratings = (total_scores / sum_of_similarities)

    predicted_ratings = predicted_ratings[user_ratings == 0]

    top_movies = predicted_ratings.nlargest(n)
    top_movies.index = top_movies.index.astype(int)
    recommended_movies = movies[movies["movieId"].isin(top_movies.index)][["movieId", "title", "genres"]].copy()

    recommended_movies["predicted_rating"] = (recommended_movies["movieId"].map(top_movies).round(2))

    return recommended_movies.sort_values(by="predicted_rating",ascending=False)


# ----------------------------------
# Streamlit UI
# ----------------------------------

st.title("🎬 Movie Recommendation System")

user_id = st.number_input("Enter User ID",min_value=1,step=1)

algo = st.selectbox(
    "Recommendation Method",["User Based Filtering","Item Based Filtering"])

top_n = st.slider("Number of Recommendations",1,20,5)

if st.button("Recommend Movies"):
    try:

        if algo == "User Based Filtering":

            result = get_user_recommendations(user_id=user_id,n=top_n)

        else:
            result = item_based_recommendation_simplest(user_id=user_id,n=top_n)

        st.success(f"Top {top_n} Recommendations")

        st.dataframe(result,use_container_width=True)

    except Exception as e:

        st.error(str(e))