"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod

from exporter.video.videoexporter import VideoExporter
from exporter.video.lossles import LosslessVideoExporter
from exporter.video.h264bp import H264BPVideoExporter
from exporter.video.h264hi422p import H264Hi422PVideoExporter

from exporter.audio.audioexporter import AudioExporter
from exporter.audio.aac import AACAudioExporter
from exporter.audio.wav import WAVAudioExporter


def main() -> None:
    """Main function."""

    # read the desired export quality
    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in {"low", "high", "master"}:
            break
        print(f"Unknown output quality option: {export_quality}.")

    # create the video and audio exporters
    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    if export_quality == "low":
        video_exporter = H264BPVideoExporter()
        audio_exporter = AACAudioExporter()
    elif export_quality == "high":
        video_exporter = H264Hi422PVideoExporter()
        audio_exporter = AACAudioExporter()
    else:
        # default: master quality
        video_exporter = LosslessVideoExporter()
        audio_exporter = WAVAudioExporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
