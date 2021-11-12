from abc import ABC, abstractmethod

class DataExporter(ABC):
	@abstractmethod
	def export(self, data):
		pass

class CsvDataExporter(ABC):
	@abstractmethod
	def export(self, data) -> str:
		pass


class DataExporterFactory(ABC):
    @abstractmethod
    def get_exporter(self) -> DataExporter:
        pass


class CsvDataExporterFactory(DataExporterFactory):
    def get_exporter(self) -> DataExporter:
        return CsvDataExporter()
