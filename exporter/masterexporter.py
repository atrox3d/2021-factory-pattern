from .factory import ExporterFactory
from .video.videoexporter import VideoExporter
from .audio.audioexporter import AudioExporter

from .video.lossles import LosslessVideoExporter
from .audio.wav import WAVAudioExporter

class FastExporter(ExporterFactory):
    
    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()
