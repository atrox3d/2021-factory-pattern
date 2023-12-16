"""
Basic video exporting example
"""

import pathlib

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

    while True:
        qualities = ', '.join(factories.keys())
        export_quality = input(f"Enter desired output quality ({qualities}): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}.")

def main(fac: ExporterFactory) -> None:
    """Main function."""

    # create the video and audio exporters
    video_exporter: VideoExporter = fac.get_video_exporter()
    audio_exporter: AudioExporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    fac = read_exporter()
    main(fac)
