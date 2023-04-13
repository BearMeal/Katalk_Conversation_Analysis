import os
import tempfile
from myapp.models import MyModel
import numpy as np

def txt_to_numpy_array(file_path):
    if os.path.isfile(file_path):
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                row = [int(num) for num in line.strip().split(',')]
                data.append(row)
        return np.array(data)
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")


def handle_uploaded_file(file):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    with open(temp_file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return temp_file.name

def predict_result(txt_file):
    # 딥러닝 모델을 사용하여 결과를 예측하고 반환하는 코드를 작성하세요.
    # 예를 들어:
    
    model = MyModel("100millon_model").load()
    txt_file2 = txt_to_numpy_array(txt_file)
    result = model.predict(txt_file2)
    
    return result
    # pass
