from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from utils import save_pipeline, read_data, split_data

EXCLUDE_COLUMNS = ['day_end', 'day_start','text']
PREDICT_COLUMNS = 'day_end'

weather_day_start_pipeline = Pipeline([('RFC',
        RandomForestClassifier(n_estimators=51, random_state=17, n_jobs=-1,
                                oob_score=True, max_depth=34, max_features= 2
                               ))])

# Train the model
def run_training():
    X, y = split_data(read_data('../data/weather_data_days.csv'), EXCLUDE_COLUMNS, PREDICT_COLUMNS)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=17)

    weather_day_start_pipeline.fit(X_train, y_train)
    save_pipeline('./day_end_pipeline.pkl', pipeline_to_persist=weather_day_start_pipeline)

run_training()