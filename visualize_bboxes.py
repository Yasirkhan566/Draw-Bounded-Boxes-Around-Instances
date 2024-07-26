import cv2
import numpy as np

def xywh2xyxy(bbox):
    bbox[2] = bbox[2] + bbox[0]
    bbox[3] = bbox[3] + bbox[1]
    return bbox

def draw_bbox(image, bbox, color, format = ''):
    x0, y0, x1, y1 = bbox
    img_height, img_width, _ = image.shape
    print("image shape: ", image.shape)

    if format == 'yolo':
        x0 = int(x0 * img_width)
        y0 = int(y0 * img_height)
        x1 = int(x1 * img_width)
        y1 = int(y1 * img_height)

    elif format == 'coco':
        x0 = int(x0)
        y0 = int (y0)
        x1 = int(x0+x1)
        y1 = int(y0+y1)
    
    cv2.rectangle(image, (x0, y0), (x1, y1), color, 2)

def visualize_bboxes(image_path, yolo_bboxes, output_path, color):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Image not found at {image_path}")
        return

    # Draw YOLO bboxes in red
    for bbox in yolo_bboxes:
        draw_bbox(image, bbox, color=(0, 0, color), format = 'coco')

    # Save the image
    cv2.imwrite(output_path, image)
    print(f"Output saved to {output_path}")

# Example usage
if __name__ == "__main__":
    output_path = "output_image.jpg"
    image_path = '/media/user/data/datasets/ds_1/coco/images/test2017/1702137355354_377571_frame_4.jpg'

    # yolo_bboxes = [
    #     [0.6929540634155273, 0.2035525427924262, 0.7366128285725911, 0.2569419578269676],
    #     [0.5427604039510091, 0.2282517327202691, 0.6887627919514974, 0.43976468686704284]
    # ]

    detic_bboxes = [[
                202.14299344507762,
                137.18700448495363,
                21.686738814036943,
                31.688040726273115
            ]]

    visualize_bboxes(image_path, detic_bboxes, output_path, 255)
    # visualize_bboxes(output_path, detic_bboxes, output_path, 100)
