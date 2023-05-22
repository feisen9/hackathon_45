from PIL import Image
import io
import base64


def imagefile_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string


def base64_to_imagefile(base64_str, output_path, maxsize=1000, quality=85):
    img_data = base64.b64decode(base64_str)
    img = Image.open(io.BytesIO(img_data))

    # 进行压缩
    img.thumbnail((maxsize,maxsize))  # 参数是一个元组，表示压缩后的最大宽度和高度
    img.save(output_path, format='JPEG', quality=quality)


