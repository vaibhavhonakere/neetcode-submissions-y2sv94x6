import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)
        self.firstLayer = nn.Linear(784, 512)
        self.projection = nn.Linear(512, 10)
        self.dropout = nn.Dropout(p=0.2)
        self.sigmoid = nn.Sigmoid()
        self.relu = nn.ReLU()
        # Define the architecture here
    
    def forward(self, images: TensorType[float]) -> TensorType[float]:
        torch.manual_seed(0)
        ret = self.sigmoid(self.projection(self.dropout(self.relu(self.firstLayer(images)))))
        return torch.round(ret, decimals=4)
        # Return the model's prediction to 4 decimal places
