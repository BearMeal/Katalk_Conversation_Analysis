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


def predict_result(txt_file):    
    model = MyModel("100millon_model").load()
    txt_file2 = txt_to_numpy_array(txt_file)
    result = model.predict(txt_file2)
    
    return result
