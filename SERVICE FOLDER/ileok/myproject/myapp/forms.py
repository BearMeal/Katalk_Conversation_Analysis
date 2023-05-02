from django import forms
# class UploadFileForm(forms.Form):
#     file = forms.FileField()

class UploadFileForm(forms.Form):
    ALLOWED_EXTENSIONS = ['txt']
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            filename = file.name
            if not filename.endswith(tuple(self.ALLOWED_EXTENSIONS)):
                raise forms.ValidationError('txt 파일만 업로드 가능합니다.')
            if file.size > 1 * 1024 * 1024:
                raise forms.ValidationError('1MB 이하의 파일만 업로드 가능합니다.')
        return file