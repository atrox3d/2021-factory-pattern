from .factory import ExporterFactory
from .fastexporter import FastExporter
from .hqexporter import HQExporter
from .masterexporter import MasterExporter

factories = dict(
    low = FastExporter(),
    high = HQExporter(),
    master = MasterExporter()
)
