# Key-phrase-extraction-of-patent-documents


## <div align="center">Description</div>

This repository contains source code for parsing and extracting the Key phrases of the in-house collection of patent documents. Firstly, the patents stored in the XML documents are parsed, and the abstract of each patent is extracted. Furthermore, the RAKE NLTK algorithm is used to extract the key phrases from the text and stored them in a MySQL database. Each row consists of a document identifier and the extracted Key phrases of a patent. Lastly, the entire application is wrapped in a docker container.  


## <div align="center">Dataset</div>
 
Download the Dataset Here. [Patents Dataset](https://databricksexternal.blob.core.windows.net/hiring/patents.zip?sp=r&st=2021-10-07T23:09:03Z&se=2021-10-31T08:09:03Z&spr=https&sv=2020-08-04&sr=b&sig=uR36HP3kCEDY9aPc0mvZFzLnblodA9adxQRTYTc6O6M%3D). 


## <div align="center">Quick Start</div>


<details open>
<summary>Install</summary>

[**Python>=3.6.0**](https://www.python.org/) is required with all
[requirements.txt](https://github.com/jayanthvarma1501/Key-phrase-extraction-of-patent-documents/blob/main/requirements.txt) installed.
<!-- $ sudo apt update && apt install -y libgl1-mesa-glx libsm6 libxext6 libxrender-dev -->

```bash
$ git clone https://github.com/jayanthvarma1501/Key-phrase-extraction-of-patent-documents.git
$ cd Key-phrase-extraction-of-patent-documents
$ pip install -r requirements.txt
```

</details>

<details open>
<summary>Inference</summary>

Inference with YOLOv5 and [PyTorch Hub](https://github.com/ultralytics/yolov5/issues/36). Models automatically download
from the [latest YOLOv5 release](https://github.com/ultralytics/yolov5/releases).

```python
import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

# Images
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
```

</details>
