# ERA1-Session5
## Session 5 Assignment of ERA 1 program from  TSAI "The School of AI"

### About this Assignment

To create a simple CNN based model using pytorch framework. Intention here is to make the code modular.
Model is included in model.py and utility functions are included in utils.py, these modules are imported in main S5.ipynb file.

Dataset = MNIST

Batch size = 512

No of parameters in model = 593, 200

Number of epoch = 20

Optimizer = SGD

Learning rate = 0.01

Test Accuracy = 99.6 %

### Framework and main libraries used

Framework = Pytorch

Model trained on = Google colab

Main libraries used stated below:

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

### Organization - Modular Files

CNN Model class Net is defined in model.py

Utility function like initialize_cuda is defined in utils.py. This function checks if gpu is available, if so sets the device to gpu else on cpu..

Main file is S5.pynb, which imports the module model and utils

Though not implemented here utils.py can also contain transforms code, accuracy function, graphs etc

### Model Parameters

No of parameters in model = 593, 200

/assets/images/Model Summary.png

Model Summary.png

### Accuracy of the model

Test Accuracy = 99.6 %

### Future improvements

In the current code, train and test function is included in main ipynb file, future scope of improvement is to modularize these functions, either move train and test function in model.py or create seperate train.py and test.py files.

### Assignment submitted by

Samir Paul
