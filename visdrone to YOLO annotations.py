import os
from os import listdir
from os.path import isfile, join
from PIL import Image

image_dir = "/images_directory/"
annotation_dir = "/annotations_directory/"
output_dir = "/output_directory/"


def transform_annotation(image_size, bbox):
    width_div = 1.0 / image_size[0]
    height_div = 1.0 / image_size[1]
    return [(bbox[0] + bbox[2] / 2) * width_div, (bbox[1] + bbox[3] / 2) * height_div, bbox[2] * width_div,
            bbox[3] * height_div]


# Read all files in the annotations directory and make a list
all_files = [file_name for file_name in listdir(annotation_dir) if isfile(join(annotation_dir, file_name))]

for file in all_files:

    basename = os.path.basename(file)
    file_picked = os.path.splitext(basename)[0]

    with open(annotation_dir + file, 'r', encoding='utf8') as f:
        img = Image.open(image_dir + file_picked + '.jpg')

        for line in f:

            data = line.strip().split(',')  # CSV file
            class_label = int(data[5]) - 1  # 5th element in the CSV line is the class label and value ranges from 0-9

            considered = data[4]  # Check if current annotation should be  considered

            if (considered != str(0)) and (class_label >= 0) and (class_label <= 9):  # Check for valid classes
                bbox_original = [float(x) for x in data[:4]]
                yolo_bbox = transform_annotation(img.size, bbox_original)
                bounding_box_string = " ".join(
                    [str(x) for x in yolo_bbox])  # Create the annotation string to be written

                with open(output_dir + file, 'a+', encoding="utf-8") as output_file:
                    output_file.write(f"{class_label} {bounding_box_string}\n")