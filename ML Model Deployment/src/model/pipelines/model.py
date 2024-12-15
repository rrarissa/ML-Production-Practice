import pickle as pk
from model.pipelines.preparation import prepare_data
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from config.config import settings
from loguru import logger


def build_model():
    logger.info("starting up model building pipeline")

    data = prepare_data()
    # identify X and y
    X, y = get_X_y(data)
    # split the dataset
    X_train, X_test, y_train, y_test = split_train_test(X, y)
    # train the model
    rf = train_model(X_train, y_train)
    # evaluation
    score = evaluation_model(rf, X_test, y_test)
    print(f'Models score = {score}')
    # 6. save the model in a configuration file
    save_model(rf)


def get_X_y(data):
    X = data[['area', 
              'construction_year', 
                 'bedrooms', 
                  'garden', 
                  'balcony_yes', 
                  'parking_yes', 
                  'furnished_yes', 
                  'garage_yes', 
                  'storage_yes']]
    
    y = data.rent
    logger.info(f"defining X and Y variables. \nX vars: {X}\ny var: {y}")
    return X, y


def split_train_test(X, y):
    logger.info("splitting data into train and test sets")

    X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.2)
    return X_train, X_test, y_train, y_test 


def train_model(X_train, y_train):
    logger.info("training a model with hyperparameters")

    grid_space = {'n_estimators': [100, 200, 300], 
                  'max_depth': [3, 6, 9, 12]}
    
    grid = GridSearchCV(RandomForestRegressor(), 
                        param_grid=grid_space, 
                        cv=5, 
                        scoring='r2')
    
    model_grid = grid.fit(X_train, y_train)

    return model_grid.best_estimator_


def evaluation_model(model, X_test, y_test):
    logger.info(f"evaluating model performance. SCORE={model.score(X_test, y_test)}")

    return model.score(X_test, y_test)


def save_model(model):
    logger.info(f"saving a model to a directory: {settings.model_path}/{settings.model_name}")

    pk.dump(model, open(f'{settings.model_path}/{settings.model_name}', 'wb'))

