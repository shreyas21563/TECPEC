# Architecture

<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/BERT/Architecture.jpg" height="500" />
</div>

# Links

Model: https://drive.google.com/file/d/1e_X4LyNgheVhGmz7BAW1pKup1dGXkYzv/view?usp=sharing <br> 
Sentence Embedding: https://drive.google.com/file/d/17XKike87FrCYHn1pHP00m2YgTJBrtEnb/view?usp=sharing

# Scores on Validation
## Classification Report
| Emotion | Precision | Recall | F1-Score | Support |
| ------- | --------- | ------ | -------- | ------- |
| Anger   | 0.26      | 0.27   |  0.27    |   192 |
| Joy     | 0.35      | 0.61    |  0.45|       254|
| Fear    | 0.07      | 0.16    |  0.10|        37|
| Disgust | 0.08      |0.24     | 0.12|        42|
| Neutral | 0.56      |0.21     | 0.31|       630|
| Surprise| 0.31      |0.39     | 0.35|       184|
| Sadness | 0.25      |0.32     | 0.28|       136|
|         |           |        |          |      |
|Accuracy |           |        |  0.32    | 1475 |
|macro avg |       0.27|      0.31  |    0.27  |    1475|
|weighted avg |       0.40|      0.32|      0.32|      1475|
## Confusion Matrix
<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/BERT/plots/val_confusion_matrix.png" />
</div>

# Plots 

<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/BERT/plots/macro_f1_train.png" width="500" />
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/BERT/plots/macro_f1_val.png" width="500" />
</div>
<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/BERT/plots/train_loss.png" width="500" />
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/BERT/plots/val_loss.png" width="500" />
</div>
<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/BERT/plots/weighted_f1_train.png" width="500" />
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Utterance_Level/BERT/plots/weighted_f1_val.png" width="500" />
</div>
