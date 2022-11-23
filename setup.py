import subprocess
import sys
import os
import locale

'''
    Uncomment these lines if you're useing linux or mac. 
'''

# print(locale.getdefaultlocale()[0])

# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# with open("requirements.txt", encoding=locale.getdefaultlocale()[1]) as requirements:
#     requirements = requirements.readlines()[0]
#     install(requirements)

import gdown

base = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists(os.path.join(base,'models/')):
    os.makedirs(os.path.join(base,'models'))

## Download TB diagnosis model
print("Downloading TB diagnosis model:")
url1 = 'https://drive.google.com/uc?id=1prDcwVc7nIPKQC6NZgYWaQGDPvTY-XR0'
output = os.path.join(base, "./models/tb_diagnosis_model.h5")
gdown.download(url1, output, quiet=False)
print("TB diagnosis model downloaded!!!!!!!!!!!!!!!!!!!!!!!!!")

### Download TB detection model
print("Downloading TB detection model:")
url2 = 'https://drive.google.com/uc?id=1FNv4CBjcc-mB5_VUfg7aQH7uRiBUxAHF'
output2 = os.path.join(base, "./models/tb_detection_model.h5")
gdown.download(url2, output2, quiet=False)
print("TB detection model downloaded!!!!!!!!!!!!!!!!!!!!!!!!!")