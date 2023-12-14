__version__ = "0.4"

# Import necessary modules or packages here
from .api import *
from .etl import *
from .tools import *

# Define a function to return the version
def get_version():
    return __version__

# List of symbols to export
__all__ = (
    api.__all__ +
    etl.__all__ +
    tools.__all__ +
    ['get_version']
)
