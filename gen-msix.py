"""
Script to generate msix from Linux

Requirements: pymsix and makemsix
"""

from pathlib import Path
from msix import MsixPacker  # type: ignore

packer = MsixPacker(verbose=True)
APP_NAME = "chepy"
OUTPUT_DIR = "output"
TMPUNPACK_DIR = "/tmp"

output_path = Path(OUTPUT_DIR)
try:
    output_path.mkdir()
except FileExistsError:
    print(f"Directory '{output_path}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{output_path}'.")
# pylint: disable=W0718
except Exception as exc:
    print(f"An error occurred: {exc}")

packer.pack("dist/chepy", f"{OUTPUT_DIR}/{APP_NAME}.msix")
packer.sign(
    f"{OUTPUT_DIR}/{APP_NAME}.msix",
    "certificate.pfx",
    pfx_password="test",
    timestamp_url="http://timestamp.digicert.com",
)
