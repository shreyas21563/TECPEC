# SemEval-2024 Task 3 Subtask 1: Textual Emotion-Cause Pair Extraction in Conversations

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
