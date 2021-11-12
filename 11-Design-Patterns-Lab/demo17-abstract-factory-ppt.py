from abc import ABC, abstractmethod
import json

class JsonDataExporter(ABC):
   @abstractmethod
   def export(self, data) -> str:
      pass

class CsvDataExporter(ABC):
   @abstractmethod
   def export(self, data) -> str:
      pass


class DataExporterFactory(ABC):
    @abstractmethod
    def get_json_exporter(self) -> JsonDataExporter:
        pass

    @abstractmethod
    def get_csv_exporter(self) -> CsvDataExporter:
        pass
