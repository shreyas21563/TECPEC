import torch
import torch.nn as nn
from load_pickel import *

class LSTM_Model_ERC(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, dropout=0.2):
        super(LSTM_Model_ERC, self).__init__()
    
        self.text_dropout = nn.Dropout(dropout)

        self.relu = nn.ReLU()
        
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, dropout=dropout, batch_first=True)

        self.fc = nn.Linear(hidden_size, len(emotion2int))

    def forward(self, text_embeddings):
        text_embeddings = text_embeddings.float().squeeze()
        text_embeddings = self.text_dropout(text_embeddings)
        output, _ = self.lstm(text_embeddings)
        output = self.fc(output)
        output = self.relu(output)
        return output