# TECPEC: Textual Emotion-Cause Pair Extraction in Conversations

## Overview

This project presents our submission to SemEval-2024 Task 3, Subtask 1, "Textual Emotion-Cause Pair Extraction in Conversation". We introduce a two-step pipeline architecture to identify emotion-cause pairs in textual conversations. Our team ranked **5th** out of 31 participating teams. 🎉🎉🎉

Check out the [SemEval-2024 Task 3 Leaderboard](https://codalab.lisn.upsaclay.fr/competitions/16141#results) for detailed rankings.

## Abstract

In this project, we aim to develop novel model architectures and employ novel techniques to improve the detection of textual emotions and their causes in conversations. The primary goal is to enhance human-computer interaction through better understanding and extraction of emotions and their causes in textual data.

## Project Structure

- **data/**: Contains the dataset used for training and evaluation.
- **models/**: Contains the model architectures and trained models.
- **scripts/**: Scripts for training, evaluation, and data preprocessing.
- **results/**: Contains the results and logs of model performance.
- **Report.pdf**: Detailed project report.
- **README.md**: This file.

## Methodology

### Task Definition

The task involves identifying emotion-cause pairs within conversations. Each conversation consists of multiple utterances from different speakers. An emotion-cause pair is defined as an emotion utterance along with its emotion category and the textual cause span in a specific cause utterance.

![image](https://github.com/user-attachments/assets/a3cf3004-68df-433f-baf3-5bb1f4dc070b)


### Pipeline Overview

The task pipeline comprises two stages:
1. **Emotion Recognition in Conversation (ERC)**: Classification of utterances into Ekman’s six emotions (anger, joy, surprise, disgust, fear, sadness) and a "neutral" label for non-emotion utterances.
2. **Cause-Emotion Extraction (CEE)**: Extraction of cause utterance corresponding to a target utterance based on its associated emotion using a Question-Answering model.

### Models

#### Emotion Recognition in Conversation (ERC)

- **Utterance Level**: We use transformer-based encoder architectures like BERT and RoBERTa with a classification head for emotion classification.
- **Conversational Level**: A GPT2-based architecture is used where the entire conversation serves as a single data point, and each utterance is labelled collectively.

#### Cause-Emotion Extraction (CEE)

We utilize a Question-Answering model based on the method proposed by Poria et al. to identify the causal span for a target non-neutral utterance.

## Dataset

The dataset contains conversations from the American sitcom F.R.I.E.N.D.S., annotated with emotion-cause pairs and emotion labels. The data distribution is as follows:
- **Training Set**: 1236 conversations with 12144 utterances.
- **Validation Set**: 138 conversations with 1475 utterances.
- **Testing Set**: 665 conversations with 6301 utterances.

## Experimental Setup

- **Sentence Embedding**: We use the `all-mpnet-base-v2` model from sentence-transformer to convert each utterance into a 768-dimensional vector.
- **BERT/RoBERTa**: We extract the output embedding corresponding to the last token of the target utterance and concatenate it with the original target utterance embedding for classification.
- **GPT2**: The whole conversation is fed into the GPT2 model, and the output embeddings are used for classification.
- **Question Answering Model**: We use the pre-trained `mrm8488/spanbert-finetuned-squadv2` model and fine-tune it for our task.

## Evaluation Metrics

### Emotion Recognition in Conversation (ERC)

- **Accuracy**: Number of Correct Predictions over Total Number of Predictions.
- **Weighted F1**: Average of class-wise F1 Score considering the proportion for each class in the dataset.
- **Macro F1**: Average of class-wise F1 Score without considering the proportion for each class.

### Cause-Emotion Extraction (CEE)

- **Strict Match**: The predicted span should be the same as the annotated span.
- **Proportional Match**: Considering the overlap proportion of the predicted span and the annotated one.

## ERC Performance on Validation Set

| Model                     | Accuracy | Macro F1 | Weighted F1 |
|---------------------------|----------|----------|-------------|
| BERT                      | 0.32     | 0.27     | 0.32        |
| RoBERTa                   | 0.31     | 0.27     | 0.30        |
| GPT2                      | 0.36     | 0.30     | 0.37        |
| Zero Shot GPT 4           | 0.38     | 0.12     | 0.28        |
| In Context Learning GPT 4 | 0.58     | 0.37     | 0.53        |

## Scores on Leaderboard

| ERC Model | Cause Model | weighted_strict_f1 | weighted_Proportional_f1 | strict_f1 | Proportional_f1 |
| --------- | ----------- | ------------------ | -------------------------| --------- |---------------- |
| GPT 2     | Simple Transformer QA (mrm8488/spanbert-finetuned-squadv2) | 0.1345 | 0.1767 | 0.1283 | 0.1626 |
| BERT      | Simple Transformer QA (mrm8488/spanbert-finetuned-squadv2) | 0.1318  | 0.1704 | 0.1267  | 0.1581  |
| RoBERTa   | Simple Transformer QA (mrm8488/spanbert-finetuned-squadv2) | 0.1314 | 0.1697 | 0.1301| 0.1629 |

## Ablation Study on Validation Set
| ERC Model | Cause Model | weighted_strict_f1 | weighted_Proportional_f1 | strict_f1 | Proportional_f1 |
| --------- | ----------- | ------------------ | -------------------------| --------- |---------------- |
| Ground truth | Simple Transformer QA (mrm8488/spanbert-finetuned-squadv2) | 0.3430 | 0.4612 | 0.3441 | 0.4594 |
| GPT 2     | Simple Transformer QA (mrm8488/spanbert-finetuned-squadv2) | 0.1153 | 0.1543 | 0.1135 | 0.1443|
| BERT      | Simple Transformer QA (mrm8488/spanbert-finetuned-squadv2) | 0.1181  | 0.1673 | 0.1148  |  0.1568 |
| RoBERTa   | Simple Transformer QA (mrm8488/spanbert-finetuned-squadv2) | 0.1132 | 0.1623 | 0.1123 | 0.1557 |

## Conclusion

Our exploration into Textual Emotion-Cause Pair Extraction in Conversations has provided a two-step pipeline that first assigns emotions to utterances in a conversation and then finds the cause for that emotion using a QA model. Despite our system’s commendable 5th place finish, the ablation study suggests further work on emotion recognition to bridge the gap to ground truth performance.

## Future Work

- Using state-of-the-art models for the ERC task.
- Developing more robust architectures for emotion recognition and cause extraction.
- Develop an end-to-end architecture that directly identifies the emotion-cause pair

## Authors
- Shreyas Kabra, CSAI, IIIT Delhi
- Parthiv A Dholaria, CSE, IIIT Delhi
- Kartik Singhal, CSAM, IIIT Delhi
- Lakshya, CSAM, IIIT Delhi

## References

-  S. Kumar, S. Dudeja, M. S. Akhtar, and T. Chakraborty, “Emotion flip
 reasoning in multiparty conversations,” IEEE Transactions on Artificial
 Intelligence, 2023.
-  S. Poria, N. Majumder, D. Hazarika, D. Ghosal, R. Bhardwaj, S. Y. B.
 Jian, P. Hong, R. Ghosh, A. Roy, N. Chhaya et al., “Recognizing emotion
 cause in conversations,” Cognitive Computation, vol. 13, pp. 1317–1332, 2021.
-  Z. Ding, R. Xia, and J. Yu, “End-to-end emotion-cause pair extraction
 based on sliding window multi-label learning,” in Proceedings of the
 2020 conference on empirical methods in natural language processing
 (EMNLP), 2020, pp. 3574–3583.
-  R. Xia and Z. Ding, “Emotion-cause pair extraction: A new task to
 emotion analysis in texts,” arXiv preprint arXiv:1906.01267, 2019.
-  P. Ekman, “Expression and the nature of emotion,” Approaches to
 emotion, vol. 3, no. 19, p. 344, 1984
