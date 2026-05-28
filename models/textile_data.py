#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tekstil Veri Modelleri
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TextileCount:
    """
    İplik numarası veri modeli.
    """
    nm: Optional[float] = None
    ktex: Optional[float] = None
    description: str = ""


@dataclass
class CalculationResult:
    """
    Hesaplama sonucu veri modeli.
    """
    calculation_type: str
    result: float
    input_data: dict
    timestamp: datetime
    notes: str = ""


@dataclass
class MachineSettings:
    """
    Makine ayarları veri modeli.
    """
    spindle_rpm: int
    machine_speed: float
    spindle_count: int
    efficiency: float
    notes: str = ""
