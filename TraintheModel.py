history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=10
)
