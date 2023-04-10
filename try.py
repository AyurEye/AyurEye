from roboflow import Roboflow


api_key="TBEC47mwgYHscWpwnyue"

rf = Roboflow(api_key=api_key)

project = rf.workspace("kathmandu-university-hqa4p").project("lungabnormalitiesdetection")
model = project.version(1).model

# infer on a local image
preds = model.predict("test3.jpg", confidence=40, overlap=30)
# print(preds)

detections = preds.json()['predictions']# visualize your prediction
dict={}
if detections ==[]:
    print("No disease")

else:
    print(detections[0])
    print(type(detections[0]))
    next((item for item in detections), None)
    dict.



# visualize your prediction
preds.save("prediction.jpg")