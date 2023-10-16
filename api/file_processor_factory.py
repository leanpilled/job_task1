from .file_processors import TextFileProcessor, ImageFileProcessor,CSVFileProcessor


class FileProcessorFactory:
    _processors = {
        'txt': TextFileProcessor,
        'jpg': ImageFileProcessor,
        'csv': CSVFileProcessor,
    }

    @staticmethod
    def create_processor(file):
        file_extension = file.file.name.split('.')[-1]
        processor_class = FileProcessorFactory._processors.get(file_extension)
        if processor_class:
            return processor_class()
        else:
            raise ValueError("Unsupported file type")
