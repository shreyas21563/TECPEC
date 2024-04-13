import pickle

with open('pickle_files/sentence_embedding_matrix.pkl', 'rb') as f:
    sentence_embedding_matrix = pickle.load(f)

with open('pickle_files/utterance2int.pkl', 'rb') as f:
    utterance2int = pickle.load(f)
with open('pickle_files/int2utterance.pkl', 'rb') as f:
    int2utterance = pickle.load(f)

with open('pickle_files/speaker2int.pkl', 'rb') as f:
    speaker2int = pickle.load(f)
with open('pickle_files/int2speaker.pkl', 'rb') as f:
    int2speaker = pickle.load(f)

with open('pickle_files/emotion2int.pkl', 'rb') as f:
    emotion2int = pickle.load(f)
with open('pickle_files/int2emotion.pkl', 'rb') as f:
    int2emotion = pickle.load(f)