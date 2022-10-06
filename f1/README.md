# Formula 1

## Basic Notes
* Useful data for a machine learning model would be telemetry data only
* Telemery data can be huge and detailed, with lots of variables
* Choosing what to predict as a research question can be challenging
* Seems more like something to create a descriptive analysis of, than predictive

## Kaggle Dataset Evaluation

### [Kaggle Formula 1 Race Data](https://www.kaggle.com/datasets/cbhavik/formula-1-ml-classifier)

* This dataset contains historical data on drivers, constructors, circuits, etc.
* The most granular information from this dataset involves lap times for each race per driver
* Cannot make a useful model on lap times alone, and historical data beyond a few years is irrelevant given the rule changes of the sport.

### [Formula 1 Race Events](https://www.kaggle.com/datasets/jtrotman/formula-1-race-events)

* Dataset contains laps where safety car was deployed, fatalities occurred, etc  historically.
* Can only be used as a supplementary dataset

### [Detailed Esports Weather Data - FormulaAIHackathon](https://www.kaggle.com/datasets/oracledevrel/formulaaihackathon2022)

* Only esports data of simulated rainfall for f1 esports, may not be super relevant

### [F1 Tweets](https://www.kaggle.com/datasets/kaushiksuresh147/formula-1-trending-tweets)

* Tweet-level data and is huge. Can be really useful as a supplementary dataset to see pre-race and post-race tweets and if they have an effect on outcomes. Ex: general sentiment of driver vs. driver standings in a race

## Non-Kaggle Dataset Evaluation

### [Fast F1 Package](https://theoehrly.github.io/Fast-F1/)

* Pretty cool python package that allows access to deep formula 1 telemetry data across laps, corners, etc on dimensions like throttles, brakes, speed

### [Sports Radar API](https://developer.sportradar.com/docs/read/racing/Formula_1_v2#formula-1-api-overview)

* Detailed API, may incur additional cost

### [Ergast Sports Developer API](https://ergast.com/mrd/)

* Detailed API, may incur additional cost
