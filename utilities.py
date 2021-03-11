'''
    @file Utilies
    @description Contains utility (helper) functions
    @author Avinash Rai
    @datemodified 11/03/2021
'''
import tensorflow
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

'''
    Instantiate Training and Validation ImageDataGenerators and return them to be used in the Keras models. 
    @input | tuple | Tuple of image dimensions (Height X Width X RGB Channels)
    @train_folder_path | string | Folder name containing Training images
    @val_folder_path | string | Folder name containing Validation images
    @batch_size | int | Batch size
    @return Keras ImageDataGenerator, Keras ImageDataGenerator
''' 
def get_train_val_iterator(input_shape, train_folder_path, val_folder_path, batch_size=64):

    dataGenerator = ImageDataGenerator( rescale=1.0/255.0)

    train_iterator = dataGenerator.flow_from_directory(
        directory = train_folder_path,
        color_mode = 'rgb',
        class_mode = 'binary',
        batch_size = 64,
        target_size = (input_shape[0], input_shape[1])
    )
    val_iterator = dataGenerator.flow_from_directory(
        directory = val_folder_path,
        color_mode = 'rgb',
        class_mode = 'binary',
        batch_size = 64,
        target_size = (input_shape[0], input_shape[1])
    )    
    
    return train_iterator, val_iterator

'''
    Plot Figure of Training Accuracy and Loss
    @history | obj | Tensorflow fit Scalar 
    @return None
'''    
def plot_training_history( fit_history ):
    plt.subplots(2,2,figsize=(15,5))
    plt.subplot(1,2,1)
    plt.plot(fit_history.history['accuracy'], label='Train', color="blue")
    plt.plot(fit_history.history['val_accuracy'], label='Validation', color="green")
    plt.legend(loc="upper left")
    plt.title("Accuracy")
    plt.subplot(1,2,2)
    plt.plot(fit_history.history['loss'], label='Train', color="blue")
    plt.plot(fit_history.history['val_loss'], label='Validation', color="green")
    plt.legend(loc="upper left")
    plt.title("Loss")
    plt.show()