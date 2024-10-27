test_loss, test_accuracy = model.evaluate(validation_generator)
print(f"Validation Accuracy: {test_accuracy}")
print(f"Validation Loss: {test_loss}")
