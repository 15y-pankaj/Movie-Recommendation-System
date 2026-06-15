import streamlit as st
import pandas as pd
import joblib
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent

# ----------------------------------------------------------
movies_dict = joblib.load(BASE_DIR / 'model' / 'movie_dict.pkl')
movies = pd.DataFrame(movies_dict)

similarity = joblib.load(BASE_DIR / 'model' / 'similarity.pkl')

#----------------------------------------------------------



import requests
@st.cache_data
def fetch_poster(movie_id):
    api_key = os.getenv("TMDB_API_KEY")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    
    for attempt in range(5):  # retry up to 5 times
        try:
            data = requests.get(url, timeout=10).json()  # 10 sec timeout
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
        except:
            continue  # retry on failure
    
    return "https://via.placeholder.com/500x750?text=No+Image"
#------------------------------------------------------------


def recommend(movie):
    
    index=movies[movies['title']==movie].index[0]

    #distances=similarity[movie_index]
    distances= sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    

    recommended_movie_name=[]
    recommended_movie_posters=[]
    for i in distances[1:6]:

        movie_id=movies.iloc[i[0]].movie_id
        
        recommended_movie_name.append(movies.iloc[i[0]].title)
        #fetch poster form API
        recommended_movie_posters.append(fetch_poster(movie_id))
        
    return recommended_movie_name,recommended_movie_posters


#-----------------------------------------------------
st.header('Movie Recommender System')

movie_list=movies['title'].values
selected_movie_name =st.selectbox('Please choose any Movie ',movie_list)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
     with col:
        st.text(names[idx])
        st.image(posters[idx])
    