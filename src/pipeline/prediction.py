import sys
import os
import pandas as pd

from src.exceptions import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join('artifacts','model.pkl')
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            model = load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("Features received for prediction:")
            print(features)
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,gender,ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score):
        self.gender=gender
        self.ethnicity=ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.ethnicity or "group A"],
                "parental level of education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],
                "reading score": [self.reading_score],
                "writing score": [self.writing_score],
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)
