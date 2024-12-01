from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = './editedImgs'

#access the unedited photos:
for filename in os.listdir(path):
    #take the image 
    if filename.lower().endswith(('.jpeg', '.png', 'jpg')):
        img_path = os.path.join(path, filename)
        img = Image.open(img_path)

    #apply filters
    edit = img.filter(ImageFilter.SHARPEN).convert("L").rotate(-180)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    #extract the filename without its extension--> save edited img with same base name but diff suffix/file type--> img.jpg--> ('img', 'jpg' and we access only the imgae portion [0])
    clean_name = os.path.splitext(filename)[0]
    
    output_path = os.path.join(pathOut, f"{clean_name}_edited.jpg")
    edit.save(output_path)