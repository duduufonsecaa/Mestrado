import SimpleITK as sitk
import os
from PIL import Image
path = r'C:\Users\marco\Desktop\Mestrado\Pesquisa\Patients_gray_L'
print('beggining the converting\n')
for path, subdir, files in os.walk(path):
    for name in files:
        names = name.split(".JPG")        
        im = sitk.ReadImage(os.path.join(path,name))
        sitk.WriteImage(im, os.path.join(r'C:\Users\marco\Desktop\Mestrado\Pesquisa\images',names[0])+'.nrrd')
print('finished the conversion\n')
