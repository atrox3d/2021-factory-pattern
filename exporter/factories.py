from .factory import ExporterFactory
from .fastexporter import FastExporter
from .hqexporter import HQExporter
from .masterexporter import MasterExporter

class Factories:

    factories = dict(
        low = FastExporter(),
        high = HQExporter(),
        master = MasterExporter()
    )

    def get_factories(self) -> dict:
        return self.factories
    
    def get_qualities(self) -> str:
        qualities = ', '.join(self.factories.keys())
        return qualities
    
    def get_factory(self, quality: str) -> ExporterFactory:
        return self.factories[quality]
