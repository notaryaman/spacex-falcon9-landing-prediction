# SpaceX Falcon 9 First Stage Landing Prediction

IBM Data Science Professional Certificate – Applied Data Science Capstone.

The goal is to predict whether the Falcon 9 first stage will land successfully. A successful landing lets SpaceX reuse the booster, which is the main reason a Falcon 9 launch costs about $62 million while other providers charge upwards of $165 million.

## Notebooks

| # | Step | File |
|---|------|------|
| 1 | Data collection with the SpaceX REST API | [1_spacex_data_collection_api.ipynb](1_spacex_data_collection_api.ipynb) |
| 2 | Data collection with web scraping (Wikipedia) | [2_spacex_webscraping.ipynb](2_spacex_webscraping.ipynb) |
| 3 | Data wrangling and landing label | [3_spacex_data_wrangling.ipynb](3_spacex_data_wrangling.ipynb) |
| 4 | Exploratory data analysis with SQL | [4_spacex_eda_sql.ipynb](4_spacex_eda_sql.ipynb) |
| 5 | Exploratory data analysis with visualization (+ extra insights) | [5_spacex_eda_visualization.ipynb](5_spacex_eda_visualization.ipynb) |
| 6 | Interactive launch site map with Folium | [6_spacex_launch_site_location_folium.ipynb](6_spacex_launch_site_location_folium.ipynb) |
| 7 | Interactive dashboard with Plotly Dash | [7_spacex_dash_app.py](7_spacex_dash_app.py) |
| 8 | Machine learning prediction | [8_spacex_machine_learning_prediction.ipynb](8_spacex_machine_learning_prediction.ipynb) |

Run the dashboard with `python 7_spacex_dash_app.py` and open http://127.0.0.1:8050.

## Key results

- 90 Falcon 9 launches analyzed (2010 to 2020); overall landing success 66.7%, and 87% when a landing was attempted.
- Landing success rose from 0% (2010 to 2013) to 90% in 2019.
- KSC LC-39A has the highest landing success ratio (76.9%).
- Best model: Support Vector Machine, 83.3% test accuracy and 84.8% cross-validation accuracy.

## Data

`dataset_part_1.csv` (collected launches), `dataset_part_2.csv` (with the `Class` label), `dataset_part_3.csv` (one-hot encoded features) and `spacex_web_scraped.csv`. Charts, map HTML files and dashboard screenshots are in `images/`.

Note: the public SpaceX API returned HTTP 525 when notebook 1 was run, so it falls back to IBM's published output of that step (the same 90 launches).
