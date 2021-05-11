class WatermarkImage():
    file_name = '1'
    color_text = 'gray'
    original_image_path = file_name
    watermark_image_path = 'wm_' + file_name
    text = 'watermark'

    startpos=(50, 50)
    font_ratio=1
    fill_text=True
    fontfile="FiraCode-Light.ttf"

    color_dict = {
        'black': (0, 0, 0),
        'gray': (128, 128, 128),
        'white': (255, 255, 255)
    }

    color = color_dict.get(color_text, 'gray')
    def __init__(self):
        print('WI created')

    def __del__(self):
        # Прописать удаление файлов
        print('WI deleted')

