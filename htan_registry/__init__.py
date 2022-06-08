"""Initialize example registry"""
import logging

from . import validator
from . import imaging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

__all__ = ["imaging", "validator"]
