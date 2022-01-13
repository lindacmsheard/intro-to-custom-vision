from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = "<your_subscription_key_here>"
endpoint = "<your_endpoint_url_here>"
REPO_PATH = os.path.dirname(os.path.realpath(__file__))

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
local_image_path = os.path.join (REPO_PATH, "<image_path_here_with_jpg_extension>")
local_image = open(local_image_path, "rb")

'''
Describe an Image - remote
This example describes the contents of an image with the confidence score.
'''
print("===== Describe an image - remote =====")
# Call API
description_results = computervision_client.describe_image_in_stream(local_image)

# Get the captions (descriptions) from the response, with confidence level
print("Description of remote image: ")
if (len(description_results.captions) == 0):
    print("No description detected.")
else:
    for caption in description_results.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))