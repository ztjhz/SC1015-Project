# Project AniFame
The cost of producing an anime is very high, so it is important to know whether the anime that a studio is producing will be profitable, hence allowing studios to maximise their profits and ensure their survivability in the industry.

This project aims to maximize studios’ profits on anime they produce. We use MyAnimeList API to scrap anime from 2000 to 2021, clean and process it for Exploratory Data Analysis and Machine Learning.

## 1. Data Collection
Dataset used:
- Animes from 2000 to 2021 scraped from MyAnimeList.net [API](https://myanimelist.net/apiconfig/references/api/v2)

## 2. Data Cleaning
#### Missing Values
Fill the NaN entries with domain specific knowledge

#### Json Manipulation
Convert features into Json format for manipulation and feature generation

#### Feature Engineering
1. Aggregate individual individual viewing statistics into `positive_viewership_fraction` and `negative_viewership_fraction`
    - `positive_viewership_fraction` = (`statistics_watching` + `statistics_completed` + `statistics_plan_to_watch`) / `total_views`
    - `negative_viewership_fraction` = (`statistics_on_hold` + `statistics_dropped`) / `total_views`
2. Create feature `success`, for animes with:
    - `rank` <= 500
    - `popularity` <= 500
    - `mean` >=8.5
    - `positive_viewership_fraction` >= 0.975

#### Time Series
Create `genres` time-series since `genres` are obvious differences between animes

#### One-hot Encoding
One-hot encoding of categorical features for building machine learning models

## 3. Exploratory Data Analysis & Visualization
### Genres Count
Frequency of occurance of all the genres of animes from 2000 to 2021

<img src="https://user-images.githubusercontent.com/100555522/164972748-2bc029ca-4ffe-4422-92b1-728ef5d3288f.png" width="800" height="800">

- 'Comedy' genre has the most animes
- Top 5 genres from 2000 to 2021 are `Comedy`, `Action`, `Fantasy`, `Adventure`, and `Shounen`

### Award Winning vs No Genre
Compairing `award_winning` genre and `no_genre` animes

![download](https://user-images.githubusercontent.com/100555522/164973052-aa1ea8f4-6991-49b9-b794-4f10d4b7d62e.png)
![download](https://user-images.githubusercontent.com/100555522/164973439-1ad3eeac-e629-4d99-8c33-7d0ef73c1b37.png)

- `Award_winning` animes on generally have higher popularity, have better rankings, and are rated higher for all the animes than that of `no_genre` animes
- What differentiate these 2 categories is that Award Winning animes are more popular and higher ranked such that `Award_Winning` animes have genres associated with them whereas `no_genre` animes do not

- Comparing average number of viewers:
    - 'no_genre':      	 2920.625
    - 'Award Winning': 	 552745.0
    - 'Award Winning' has 18925.57% more views than 'no_genre'

- Comparing percentage of positive viewship:
    - 'no_genre':      	 2786.88
    - 'Award Winning': 	 550592.33
    - 'Award Winning' has 19756.59% more positive views than 'no_genre'
 
- Comparing percentage of negative viewship:
    - 'no_genre':      	 133.75
    - 'Award Winning': 	 2152.67
    - 'Award Winning' has 1609.47% more negative views than 'no_genre'
 
- More people watch Award Winning animes and have positive experience with them compared to no_genre animes since the retention is greater for Award Winning animes

### Genres Trends
`Genre` trends by anime counts from 1999 to 2021

<img src="https://user-images.githubusercontent.com/100555522/164975183-962cb2a5-7311-4a56-9cc2-fe5330354c20.png" width="800" height="800">

- Decreasing genre trends: 
    - Shounen, Comedy, Kids, Mecha, Sci-Fi, Adventure
- Increasing genre trends:
    - Slice of Life, Music
 
### Studio Analysis
Anime `studio` counts from 2000 to 2021

![download](https://user-images.githubusercontent.com/100555522/164975540-bf621492-d04a-4add-a9ab-21fd19542031.png)

- Top 5 anime studios:
    - Toei Animation, Sunrise, TMS Entertainment, Madhouse, OLM

### Mean Rating Analysis
Number of positive user scoring of anime without ratings vs anime with ratings

![download](https://user-images.githubusercontent.com/100555522/164976060-ccbb9f10-1b4e-4092-9de8-a31d0937d1de.png)

- Animes without mean ratings are those that have low `num_scoring_users`, which means that there are not enough users watching and rating these animes for it to have a reliable `mean` rating

### Source vs Mean Rating
`Sources` of anime vs `mean` ratings of anime

<img src="https://user-images.githubusercontent.com/100555522/164976211-ec360780-87dd-4185-8c84-90b6e00b621f.png" width="800" height="500">
<img src="https://user-images.githubusercontent.com/100555522/164976285-c5698c46-ae9b-485e-b8a1-cfffbde1f74f.png" width="800" height="500">

- `Web Novels` is a anime source that is very popular among viewers as these animes have a mean rating of 8.4, which is significantly more than that of other sources
- The top 5 anime sources are `web_novel`, `manga`, `light_novel`, `novel`, and `web_manga`

### Media Type vs Mean Rating
`Media type` of anime vs `mean` rating of anime

<img src="https://user-images.githubusercontent.com/100555522/164976426-a6798473-6597-47e3-8f85-9c86ab26dfe8.png" width="800" height="500">
<img src="https://user-images.githubusercontent.com/100555522/164976464-6556191d-c19c-47e4-b968-ef15e2f9792b.png" width="800" height="500">

- All media types generally have similar mean rating
- Types `tv`, `movie`, and `ova` have slightly higher mean rating, while music have the lowest mean rating

### Mean Rating vs Rating
`Rating` of anime vs `mean` rating of anime

<img src="https://user-images.githubusercontent.com/100555522/164976602-4b51d010-d723-442a-8c11-c3f7fdd035ef.png" width="800" height="500">
<img src="https://user-images.githubusercontent.com/100555522/164976645-bd0865b7-12aa-4159-9112-3beb71f44f46.png" width="800" height="500">

- The rating `r` has the highest mean rating while `no_rating` and `g` have the lowest mean rating

### Genre vs Mean rating
`Genre` of anime vs `mean` rating of anime

<img src="https://user-images.githubusercontent.com/100555522/164976708-afac5be8-6b9c-4f03-ad36-dd9582778bd4.png" width="800" height="500">
<img src="https://user-images.githubusercontent.com/100555522/164976784-b7cce3cb-2964-4490-ac46-b3cce2345cb2.png" width="800" height="500">

- The top 5 genres with the highest mean rating include `Award Winning`, `Suspense`, `Police`, `Super Power`, and `Samurai`
- The bottom 5 genres with the lowest mean rating include `no_genre`, `Avant Garde`, `Kids`, `Music`, and `Cars`
- `Kids` has the 3rd lowest mean rating which supports its decreasing trend in animes with 'Kids' genre produced yearly

### Studios vs Mean rating
`Studio` of anime vs `mean` rating of anime

![download](https://user-images.githubusercontent.com/100555522/164976848-e67da9a0-ae0c-4bc0-b047-288ca9fb447f.png)

- The studio that produced the highest mean rating is Studio Bind, followed by `Studio Signpost`, `Egg Firm`, `China Literature Limited`, and `CLAP`
- It is surprising that the top 5 most common studios in from 2000 to 2021 are not in the top 20 studios that produce the highest mean rating

### Relationship analysis
Relationship between `mean`, `rank`, `popularity`, `positive_viewership_fraction`, and `negative_viewership_fraction`

![download](https://user-images.githubusercontent.com/100555522/164976961-3b23df00-7711-4d21-8095-5482bf811bdd.png)
![download](https://user-images.githubusercontent.com/100555522/164977027-d8680924-9fef-477c-ab73-542df5c116fd.png)

- `mean` increases while `rank` decreases --> As rank improves, mean rating increases
- `mean` increases while `popularity` decreases --> As popularity improves, mean rating increases
- `rank` increases with `popularity` --> As rank worsens, popularity also worsens
- There isn't much correction between `mean`, `rank`, and `popularity` with `negative_viewership_fraction` and `positive_viewership_fraction`
