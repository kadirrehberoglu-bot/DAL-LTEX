#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Biçimlendirme Fonksiyonları
"""

from typing import Union


class Formatters:
    """
    Veri biçimlendirme sınıfı.
    """
    
    @staticmethod
    def format_number(value: float, decimals: int = 2) -> str:
        """
        Sayıyı biçimlendir.
        
        Args:
            value: Biçimlendirilecek sayı
            decimals: Ondalık basamak sayısı
        
        Returns:
            str: Biçimlendirilmiş sayı
        """
        return f"{value:.{decimals}f}"
    
    @staticmethod
    def format_percentage(value: float, decimals: int = 2) -> str:
        """
        Yüzdeyi biçimlendir.
        
        Args:
            value: Biçimlendirilecek yüzde
            decimals: Ondalık basamak sayısı
        
        Returns:
            str: Biçimlendirilmiş yüzde
        """
        return f"{value:.{decimals}f}%"
    
    @staticmethod
    def format_production(value: float) -> str:
        """
        Üretim değerini biçimlendir.
        
        Args:
            value: Biçimlendirilecek değer (kg/gün)
        
        Returns:
            str: Biçimlendirilmiş üretim değeri
        """
        return f"{value:.2f} kg/gün"
