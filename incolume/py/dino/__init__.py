import toml
from pathlib import Path


pyproject = Path(__file__).parents[3].joinpath('pyproject.toml')
versionfile = Path(__file__).parents[3] / 'version.txt'

versionfile.write_text(
    f"{toml.load(pyproject)['tool']['poetry']['version']}\n"
)
__version__ = versionfile.read_text().strip()
