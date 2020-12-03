from keras.layers import Embedding, SpatialDropout1D, LSTM
from keras.models import Sequential
from keras import optimizers


def build_lstm_model(
    X_train,
    y_train,
    X_val,
    y_val,
    embedding_matrix,
    vocab_size,
    embedding_dim,
    learning_rate,
):
    model = Sequential()
    model.add(
        Embedding(
            vocab_size, embedding_dim, weights=[embedding_matrix], trainable=False
        )
    )
    model.add(SpatialDropout1D(0.2))
    model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
    model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(1, activation="sigmoid"))
    model.summary()
    print(model.summary())

    # train model
    model.compile(
        loss="binary_crossentropy",
        optimizer=optimizers.Adam(lr=learning_rate),
        metrics=["accuracy"],
    )
    history = model.fit(
        X_train, y_train, epochs=3, validattion_data=(X_val, y_val), batch_size=128
    )

    return model, history