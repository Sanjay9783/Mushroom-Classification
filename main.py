'''
import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
dataBase = client["neurolabDB"]

# Collection  Name
collection = dataBase['Products']

# Sample data
d = {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'}

# Insert above records in the collection
rec = collection.insert_one(d)

# Lets Verify all the record at once present in the record with all the fields
all_record = collection.find()

# Printing all records present in the collection
for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")
'''

##############################################
from mushroom_classification.pipeline.training_pipeline import start_training_pipeline
# from mushroom_classification.pipeline.batch_prediction import start_batch_prediction

# file_path="/config/workspace/aps_failure_training_set1.csv"

print(__name__)


if __name__=="__main__":
     try:
          start_training_pipeline()
          #output_file = start_batch_prediction(input_file_path=file_path)
          #print(output_file)
     except Exception as e:
          print(e)
