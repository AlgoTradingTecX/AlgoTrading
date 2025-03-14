


###
# Trains AI to detect market anomalie# Build Autoencoder Model
model = Sequential([
    Dense(32, activation="relu", input_shape=(df_scaled.shape[1],)),
    Dense(16, activation="relu"),
    Dense(8, activation="relu"),
    Dense(16, activation="relu"),
    Dense(32, activation="relu"),
    Dense(df_scaled.shape[1], activation="linear")
])

model.compile(optimizer="adam", loss="mse")
model.fit(df_scaled, df_scaled, epochs=50, batch_size=32)

model.save("anomaly_detector.h5")

####
