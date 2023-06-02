import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torchvision import transforms


def set_seed(seed, cuda_present):
  """ This is done to reproduce the results """
  torch.manual_seed(seed)
  if cuda_present:
    torch.cuda.manual_seed(seed)

def initialize_cuda(seed):
    """ This is used to run on GPU """

    # Check CUDA availability
    cuda_present = torch.cuda.is_available()
    print('GPU Available?', cuda_present)

    # Initialize seed
    set_seed(seed, cuda_present)

    # Set device
    device = torch.device("cuda" if cuda_present else "cpu")

    return cuda_present, device