"""
Script to unpack msix from Linux

Requirements: pymsix and makemsix
"""

from msix import MsixPacker  # type: ignore

packer = MsixPacker(verbose=True)
APP_NAME = "chepy"
OUTPUT_DIR = "output"
TMPUNPACK_DIR = "/tmp"

packer.unpack(f"{OUTPUT_DIR}/{APP_NAME}.msix", TMPUNPACK_DIR)
