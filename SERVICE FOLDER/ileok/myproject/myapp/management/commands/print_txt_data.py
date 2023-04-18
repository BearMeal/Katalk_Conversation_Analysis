# myapp/management/commands/print_txt_data.py
from django.core.management.base import BaseCommand
from myapp.models import UploadedFile
import os

def txt_to_list(file_path):
    if os.path.isfile(file_path):
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                row = [int(num) for num in line.strip().split(',')]
                data.append(row)
        return data
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")

class Command(BaseCommand):
    help = 'Prints data from all uploaded txt files as lists'

    def handle(self, *args, **options):
        uploaded_files = UploadedFile.objects.all()
        all_data_lists = []

        for uploaded_file in uploaded_files:
            data_list = txt_to_list(uploaded_file.file.path)
            all_data_lists.append(data_list)

        print(all_data_lists)