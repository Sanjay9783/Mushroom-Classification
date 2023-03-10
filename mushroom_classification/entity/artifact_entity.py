from dataclasses import dataclass

'''
there are main 6 steps in this project 
    1-DataIngestion
    2-DataValidation
    3-DataTransformation
    4-ModelTrainer
    5-ModelEvaluation
    6-ModelPusher

this file will act as output file for each and every step
'''

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str

@dataclass
class DataTransformationArtifact:
    transform_object_path:str
    transformed_train_path:str
    transformed_test_path:str
    target_encoder_path:str

@dataclass
class ModelTrainerArtifact:
    model_path:str 
    f1_train_score:float 
    f1_test_score:float