import torch 
import torch.nn as nn
from torch.optim import SGD 
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchvision
import numpy as np 
import matplotlib.pyplot as plt

x,y = torch.load('C:\Users\Seiven\Desktop\MY_MLmodels\MNIST_practice\MNIST\processed\training.pt')


""" plt.imshow(x[2].numpy()) """