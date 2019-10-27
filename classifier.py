from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
import cv2 as cv

def classify(image_path):
    # Replace with a valid key
    prediction_key = "c3741dd758584195b3bcd4331c4ba6c0"
    #prediction_resource_id = "/subscriptions/bad6784e-798e-4bbc-89cf-cb5149375471/resourceGroups/Ecolab(Group)/providers/Microsoft.CognitiveServices/accounts/Ecolab-Prediction"
    training_key = 'd898f79af8f84520994849cf82d4a6be'
    ENDPOINT = "https://ecolab-prediction.cognitiveservices.azure.com/"
    publish_iteration_name = "Ecolab3"
    test_image = image_path
    trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)
    predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)
    project = trainer.get_projects()[0]

    # Now there is a trained endpoint that can be used to make a prediction

    with open(test_image, "rb") as image_contents:
        results = predictor.classify_image(
            project.id, publish_iteration_name, image_contents.read())
        # Display the results.
        for prediction in results.predictions:
            return prediction.tag_name
    #sorted_results = sorted(result,key=lambda x : x[1])
    #return sorted_results[0][0]
def take_picture():
    camera = cv.VideoCapture(0)
    ret, frame = camera.read()
    # print(ret)
    cv.imshow("test", frame)
    img_name = "cv_frame.png"
    cv.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    camera.release()
    cv.destroyAllWindows()
    x = classify('./cv_frame.png')
    print(x)
    return x
