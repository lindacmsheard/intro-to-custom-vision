# Introduction to Computer Vision

## Pre-requisites
- Access to an Azure subcription, with contributor rights to at least one resource group.

## Review the sample data in this repo
- [./sampledata/Ozgenel2019](./sampledata/Ozgenel2019) is from *2018 – Özgenel, Ç.F., Gönenç Sorguç, A. “Performance Comparison of Pretrained Convolutional Neural Networks on Crack Detection in Buildings”, ISARC 2018, Berlin.* The full dataset can be downloaded to local machine with the script [./data/fetch_Ozgenel2018_data_to_local.sh].

- [./sampledata/RDD2020](./sampledata/RDD2020) contains a subset of road images from the Czech Republic, from *Arya D, Maeda H, Ghosh SK, Toshniwal D, Sekimoto Y. RDD2020: An annotated image dataset for automatic road damage detection using deep learning. Data Brief. 2021 May 12;36:107133. doi: 10.1016/j.dib.2021.107133. PMID: 34095382; PMCID: PMC8166755.*

> Note that any subdirectory in the [./data](./data) folder will be gitignored, so this location is suitable for storing larger datasets locally


## [optional] Provision a Cognitive Services Resource in Azure 

Use of the Custom Vision Portal and API requires a cognitive services resource.

> 💡 You can skip this section if you want to provision this from within the custom vision interface in the next step. 

Azure Cognitive Services are cloud-based services that encapsulate artificial intelligence capabilities you can incorporate into your applications. You can provision individual cognitive services resources for specific APIs (for example, Language or Computer Vision), or you can provision a general Cognitive Services resource that provides access to multiple cognitive services APIs through a single endpoint and key. In this case, you'll use a single Cognitive Services resource.

1. Open the Azure portal at https://portal.azure.com, and sign in using the Microsoft account associated with your Azure subscription.
2. Select the ＋Create a resource button, search for cognitive services, and create a Cognitive Services resource with the following settings:
  - Subscription: Your Azure subscription
  - Resource group: Choose or create a resource group (if you are using a restricted subscription, you may not have permission to create a new resource group - use the one provided)
  - Region: Choose any available region
  - Name: Enter a unique name
  - Pricing tier: Standard S0
3. Select the required checkboxes and create the resource.
4. Wait for deployment to complete, and then view the deployment details.
5. Go to the resource and view its Keys and Endpoint page. This page contains the information that you will need to connect to your resource and use it from applications you develop. Specifically:
  - An HTTP endpoint to which client applications can send requests.
  - Two keys that can be used for authentication (client applications can use either key to authenticate).
  - The location where the resource is hosted. This is required for requests to some (but not all) APIs.

### See also
- [Provision and manage Azure Cognitive Services](https://docs.microsoft.com/en-us/learn/paths/provision-manage-azure-cognitive-services/)
- [Quickstart: Create a Cognitive Services resource using the Azure portal](https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account)
- [MicrosoftLearning/AI-102-AIEngineer](https://github.com/MicrosoftLearning/AI-102-AIEngineer/blob/master/Instructions/01-get-started-cognitive-services.md)



## Log in to the Computer Vision studio

👉 [https://www.computervision.ai](https://computervision.ai)


## Create a Classification Model
Use the provided Ozgenel2018 dataset to create a concrete crack classification model.

> 💡 You can use your own dataset, but we suggest using a datset that has been chipped up in a similar way to the provided sample.

Follow the instructions to do so via the Custom Vision studio interface here:
- https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/getting-started-build-a-classifier 

Use the `Quick Training` Method.

Refer to this page to choose a domain model to use for transfer learning:

- [Selecting a Domain Model](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/select-domain)


### Discuss
1. What is the experience of creating a training data set?
2. What issues can you foresee with the provided sample dataset
3. How would you interpret the model performance metrics
3. How might you improve the training data strategy

### See also
- [Create a Classification Model programmatically](https://docs.microsoft.com/en-us/azure/cognitive-services/Custom-Vision-Service/quickstarts/image-classification)



## Create an Object Detection Model
Use the provided RD2020 dataset sample to create a Road Damage object detection model.

You can also use your own dataset instead. 

Follow the instructions to do so via the Custom Vision studio interface here:
- https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/get-started-build-detector


### Discuss
1. What is the experience of creating a training data set?
2. What issues can you foresee with the provided sample dataset?
3. How would you interpret the model performance metrics?
4. Which of your two models would you have more confidence in at this point in time?

### See also
- [Create an Object Detection Model programmatically](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/quickstarts/object-detection)




## Azure Resources

### AzureML
- https://github.com/retkowsky/AutoMLforImages - with crack detection sample (Status: Public preview)
- https://docs.microsoft.com/en-us/azure/machine-learning/how-to-auto-train-image-models
- https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-automl-small-object-detect - using tiling



### Quickstarts and Tutorials
- https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ImageAnalysisQuickstart.py
- 






## Further Resources for the Crack and Defect Detection Domains

### 3rd Party Image Labelling and Data Management
### iMerit
- iMerit has API integration for workflow management around labelling, including for segmentation
- https://imerit.net/datastudio/edgecase/

### Research Domain
#### Road Damage
- https://blog.issart.com/concrete-crack-detection-using-deep-learning-and-computer-vision/
- [Global Road Damage Detection Challenge 2020](https://rdd2020.sekilab.global/)
- [RoadDamageDetector](https://github.com/sekilab/RoadDamageDetector)

#### Remote Sensing of Building Damage post disaster
- https://www.researchgate.net/publication/349831785_Building_Damage_Detection_Using_U-Net_with_Attention_Mechanism_from_Pre-_and_Post-Disaster_Remote_Sensing_Datasets
- https://www.researchgate.net/publication/347526564_Post-Disaster_Building_Damage_Detection_from_Earth_Observation_Imagery_Using_Unsupervised_and_Transferable_Anomaly_Detecting_Generative_Adversarial_Networks

 
#### Other
- [Advances in Computer Vision-Based Civil Infrastructure Inspection and Monitoring (2019)](https://www.sciencedirect.com/science/article/pii/S2095809918308130)
- [Detection of Surface Cracks in Concrete Structures using Deep Learning](https://towardsdatascience.com/detection-of-surface-cracks-in-concrete-structures-using-deep-learning-f8f85cd8ac8b)

### OSS Code & Data assets
- [Road Damage Dataset & Tutorial](https://github.com/sekilab/RoadDamageDetector/blob/master/RoadDamageDatasetTutorial.ipynb)

- [Road Damage Dataset (RDD2020) - 26k images](https://data.mendeley.com/datasets/5ty2wb6gvg/1)
- [RDD2020 - accompanying article with data links](https://github.com/sekilab/RoadDamageDetector)

- [Crack detection for masonry surfaces](https://github.com/dimitrisdais/crack_detection_CNN_masonry)
- [Concrete Crack Images for Classification](https://data.mendeley.com/datasets/5y9wdsg2zt/2)

- [xBD dataset (pre & post disaster)](https://github.com/DIUx-xView/xView2_baseline)
