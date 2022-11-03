import os
import matplotlib.pyplot as plt
import numpy as np

# ignore tensorflow & opencv debug & warning information by setting log level
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
from tensorflow import keras


def build_model(
    n_classes=1,
    hidden_layer_sizes=[],
    activation="relu",
    optimizer="SGD",
    learning_rate=0.01,
):
    """
    Args:
        n_classes: Number of output classes in the dataset.
        hidden_layer_sizes: A list with the number of units in each hidden layer.
        activation: The activation function to use for the hidden layers.
        optimizer: The optimizer to use (SGD, Adam).
        learning_rate: The desired learning rate for the optimizer.

    Returns:
        model: A tf.keras model (graph).
    """
    tf.keras.backend.clear_session()
    np.random.seed(0)
    tf.random.set_seed(0)

    model = tf.keras.Sequential()

    # INPUT LAYER
    model.add(tf.keras.layers.Flatten())

    # HIDDEN LAYER
    # add as many hidden layer and nodes as called for in the function signature
    for hidden_layer_size in hidden_layer_sizes:
        model.add(
            tf.keras.layers.Dense(
                units=hidden_layer_size,
                activation=activation,
                name="Hidden" + str(hidden_layer_size),
            )
        )

    # OUTPUT LAYER
    model.add(
        tf.keras.layers.Dense(units=n_classes, activation="sigmoid", name="Output")
    )

    opti = keras.optimizers.SGD(learning_rate=learning_rate)

    if optimizer == "Adam":
        opti = keras.optimizers.Adam(learning_rate=learning_rate)
    elif optimizer == "RMSprop":
        opti = keras.optimizers.RMSprop(learning_rate=learning_rate)

    model.compile(
        loss="binary_crossentropy",
        optimizer=opti,
        metrics=[tf.keras.metrics.Accuracy(), "Precision", "Recall"],
    )

    return model


def train_and_evaluate(
    hidden_layer_sizes=[],
    activation="tanh",
    optimizer="Adam",
    learning_rate=0.01,
    num_epochs=20,
    batch_size=32,
):

    # Build the model.
    model = build_model(
        n_classes=1,
        hidden_layer_sizes=hidden_layer_sizes,
        activation=activation,
        optimizer=optimizer,
        learning_rate=learning_rate,
    )

    X_train = np.array(images_training)
    # X_train = images_training
    Y_train = image_label

    X_test = np.array(images_test)
    # X_test = images_test
    Y_test = image_label_test

    # Train the model.
    print("Training...")
    history = model.fit(
        x=X_train,
        y=Y_train,
        epochs=num_epochs,
        batch_size=batch_size,
        validation_split=0,
        verbose=0,
    )

    # Retrieve the training metrics (after each train epoch) and the final test
    # accuracy.
    # history = pd.DataFrame(history.history)
    # display(history)

    train_accuracy = history.history["accuracy"]
    # val_accuracy = history.history['val_accuracy']
    train_recall = history.history["recall"]
    train_precision = history.history["precision"]
    plt.plot(train_accuracy, label="train_accuracy")
    # plt.plot(val_accuracy, label='validation accuracy')
    plt.plot(train_recall, label="train_recall")
    plt.plot(train_precision, label="train_precision")
    plt.xticks(range(num_epochs))
    plt.xlabel("Train epochs")
    plt.legend()
    plt.show()

    model.summary()

    test_accuracy = 0
    test_accuracy = model.evaluate(x=X_test, y=Y_test, verbose=0, return_dict=True)[
        "accuracy"
    ]
    return test_accuracy
