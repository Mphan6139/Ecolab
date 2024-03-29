import time
from msrest.exceptions import HttpOperationError
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry

# Replace with a valid key
prediction_key = "c3741dd758584195b3bcd4331c4ba6c0"
prediction_resource_id = "/subscriptions/bad6784e-798e-4bbc-89cf-cb5149375471/resourceGroups/Ecolab(Group)/providers/Microsoft.CognitiveServices/accounts/Ecolab-Prediction"
training_key = 'd898f79af8f84520994849cf82d4a6be'
ENDPOINT = "https://ecolab-prediction.cognitiveservices.azure.com/"
publish_iteration_name = "EcoIdentify"
test_image = './test_images/sample.jpg'
trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

# Create a new project
print("Get project...")
project = trainer.get_projects()[0]
print(project.id)

# Now there is a trained endpoint that can be used to make a prediction

with open(test_image, "rb") as image_contents:
    results = predictor.classify_image(
        project.id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))


