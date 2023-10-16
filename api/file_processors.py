from abc import ABC, abstractmethod
import time


class FileProcessor(ABC):
    @abstractmethod
    def process(self, file):
        pass
    

class TextFileProcessor(FileProcessor):
    def process(self, file):
        time.sleep(5)
        file.processed = True
        file.save()
        

class ImageFileProcessor(FileProcessor):
    def process(self, file):
        time.sleep(60)
        file.processed = True
        file.save()
        

class CSVFileProcessor(FileProcessor):
    def process(self, file):
        time.sleep(30)
        file.processed = True
        file.save()
