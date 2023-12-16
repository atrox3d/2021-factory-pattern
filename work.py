"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod

from exporter.video.videoexporter import VideoExporter
from exporter.audio.audioexporter import AudioExporter

from exporter.factory import ExporterFactory
from exporter.fastexporter import FastExporter
from exporter.hqexporter import HQExporter
from exporter.masterexporter import MasterExporter

def read_exporter() -> ExporterFactory:
    # read the desired export quality
    factories = dict(
        low = FastExporter(),
        high = HQExporter(),
        master = MasterExporter()
    )

    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}.")

def main() -> None:
    """Main function."""

    fac = read_exporter()

    # create the video and audio exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
