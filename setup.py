from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mpil_custom_app/__init__.py
from mpil_custom_app import __version__ as version

setup(
	name="mpil_custom_app",
	version=version,
	description="Mpil Custom App",
	author="Sowaan",
	author_email="info@sowaan.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
