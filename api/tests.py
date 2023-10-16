import json
from django.test import TestCase, Client
from unittest.mock import patch

from django.urls import reverse

from api.file_processor_factory import FileProcessorFactory
from api.file_processors import CSVFileProcessor, ImageFileProcessor, TextFileProcessor
from .models import File


class FileTestCase(TestCase):
    def setUp(self):
        File.objects.create(file="xxx.jpg")
        File.objects.create(file="xxx.csv")
        File.objects.create(file="xxx.txt")
        
    def test_factory(self):
        file = File.objects.get(file="xxx.jpg")
        processor = FileProcessorFactory.create_processor(file)
        assert isinstance(processor, ImageFileProcessor)
        
        file = File.objects.get(file="xxx.txt")
        processor = FileProcessorFactory.create_processor(file)
        assert isinstance(processor, TextFileProcessor)
        
        file = File.objects.get(file="xxx.csv")
        processor = FileProcessorFactory.create_processor(file)
        assert isinstance(processor, CSVFileProcessor)
        
    @patch('time.sleep', return_value=None)
    def test_processor(self, patched_time_sleep):
        file = File.objects.get(file="xxx.jpg")
        assert file.processed is False
        processor = ImageFileProcessor()
        processor.process(file)
        assert file.processed is True
        
        file = File.objects.get(file="xxx.txt")
        assert file.processed is False
        processor = TextFileProcessor()
        processor.process(file)
        assert file.processed is True
        
        file = File.objects.get(file="xxx.csv")
        assert file.processed is False
        processor = CSVFileProcessor()
        processor.process(file)
        assert file.processed is True

    def test_files_handler(self):
        client = Client()
        response = client.get("/api/files/")
        assert response.status_code == 200
        content = json.loads(response.content)
        files = content["files"]
        assert len(files) == 3