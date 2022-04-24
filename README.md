# SC1015 DSAI Project: AniFame

**Our Motivation:**
- Animes are outlets of relaxation and escape for people of all ages. However, while anime viewers love watching anime, studios are experiencing difficulties in making profits for many of the anime they produced due to **high costs.**
- According to Eric (2015), an average 13-episode anime season costs around $2 million USD, and many animes cannot recoup this expense. In order to make it sell, anime advertisements, events and merchandise are essential to studios’ profit margin. All this depends on the popularity of the anime with anime viewers. 
- Hence, it is important to know whether the anime that a studio is producing will be profitable, hence allowing studios to **maximise their profits** and ensure their survivability in the industry.

![MAL](https://user-images.githubusercontent.com/47933193/164981422-834ebc32-3be4-430e-b69e-c38dcf065d3e.png)

## Project Goal:
- This project aims to **maximize studios’ profits** on animes they produce by estimating 'mean' rating of animes and predicting 'success' probability before production, hence giving studios the ability to **fine-tune** the animes before production.

## Dataset Used:
We used MyAnimeList [API](https://myanimelist.net/apiconfig/references/api/v2) to scrap anime from 2000 to 2021, cleaned and processed it for Exploratory Data Analysis and Machine Learning.
- [DataSet Folder](https://github.com/ztjhz/SC1015-Project/tree/main/Anime/dataset)

**Note:** Some datasets are scraped but are not included in the final project (e.g. the various ranking datasets)

## Jupyter Notebooks:
- [Data Collection](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/data_collection_(scraping).ipynb)
- [Data Cleaning and Preprocessing](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/data_cleaning_preprocessing.ipynb)
- [Exploratory Data Analysis & Visualization](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/exploratory_data_analysis_visualization.ipynb)
- [Linear Regression](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/linear_regression.ipynb)
- [Classification](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/classification.ipynb)

**Note:** Some Jupyter Notebooks are used but are not included in the final project (e.g. anomaly detection, helpers, scraper)

## Slide Deck:
- [Presentation Slides](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/slides_deck.pdf)

<br>

---

# Overview of DataScience Pipeline:
### [1. Data collection:](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/data_collection_(scraping).ipynb)
- Used [MAL API](https://myanimelist.net/apiconfig/references/api/v2) to recursively scrap thousands of anime data from 2000 to 2021

### [2. Data cleaning and preprocessing:](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/data_cleaning_preprocessing.ipynb)
- Removing useless features, handling missing values
- Json conversion and manipulation
- Feature engineering and generation
- Creating 'genres' time series data
- Export data as csv
- [One-hot Encoding](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/linear_regression.ipynb)

### [3. EDA & Visualization:](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/exploratory_data_analysis_visualization.ipynb)

Explored, visualized, and generated insights for the following:
- 'genres' + 'genres' time series
- 'studios'
- 'mean' rating vs 'source', 'media_type', 'nsfw', 'rating', 'genre', and 'studios'
- Relationship between 'mean', 'rank', 'popularity', 'positive_viewership_fraction', and 'negative_viewership_fraction'
- num_episodes' and 'average_episode_duration' overview trend
- 'start_season_season'

### [4. Regression:](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/linear_regression.ipynb) <br>
`Models:`
- Linear Regression
- Lasso Regression
- Ridge Regression **(Best)**
 
`Metrics:`
- Explained Variance (R^2)
- Mean Squared Error, Root Mean Squared Error


### [5. Classification:](https://github.com/ztjhz/SC1015-Project/blob/main/Anime/classification.ipynb) <br>
`Models:`
- LinearSVC
- Decision Tree
- Random Forest **(Best - 4th version)** 

`Metrics:`
- TPR, TNR, Confusion Matrix
- Precision, Recall (TPR), F-score
- Out-of-bag score
- ROC AUC score
- K-fold cross validation standard deviation


### 6. Key Insights & Recommendations:

Studios should:
- Focus on **quality over quantity** of animes
- Broadcast animes **regardless of season**
- **Not** focus on producing animes that generate more positive views through fan-service
- Produce **anime movie franchises**

**Important features** that determine the success of an anime:
  - ‘average_episode_duration’
  - ‘num_episodes’
  - ‘source_manga’
  - ‘media_type_movie’
  - ‘rating_pg_13’

<br>

---

# What we learnt from this project:
**Data collection:**
- Scraping data using API calls

**Data cleaning and preprocessing:**
- Feature Engineering & Feature generation
- JSON manipulation techniques
- Generating time-series data 

**EDA & Visualization:**
- Visualization plots with large number of datapoints
  - By reducing the data point size,
  - By reducing the opacity of data points, or
  - By introducing random sampling
- ‘genres’ time-series EDA

**Machine Learning:**
- Machine Learning Models:
  - Ridge Regression, Lasso Regression, Random Forest, LinearSVC
- Classification Performance Metrics:
  - F-score (Precision & Recall), out-of-bag (obb) score, ROC AUC score

<br>

---

# Contributions:
**Data Collection:** `Jing Qiang` and `Jing Hua` <br>
**Data cleaning and preprocessing:** `Jing Qiang`, `Jing Hua`, and `YinFeng` <br>
**EDA and visualization:** `Jing Qiang` and `Jing Hua` <br>
**Regression:** `Jing Hua` <br>
**Classification:** `Jing Qiang` <br>
**Presentation Script:** `Jing Qiang` <br>
**Presentation Voice Over + Editing:** `Jing Hua` <br>
**Slides Deck:** `Jing Qiang`, `Jing Hua`, `YinFeng` <br>
**GitHub ReadMe:** `Jing Qiang` <br>


Did but not included in the final product: <br>
- **Ranking dataset EDA:** `YinFeng` <br>
- **Anomaly Detection:** `Jing Qiang`, `YinFeng` <br>


# References:
- https://myanimelist.net/apiconfig/references/api/v2
- https://www.animenewsnetwork.com/interest/2015-08-13/anime-insiders-share-how-much-producing-a-season-costs/.91536#:%7E:text=Like%20other%20entertainment%20ventures%2C%20any,yen%20(or%20%242%20million)
- https://medium.com/@cheahwen1997/data-analysis-and-visualization-on-anime-using-pandas-and-matplotlib-1150d6605f5a
- https://towardsdatascience.com/linear-regression-models-4a3d14b8d368
- https://medium.datadriveninvestor.com/choosing-the-best-algorithm-for-your-classification-model-7c632c78f38f
- https://builtin.com/data-science/random-forest-algorithm
- https://www.kaggle.com/code/niklasdonges/end-to-end-project-with-python/notebook
- https://quantdare.com/decision-trees-gini-vs-entropy/

