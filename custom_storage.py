# custom_storage.py
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class CustomImageStorage(FileSystemStorage):
    def get_available_name(self, name, **kwargs):
        # Define a custom filename for the uploaded file
        original_name, extension = os.path.splitext(name)
        new_name = original_name + '_custom' + extension
        return super().get_available_name(new_name, **kwargs)

    @property
    def location(self):
        # Define the directory where files will be saved
        return os.path.join(settings.STATIC_ROOT, 'db_images')
