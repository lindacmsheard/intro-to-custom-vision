"""
A short script to download and re-upload images from a Custom Vision project to a brand new one.

@Author - Ethan Jones

@Date - 2022-03-22

References:
- https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/quickstarts/image-classification?tabs=visual-studio&pivots=programming-language-python
- https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/cognitive-services/Custom-Vision-Service/copy-move-projects.md#:~:text=Export%20the%20project%20Call%20ExportProjectusing%20the%20project%20ID,key%20and%20endpoint.%20curl%20-v%20-X%20GET%20%22%7Bendpoint%7D%2Fcustomvision%2Fv3.3%2FTraining%2Fprojects%2F%7BprojectId%7D%2Fexport%22
"""

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials

import os, time, uuid
import urllib.request
import json

def myprint(str_to_print):
    base = ">> [Custom Vision export -> import tool]       "
    print(f"{base}{str_to_print}")

############################################################################
# These need changing based on your own CV resource & local file structure #
ENDPOINT = "https://uksouth.api.cognitive.microsoft.com/"
TRAINING_KEY = ""
ORIGINAL_PROJECT_ID = ""
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
EXPORT_PATH = os.path.join(ROOT_PATH, "exported_images") # <- assumes folder exists
#############################################################################

credentials = ApiKeyCredentials(in_headers={"Training-key": TRAINING_KEY})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# exp = trainer.export_project(ORIGINAL_PROJECT_ID)
# myprint(exp.token) <- project token used when importing
# imp = trainer.import_project(exp.token)

images = trainer.get_tagged_images(ORIGINAL_PROJECT_ID) #Add tags as a list param here
tags_list = []

counter = 0
image_regions = {}

for image in images:
    regions_list = []
    image_dict = image.as_dict()
    image_tags = image_dict.get('tags')
    regions = image_dict.get('regions')
    for tag in image_tags:
        tag_name = tag.get('tag_name')
        if tag_name not in tags_list:
            tags_list.append(tag_name)
    for region in regions:
        regions_list.append([region.get('left'), region.get('top'), region.get('width'), region.get('height'), region.get('tag_name')]) #L,T,W,H
        #myprint([region.get('left'), region.get('top'), region.get('width'), region.get('height'), region.get('tag_name')])
    image_regions[f"image_{counter}.jpg"] = regions_list
    urllib.request.urlretrieve(image_dict.get("original_image_uri"), os.path.join(EXPORT_PATH, f"image_{counter}.jpg"))
    counter += 1

# Create a new project
myprint ("Creating project...")
obj_detection_domain = next(domain for domain in trainer.get_domains() if domain.type == "ObjectDetection" and domain.name == "General")
project = trainer.create_project("export->input test", domain_id=obj_detection_domain.id)
for tag in tags_list:
    trainer.create_tag(project.id, tag)

myprint("Adding images...")

image_list = []
counter = 0

project_tags_list = trainer.get_tags(project.id)
project_tags = {}

for tag in project_tags_list:
    project_dict_ = tag.as_dict()
    project_tags[project_dict_.get('name')] = project_dict_.get('id')

for image in images:
    regions_list = []
    file_name = "image_{}.jpg".format(counter)
    tags = image_regions[file_name]
    for tag in tags:
        left_, top_, width_, height_ = tag[0:-1]
        tag_name_ = tag[-1]
        tag_id_ = project_tags.get(tag_name_)
        regions_list.append(Region(tag_id=tag_id_, left=left_, top=top_, width=width_, height=height_))
    with open(os.path.join(EXPORT_PATH, file_name), "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), regions=regions_list))
    counter += 1

upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=image_list))
if not upload_result.is_batch_successful:
    myprint("Image batch upload failed.")
    for image in upload_result.images:
        myprint("Image status: ", image.status)
    exit(-1)