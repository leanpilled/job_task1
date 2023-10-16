from celery import shared_task

from .file_processor_factory import FileProcessorFactory
from .models import File


@shared_task
def process_file(file_id):
    file = File.objects.get(id=file_id)
    try:
        processor = FileProcessorFactory.create_processor(file)
        processor.process(file)
    except ValueError as e:
        print(f"Error: {e}")
