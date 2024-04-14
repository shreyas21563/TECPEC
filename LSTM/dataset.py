from torch.utils.data import Dataset
from load_pickel import *
import torch
import numpy as np
import sys
sys.path.append('../')
from utils import *

MAX_CONV_LEN = 30

# Defined index 7 for padding
class LSTM_Dataset_ERC(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        conversation = self.data[idx]['conversation']
        emotion_labels = [emotion2int[utterance['emotion']] for utterance in conversation]
        texts = [utterance['text'] for utterance in conversation]
        text_embeddings = [torch.from_numpy(sentence_embedding_matrix[utterance2int[preprocess_text(text)]]) for text in texts]

        # Padding
        if len(conversation) < MAX_CONV_LEN:
            text_embeddings += [torch.zeros_like(text_embeddings[0])] * (MAX_CONV_LEN - len(conversation))
            emotion_labels += [7] * (MAX_CONV_LEN - len(conversation))
            attention_mask = [1] * len(conversation) + [0] * (MAX_CONV_LEN - len(conversation))
        else:
            text_embeddings = text_embeddings[:MAX_CONV_LEN]
            emotion_labels = emotion_labels[:MAX_CONV_LEN]
            attention_mask = [1] * MAX_CONV_LEN
        
        text_embeddings = torch.stack(text_embeddings)
        emotion_labels = torch.LongTensor(emotion_labels)
        attention_mask = torch.from_numpy(np.array(attention_mask))
        
        return {
            'text': text_embeddings,
            'emotion_labels': emotion_labels,
            'attention_mask': attention_mask,
        }
