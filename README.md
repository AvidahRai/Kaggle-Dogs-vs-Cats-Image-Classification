# Kaggle-Dogs-vs-Cats-Image-Classification
Using Kaggle Dogs vs Cats to experiment with different Image Classification architectures

This repository contains a set of experiments performed on Dogs vs Cats image dataset downloaded from https://www.kaggle.com/c/dogs-vs-cats/data.

<b>Hardware Specifications</b>
|||
| ------------- | -----|
| CPU | Intel Core i5 9th Gen |
| GPU | Nvidia GTX 1650 4GB (Mobile) |
| RAM | 8GB 2700Hz Dual channel |
| Storage | M.2 SSD 250GB |

The models were built and trained using <b>Keras</b> and <b>Tensorflow GPU</b>

|Model| Parameters | Val Accuracy | Val Loss | Notes|
| ------------- | -----| -------- | -----| --- |
| LeNet5 | 1,311,246 | 74.17 | 0.2941 | Learning rate not set, Dropout rate not set, Batch Normalisation not set |
| AlexNet | 58,289,538 | 87.61 | 0.1535 | Learning rate not set, Dropout rate not set, Batch Normalisation not set |
| VGG-16 | 134,268,738 | N/A | N/A | Training not started because of insufficent memory on the graphic card |

<b>Future models</b>
1) VGG-13
2) GoogLeNet/Inception
3) ResNET50
4) ResNET100
