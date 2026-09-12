import sys
import numpy as np
import torch

def main():
    x = np.arange(100)
     #----------- use gpu if available else cpu------------
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print('Pytorch will use: ', device)
    #----convert numpy to tensor-----
    x_tensor = torch.from_numpy(x).float().to(device)
    print(type(x_tensor))

if __name__ == "__main__":
    sys.exit(int(main() or 0))
