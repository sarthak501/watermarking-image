import cv2


def add_text_watermark(image_path, text, output_path, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=7, color=(192, 192, 192), thickness=7):
    
    image = cv2.imread(image_path)
    image_height, image_width, _ = image.shape

    
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_width, text_height = text_size
    center_x = int((image_width - text_width) / 2)
    center_y = int((image_height + text_height) / 2)

    
    cv2.putText(image, text, (center_x, center_y),
                font, font_scale, color, thickness)

    cv2.imwrite(output_path, image)

    print("Text watermark added successfully!")



if __name__ == "__main__":
   
    original_image_path = "a.jpg"
    output_image_path = "output_image_with_text_watermark.jpg"


    text = "Nature"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 7
    color = (192, 192, 192)  
    thickness = 7 

   
    add_text_watermark(original_image_path, text,
                       output_image_path, font, font_scale, color, thickness)
