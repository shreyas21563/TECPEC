# Architecture

<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/RoBERTa/Architecture.jpg" height="500" /
</div>

# Links

Model: https://drive.google.com/file/d/1h1xFzQijXI7rQDLjgatzbo4shZt7JKKZ/view?usp=drive_link <br> 
Sentence Embedding: https://drive.google.com/file/d/17XKike87FrCYHn1pHP00m2YgTJBrtEnb/view?usp=sharing

# Scores on Validation
## Classification Report
| Emotion | Precision | Recall | F1-Score | Support |
| ------- | --------- | ------ | -------- | ------- |
| Anger   | 0.24      | 0.32   |   0.27    |   192|
| Joy     | 0.33      |0.65    |  0.44    |   254|
| Fear    |0.10      |0.22    |  0.13      |  37|
| Disgust | 0.09      |0.31    |  0.14    |    42|
| Neutral | 0.63      |0.17   |  0.27     |  630|
| Surprise| 0.32      |0.38    |  0.34    |   184|
| Sadness | 0.35      |0.29    |  0.32     |  136|
|         |           |        |          |      |
|Accuracy |           |        |  0.31    | 1475 |
|macro avg |       0.29|      0.33      |0.27      |1475|
|weighted avg |       0.43|      0.31|      0.30|      1475|

## Confusion Matrix

<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/RoBERTa/plots/val_confusion_matrix.png" />
</div>

# Plots 

<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/RoBERTa/plots/macro_f1_train.png" width="500" />
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/RoBERTa/plots/macro_f1_val.png" width="500" />
</div>
<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/RoBERTa/plots/train_loss.png" width="500" />
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/RoBERTa/plots/val_loss.png" width="500" />
</div>
<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/RoBERTa/plots/weighted_f1_train.png" width="500" />
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/RoBERTa/plots/weighted_f1_val.png" width="500" />
</div>
