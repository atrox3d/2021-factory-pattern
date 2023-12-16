from .factory import ExporterFactory
from .video.videoexporter import VideoExporter
from .audio.audioexporter import AudioExporter

from .video.h264bp import H264BPVideoExporter
from .audio.aac import AACAudioExporter

class FastExporter(ExporterFactory):
    
    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


