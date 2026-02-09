

from pathlib import Path
from enum import Enum


class GameVersion(str, Enum):
    GC_NTSC = "gc_ntsc"
    GC_PAL = "gc_pal"




class PracticeModMode(str, Enum):
    disabled = "disabled"
    full = "full"



def get_elf_for(version: GameVersion, practice_mode: PracticeModMode) -> Path:
    elf_path = Path(__file__).parent.joinpath(
        "elfs", f"{version.value}_{practice_mode.value}.elf"
    )

    if not elf_path.is_file():
        raise ValueError(f"No practice mod available for combination {version.name} and {practice_mode.name}.")
    return elf_path

