# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System that suggests movies to users based on their preferences, viewing history, and similarity between movies. The system leverages recommendation algorithms to provide personalized movie suggestions and improve user experience.


## 📌 Features

* Recommend movies based on user preferences.
* Content-based filtering using movie metadata.
* Similar movie recommendations.
* Fast and efficient recommendation generation.
* User-friendly interface.
* Scalable architecture for large movie datasets.


## overview:-


<img width="2816" height="1536" alt="movie" src="https://github.com/user-attachments/assets/ef502566-b836-4f13-92f3-ccbb14b7351d" />



## 🛠️ Technologies Used

### Programming Language

* Python 3.x

### Libraries & Frameworks

* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit / Flask (for web application)
* Pickle

## 📂 Project Structure

```bash
movie-recommendation-system/
│
├── data/
│   ├── movies.csv
│   ├── credits.csv
│
├── notebooks/
│   ├── movie_recommendation.ipynb
│
├── models/
│   ├── similarity.pkl
│   ├── movies.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### Streamlit Version

```bash
streamlit run app.py
```

### Flask Version

```bash
python app.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

or

```text
http://127.0.0.1:5000
```


## 🧠 How It Works

1. Data preprocessing and cleaning.
2. Feature extraction from movie metadata.
3. Vectorization using CountVectorizer or TF-IDF.
4. Similarity computation using Cosine Similarity.
5. Recommendation generation based on the selected movie.

### Recommendation Pipeline

```text
Movie Selected
       ↓
Feature Extraction
       ↓
Vectorization
       ↓
Cosine Similarity
       ↓
Top N Similar Movies
```

## 📊 Example Output

**Input:**

```text
Avatar
```

**Recommended Movies:**

```text
Guardians of the Galaxy
Star Trek
John Carter
The Avengers
Ender's Game
```



