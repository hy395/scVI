# -*- coding: utf-8 -*-

"""Top-level package for scVI-dev."""

__author__ = "Romain Lopez"
__email__ = "romain_lopez@berkeley.edu"
__version__ = "0.6.5"

# Set default logging handler to avoid logging with logging.lastResort logger.
import logging
from logging import NullHandler

from ._settings import set_verbosity, set_seed

logger = logging.getLogger(__name__)
logger.addHandler(NullHandler())

# default to INFO level logging for the scvi package
set_verbosity(logging.INFO)
# this prevents double outputs
logger.propagate = False

__all__ = ["set_verbosity", "set_seed"]
