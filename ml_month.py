import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from  utils import save_pipeline

def read_data(path):
    return pd.read_csv(path+'weather_data_month.csv')


def split_data(data):

    X = data.drop('month', axis=1)
    y = data['month'].astype('int64')

    return X, y


weather_month_pipeline = Pipeline(['DTC', DecisionTreeClassifier(random_state=17, max_depth=12)])


# Train the model
def run_training():
    X, y = split_data(read_data('./'))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=17)

    weather_month_pipeline.fit(X_train, y_train)
    save_pipeline('./', 'month_pipeline.pkl', pipeline_to_persist=price_pipe)