import argparse
import logging
from pathlib import Path
import subprocess

from open_prime_rando_practice_mod import GameVersion, PracticeModMode, get_filename_for

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output_dir",
        type=Path,
        help="The directory to place the ELF file in",
    )
    parser.add_argument(
        "-B", "--build-type",
        type=str,
        choices=["Release", "Debug"],
        default="Release",
        help="Which build type to use"
    )
    parser.add_argument(
        "-v", "--version",
        type=GameVersion,
        choices=[version.value for version in GameVersion],
        default=GameVersion.GC_NTSC,
        help="Which version of the game to build for",
    )
    parser.add_argument(
        "-m", "--mode",
        type=PracticeModMode,
        choices=[mode.value for mode in PracticeModMode],
        default=PracticeModMode.full,
        help="Which practice mod mode to build for"
    )
    return parser


def build_elf(args: argparse.Namespace) -> None:
    path: Path = args.output_dir
    if not path.is_dir():
        raise ValueError(f"{path} is not a valid directory")
    
    path = path.joinpath(get_filename_for(args.version, args.mode))

    mode = "-DRANDOMIZER=ON"
    if args.mode == PracticeModMode.disabled:
        mode += " -DPRACTICE_MOD=OFF"
    else:
        mode += " -DPRACTICE_MOD=ON"

    if args.version != GameVersion.GC_NTSC:
        raise ValueError(f"Cannot build ELF for {args.version}")
    
    subprocess.run([
        "./build-elf.sh",
        path,
        args.build_type,
        mode,
    ])


def main() -> None:
    parser = create_parser()
    raise SystemExit(build_elf(parser.parse_args()))


if __name__ == "__main__":
    main()
