from abc import ABC, abstractmethod

from .video.videoexporter import VideoExporter
from .audio.audioexporter import AudioExporter


class ExporterFactory(ABC):
    
    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        pass

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        pass

