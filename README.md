# Advancing Tuberculosis Detection in Chest X-ray

Our project presents a Computer-Aided Diagnosis (CAD) system leveraging advanced deep learning and computer vision techniques to enhance diagnostic accuracy and reduce transmission risks associated with tuberculosis (TB). Employing the YOLOv7 (You Only Look Once, version 7) object detection architecture, our system accurately identifies regions of interest in chest X-rays indicative of TB. By utilizing Convolutional Neural Networks (CNNs) and YOLO models, we detect consolidation and cavitary patterns of TB lesions, respectively.

We conducted experiments on the TBX11K dataset, a publicly available dataset, where we addressed data imbalance through class weights and data augmentation techniques. This approach yielded promising results, with a mean average precision (mAP) of 0.587, demonstrating robust performance in detecting both obsolete pulmonary TB and active TB. 

Our CAD system not only advances diagnostic accuracy but also contributes to mitigating TB transmission risks. The ability to handle class imbalance underscores its potential for real-world TB detection applications.

Find Research Paper at https://www.mdpi.com/2078-2489/14/12/655

---

## Repository Contents

1. **Code:** Contains the source code for the CAD system implementation.
2. **Documentation:** Includes detailed documentation on system architecture, usage instructions, and dataset information.
3. **Data:** Contains the TBX11K dataset used for training and evaluation.
4. **Results:** Includes evaluation metrics, graphs, and visualizations showcasing the performance of the CAD system.
5. **References:** Lists relevant research papers, articles, and resources.

---

## Installation

### Clone repository
 - git clone https://github.com/AyurEye/AyurEye.git

### Create Virtual environment
 - python -m venv env

### Activate Virtual environment
source env/bin/activate (linux)
 - env\Scripts\activate (windows)


### Project Setup 
 - pip install -r requirements.txt

### RunServer 
 - python manage,py runserver 

---

## Result

After conducting our comprehensive experiments with image weights assignment, minority class augmentation, and evolving the hyperparameter, we achieved promising results for our TB detection model. The AP for the obsolete pulmonary TB class reached 0.499, while the AP for the active TB class achieved a value of 0.675. As a result, the mAP at an IoU threshold of 0.5 amounted to 0.587, as illustrated.

![Precision–recall curve for the model](https://www.mdpi.com/information/information-14-00655/article_deploy/html/images/information-14-00655-g014.png)

## Screenshots
![Screenshots](media/screenshots.png)

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/). 

Please review the license terms before using or reproducing any part of this project.

---
## Contact

For any inquiries or feedback, please contact [anurag.timilsina@gmail.com]