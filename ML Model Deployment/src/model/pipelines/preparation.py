import pandas as pd
import re
from model.pipelines.collection import load_data
from loguru import logger 

def prepare_data():
    logger.info("starting up preprocessing pipeline")
    # to prepare dataset we need: 
    #1. load the dataset
    data = load_data()
    #2. encode columns like balcony, parking etc
    data_encoded = encode_cat_cols(data)
    #3. parse the garden column
    df = parse_garden_col(data_encoded)

    return df

def encode_cat_cols(data):
    logger.info("encode categorical columns")

    return pd.get_dummies(data, 
                          columns = ['balcony',
                                    'parking', 
                                    'furnished', 
                                    'garage', 
                                    'storage'], 
                          drop_first=True)

def parse_garden_col(data):
    logger.info("parsing garden column")

    for i in range(len(data)):
        if data.garden[i]=='Not present':
            data.garden[i]=0
        else: 
            data.garden[i] = int(re.findall(r'\d+', data.garden[i])[0])
    return data 


