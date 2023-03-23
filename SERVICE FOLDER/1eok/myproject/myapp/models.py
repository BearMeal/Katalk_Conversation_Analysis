import os
from django.conf import settings
import tensorflow as tf
# from tf.keras. import load_model


class MyModel:
    def __init__(self, model_name):
        model_path = os.path.join(settings.MODEL_DIR, f"{model_name}.h5")
        self.model_path = model_path
        self.model = None

    def save(self, model):
        model.save(self.model_path)

    def load(self):
        if os.path.exists(self.model_path):
            self.model = tf.keras.models.load_model(self.model_path)
        else:
            raise FileNotFoundError(f"Model file {self.model_path} not found.")
        return self.model

    def predict(self, input_data):
        if self.model is None:
            self.load()
        # 예측 작업 수행
        # 예를 들어:
        result = self.model.predict(input_data)
        return result
        # pass