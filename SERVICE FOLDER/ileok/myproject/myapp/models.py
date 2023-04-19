import os
from django.conf import settings
import tensorflow as tf
# from tf.keras. import load_model
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploaded_files/')
    upload_date = models.DateTimeField(auto_now_add=True)


class MyModel:
    def __init__(self, model_name):
        model_path = os.path.join(settings.MODEL_DIR, 'model1', f"{model_name}.h5")
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

class TrainingData(models.Model):
    input_data = models.JSONField()
    output_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Training Data {self.id}"
    
class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()

class NaverMovieData(models.Model):
    content = models.CharField(max_length=160)
    label = models.IntegerField()

class Sentiword_dict1(models.Model):
    content = models.CharField(max_length=32)
    label = models.IntegerField()

class Sentiword_dict2(models.Model):
    content = models.CharField(max_length=10)
    sentiment = models.CharField(max_length=10)
    frequency = models.FloatField()
    degree1 = models.FloatField()
    degree2 = models.FloatField()

class User_kakao_data(models.Model):
    sender=models.CharField(max_length=10)
    content = models.CharField(max_length=200)
    time=models.TimeField()
