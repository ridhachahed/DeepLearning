import torch.nn as nn
import numpy as np

NB_SAMPLES = 1000
DATA_DIR = './data'

NUMBER_OF_CLASSES = 10

WIDTH_HEIGHT = 14
SINGLE_IMAGE_SIZE = WIDTH_HEIGHT * WIDTH_HEIGHT
DOUBLE_IMAGE_SIZE = 2 * SINGLE_IMAGE_SIZE

# ----Train Config-----#
LEARNING_RATE = 0.001
TRAIN_BATCH_SIZE = 5
EPOCHS = 20

# ----AuxLoss Config-----#
ALPHA = 0.5
BEST_ALPHA = 0.22

# ----Search Config-----#
KERNEL_SIZES = [3,5]
NB_CHANNELS = [4,8,16,24,48]
FCNEURONS = [32,64,128, 256,512]
NB_LAYERS = [1, 2, 3]
ALPHAS = np.linspace(0, 1, 10)

#----Test Config-----#
TEST_BATCH_SIZE = NB_SAMPLES

#----BasicNet Config-----#
BASIC_NET_HIDDEN_LAYER = 512
BASIC_NET_NB_HIDDEN = 1
BASIC_LEARNING_RATE = 0.00001

#----FCN Config-----#
FCN_HIDDEN_LAYER = 64
FCN_NB_HIDDEN = 1

#----CNN Config-----#
CNN_HIDDEN_LAYER = 64
CNN_BASE_CHANNEL_SIZE = 4
CNN_NB_HIDDEN = 1
CNN_KERNEL_SIZE = 3

CNN_BEST_HIDDEN = 64
CNN_BEST_CHANNEL = 48
CNN_BEST_KERNEL_SIZE = 3

#----SiameseNet Config-----#
SIAMESE_NET_HIDDEN_LAYER = 128
SIAMESE_NET_NB_HIDDEN = 2