from app.analysis.filesystem import FilesystemAnalysis
from app.analysis.firmware_analysis import FirmwareAnalysis
from app.analysis.operating_system_analysis import OperatingSystemAnalysis
from app.analysis.root_subvolume_analysis import RootSubvolumeAnalysis
from app.modules.base import Module


class SystemCheckModule(Module):
    """Runs system analysis."""

    name = "System Analysis"
    description = "Analyze the current system."

    def run(self):
        return [
            OperatingSystemAnalysis().run(),
            FirmwareAnalysis().run(),
            FilesystemAnalysis().run(),
            RootSubvolumeAnalysis().run(),
        ]
