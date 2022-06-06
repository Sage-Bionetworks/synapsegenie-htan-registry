"""Initialize example registry"""
import logging

from . import ometif
from . import validator
from . import tiffinfo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

__all__ = ["ometif", "validator"]
