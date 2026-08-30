"""
Script to generate msix from Linux

Requirements: pymsix and makemsix
"""

from msix import MsixPacker

packer = MsixPacker()
app_name = "chepy"
packer.pack("dist/chepy", f"output/{app_name}.msix")
packer.unpack(f"output/{app_name}.msix", "/tmp/extracted/")
packer.sign(
    f"output/{app_name}.msix",
    "certificate.pfx",
    pfx_password="test",
    timestamp_url="http://timestamp.digicert.com",
)
