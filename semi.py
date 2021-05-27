import torch
import numpy as np
import os
from pathlib import Path

if __name__ == "__main__":
	print(torch.__version__)
	for i in range(10):
		print(i)
	
	a = torch.FloatTensor([10])
	b = torch.randn((512,512,3))

