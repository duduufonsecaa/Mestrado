from PIL import Image, ImageOps
import os

modo = input('modo: \n')
path = r'C:\Users\marco\Desktop\Mestrado\Pesquisa\Pacientes_renome'

if (modo == 'Ops'):
    for path, subdir, files in os.walk(path):
        for name in files:
           img = Image.open(os.path.join(path,name))
           g = ImageOps.grayscale(img)
           g.save(os.path.join(r'C:\Users\marco\Desktop\Mestrado\Pesquisa\Patients_gray_Ops',name))

if (modo == 'L' or modo == 'l'):
    for path, subdir, files in os.walk(path):
        for name in files:
            img = Image.open(os.path.join(path,name))
            img.convert('L')
            img.save(os.path.join(r'C:\Users\marco\Desktop\Mestrado\Pesquisa\Patients_gray_L',name))

if (modo == 'channels'):
    for path, subdir, files in os.walk(r'C:\Users\marco\Desktop\Mestrado\Pesquisa\Pacientes_renome'):
        for img in files:
            img_rgb = Image.open(os.path.join(path,img))
           img_r = img_rgb.getchannel(0)
           img_g = img_rgb.getchannel(1)
           img_b = img_rgb.getchannel(2)
           new_image = Image.new('L', (img_g.size[0],img_g.size[1]), 0)
           new_image.paste(imgr,(0,0))
           new_image.paste(imgg,(img_g.size[0],0))
           new_image.paste(imgb,(img_g.size[0],0))
           new_image.save(os.path.join(r'C:\Users\marco\Desktop\Mestrado\Pesquisa\Patients_gray_channel',img))
