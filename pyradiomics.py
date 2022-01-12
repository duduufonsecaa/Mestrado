from __future__ import print_function
import SimpleITK as sitk
import radiomics
from radiomics import featureextractor
from datetime import datetime
import os

image = []
#mask = []
mask_split = []

# Get some test data

# Download the test case to temporary files and return it's location. If already downloaded, it is not downloaded again,
# but it's location is still returned.
#imageName, maskName = radiomics.getTestCase('brain1')

for path, subdir, files in os.walk(r'C:\Users\marco\Desktop\Mestrado\Pesquisa\images'):
    for images in files:
        image.append(os.path.join(r'C:\Users\marco\Desktop\Mestrado\Pesquisa\images',images))
        

#for path, subdir, files in os.walk(r'C:\Users\marco\Desktop\Mestrado\Pesquisa\masks'):
    for masks in files:
        mask.append(os.path.join(r'C:\Users\marco\Desktop\Mestrado\Pesquisa\masks',masks))
        mask_split.append(images.split('.nrrd'))
        


for i in range (len(image)):
    imageName = image[i]
    maskName = mask[i]
  
    print('image = ',image[i])
    print('nome = ',mask_split[i][0])



    if imageName is None or maskName is None:  # Something went wrong, in this case PyRadiomics will also log an error
        print('Error getting testcase!')
        exit()



  # Define settings for signature calculation
  # These are currently set equal to the respective default values
    settings = {}
    settings['binWidth'] = 25
    settings['resampledPixelSpacing'] = None  # [3,3,3] is an example for defining resampling (voxels with size 3x3x3mm)
    settings['interpolator'] = sitk.sitkBSpline




  # Initialize feature extractor
    extractor = featureextractor.RadiomicsFeatureExtractor(**settings)

  # By default, only original is enabled. Optionally enable some image types:
    extractor.enableAllImageTypes()




    extractor.disableAllFeatures()
    extractor.enableFeatureClassByName('firstorder')
    extractor.enableFeatureClassByName('glcm')
    extractor.enableFeatureClassByName('gldm')
    extractor.enableFeatureClassByName('glrlm')
    extractor.enableFeatureClassByName('glszm')
    extractor.enableFeatureClassByName('ngtdm')


    texto = open(os.path.join(r'C:\Users\marco\Desktop\Mestrado\Pesquisa\Resultados',mask_split[i][0]+'.txt'),'w+')


    texto.write(f"Calculating features - hora: {datetime.now().strftime('%H:%M:%S')}\n")
    featureVector = extractor.execute(imageName, maskName)



    for featureName in featureVector.keys():
        texto.write("Computed %s: %s" % (featureName, featureVector[featureName]))
    texto.write(f"Finished - hora: {datetime.now().strftime('%H:%M:%S')}\n")
    texto.close()


