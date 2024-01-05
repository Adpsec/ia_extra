import numpy as np
import tensorflow as tf

print(tf.__version__)


X = np.linspace(-10.0, 10.0, 300)  
np.random.shuffle(X) 

y = 119 * X - 466


train_end = int(0.6 * len(X))
test_start = int(0.8 * len(X))
X_train, y_train = X[:train_end], y[:train_end]
X_test, y_test = X[test_start:], y[test_start:]
X_val, y_val = X[train_end:test_start], y[train_end:test_start]


tf.keras.backend.clear_session()
linear_model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1], name='Single')
])

linear_model.compile(optimizer=tf.keras.optimizers.SGD(), loss=tf.keras.losses.mean_squared_error)
print(linear_model.summary())

linear_model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=900)

new_values = np.linspace(-5.0, 5.0, 26)  
predictions = linear_model.predict(new_values)
print(predictions.tolist())

W = linear_model.layers[0].get_weights()[0]
b = linear_model.layers[0].get_weights()[1]

print("W = ", W)
print("b = ", b)

print(new_values)