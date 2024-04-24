# Architecture

<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Conversational_Level/Architecture.jpg" height="500" />
</div>

# Links

Model: https://drive.google.com/file/d/1kQD9KW1NYgTLwYK-QHMDBee4jEmVvJBR/view?usp=sharing <br> 
Sentence Embedding: https://drive.google.com/file/d/17XKike87FrCYHn1pHP00m2YgTJBrtEnb/view?usp=sharing

# Scores on Validation

## Classification Report
| Emotion | Precision | Recall | F1-Score | Support |
| ------- | --------- | ------ | -------- | ------- |
| Anger   | 0.27      | 0.26   |  0.26    |   192 |
| Joy     | 0.41      | 0.56   |   0.47   |   254 |
| fear    | 0.11      | 0.24   |  0.15    |   37 |
| Disgust | 0.07      | 0.21   |  0.11    |   42 |
| Neutral | 0.57      | 0.32   |  0.41    |   630 |
| Surprise| 0.32      | 0.42   |  0.36    |  184 |
| Sadness | 0.28      | 0.31   |  0.30    |  136 |
|         |           |        |          |      |
|Accuracy |           |        |  0.36    | 1475 |
|macro avg |       0.29   |   0.33     | 0.30  |    1475 |
|weighted avg |       0.42 |     0.36 |      0.37 |      1475 |

# Plots 

<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Conversational_Level/plots/macro_f1_train.png" width="500" />
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Conversational_Level/plots/macro_f1_val.png" width="500" />
</div>
<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Conversational_Level/plots/train_loss.png" width="500" />
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Conversational_Level/plots/val_loss.png" width="500" />
</div>
<div style="display: flex; flex-wrap: wrap;">
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Conversational_Level/plots/weigthed_f1_train.png" width="500" />
  <img src="https://github.com/parthivdholaria/NLP-Project-24/blob/Shreyas/ERC/ERC_Conversational_Level/plots/weigthed_f1_val.png" width="500" />
</div>
