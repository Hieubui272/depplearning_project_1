from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Initialize ImageDataGenerator with validation split
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

# Training data generator
train_generator = datagen.flow_from_dataframe(
    dataframe=labels_df,
    directory='/content/G1020/Images',
    x_col='imageID',
    y_col='binaryLabels',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

# Validation data generator
validation_generator = datagen.flow_from_dataframe(
    dataframe=labels_df,
    directory='/content/G1020/Images',
    x_col='imageID',
    y_col='binaryLabels',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)
