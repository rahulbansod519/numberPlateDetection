import os
import cv2
import numpy as np
from psutil import win_service_get
import easyocr
import matplotlib.pyplot as plt
from db import dbEntry

def filter_text(region, ocr_result, region_threshold):
    rectangle_size = region.shape[0]*region.shape[1]
    plate = []
    for result in ocr_result:
        length = np.sum(np.subtract(result[0][1], result[0][0]))
        height = np.sum(np.subtract(result[0][2], result[0][1]))
        if length*height / rectangle_size > region_threshold:
            plate.append(result[1])
        return plate

def ocr_it(image, detections, detection_threshold, region_threshold):
    scores = list(filter(lambda x: x> detection_threshold, detections['detection_scores']))
    boxes = detections['detection_boxes'][:len(scores)]
    classes = detections['detection_classes'][:len(scores)]
    width = image.shape[1]
    height = image.shape[0]
    for idx,box in enumerate(boxes):
        roi = box*[height, width, height, width]
        region = image[int(roi[0]):int(roi[2]),int(roi[1]):int(roi[3])]
        reader = easyocr.Reader(['en'])
        ocr_result = reader.readtext(region)
        text = filter_text(region, ocr_result, region_threshold)
        plt.imshow(cv2.cvtColor(region, cv2.COLOR_BGR2RGB))
        return text
        
def save_results(csv_filename,text):
    # img_name = '{}.jpg'.format(uuid.uuid1())
#     cv2.imwrite(os.path.join(folder_path, img_name), region1)
    with open(csv_filename, mode='a', newline='') as f:
        if not text:
            pass
        else:
            num_plate = ""
            for i in text:
                num_plate+=i
            # csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # csv_writer.writerow([text])
            print(num_plate)
            print(type(num_plate))
            dbEntry(num_plate)
                
        