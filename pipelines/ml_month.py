from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from utils import save_pipeline, read_data, split_data

EXCLUDE_COLUMNS = ['month','text']
PREDICT_COLUMNS = 'month'

weather_month_pipeline = Pipeline([('DTC', DecisionTreeClassifier(random_state=17, max_depth=12))])

# Train the model
def run_training():
    X, y = split_data(read_data('././data/weather_data_month.csv'), EXCLUDE_COLUMNS, PREDICT_COLUMNS)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=17)

    weather_month_pipeline.fit(X_train, y_train)
    save_pipeline('./pipelines/month_pipeline.pkl', pipeline_to_persist=weather_month_pipeline)

run_training()