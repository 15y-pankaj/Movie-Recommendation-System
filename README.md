# Movie Recommendation System

A simple content-based movie recommender built from TMDB datasets. Includes a Jupyter notebook used to prepare data and build model artifacts and a Streamlit front-end for interactive recommendations.

## Repository layout

- `app.py` — Streamlit app that loads precomputed artifacts and serves recommendations.
- `notebook/make.ipynb` — Notebook used to preprocess data and build the model (feature extraction, vectorization, cosine similarity).
- `data/` — CSV data files used by the notebook (tmdb_5000_movies.csv, tmdb_5000_credits.csv).
- `model/` — Saved artifacts used by the app (e.g. `movie_dict.pkl`, `similarity.pkl`).
- `requirements.txt` — Minimal Python dependencies for running the app and notebook.
- `.gitignore` — Project ignores (virtualenvs, data, model artifacts).

## Requirements

Install the project's dependencies into a virtual environment. Requirements are intentionally minimal — only the libraries referenced by the code and notebook are included.

```bash
python -m venv venv3.11
# Windows PowerShell
.\venv3.11\Scripts\Activate.ps1
# or (cmd)
.\venv3.11\Scripts\activate
pip install -r requirements.txt
```

## Run the Streamlit app

Start the app locally with:

```bash
streamlit run app.py
```

Open the URL shown by Streamlit in your browser.

## Notes & configuration

- The app calls The Movie Database (TMDB) API to fetch poster images. The API key should be stored in a `.env` file as `TMDB_API_KEY=your_key`. Copy `.env.example` to `.env`.
- Model artifacts: the app expects `model/movie_dict.pkl` and `model/similarity.pkl`. If you regenerate these from the notebook, save them into the `model/` directory.
- The notebook uses `nltk` and `scikit-learn` for preprocessing and vectorization. Run the notebook to reproduce artifacts.

## Reproducing model artifacts

1. Open `notebook/make.ipynb` and run cells from top to bottom (ensure data files are present in `data/`).
2. The notebook saves pickled artifacts into the `model/` folder; ensure these files exist before running the Streamlit app.

## Development

- Use `.gitignore` to avoid committing virtual environments, the `data/` directory, and model `.pkl` files.

## Contact

If you want help pinning versions in `requirements.txt`, or automating artifact generation, tell me and I can add them.
