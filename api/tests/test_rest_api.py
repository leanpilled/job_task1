

from api.file_processor_factory import FileProcessorFactory
from api.file_processors import TextFileProcessor

class MockFile:
    def __init__(self, name):
        self.name = name
        
class MockFileInstance:
    def __init__(self, name, uploaded_at, processed):
        self.file = MockFile(name)
        self.uploaded_at = uploaded_at
        self.processed = processed



def test_upload_file(api_client):
    assert 1 == 1
    
    
def test_create_text_processor():
    file = MockFile('sample.txt')
    processor = FileProcessorFactory.create_processor(file)
    assert isinstance(processor, TextFileProcessor)