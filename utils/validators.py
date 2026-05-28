#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Doğrulama Fonksiyonları
"""

from typing import Union


class Validators:
    """
    Veri doğrulama sınıfı.
    """
    
    @staticmethod
    def validate_positive_number(value: Union[int, float], name: str = "Value") -> bool:
        """
        Pozitif sayı doğrulaması.
        
        Args:
            value: Doğrulanacak değer
            name: Değerin adı (hata mesajında kullanılır)
        
        Returns:
            bool: Geçerli ise True
        
        Raises:
            ValueError: Geçersiz ise
        """
        if not isinstance(value, (int, float)):
            raise ValueError(f"{name} bir sayı olmalıdır.")
        if value <= 0:
            raise ValueError(f"{name} sıfırdan büyük olmalıdır.")
        return True
    
    @staticmethod
    def validate_percentage(value: float, name: str = "Percentage") -> bool:
        """
        Yüzde doğrulaması.
        
        Args:
            value: Doğrulanacak değer
            name: Değerin adı
        
        Returns:
            bool: Geçerli ise True
        
        Raises:
            ValueError: Geçersiz ise
        """
        if not isinstance(value, (int, float)):
            raise ValueError(f"{name} bir sayı olmalıdır.")
        if value < 0 or value > 100:
            raise ValueError(f"{name} 0-100 arasında olmalıdır.")
        return True
    
    @staticmethod
    def validate_integer(value: int, min_val: int = 1, name: str = "Value") -> bool:
        """
        Tamsayı doğrulaması.
        
        Args:
            value: Doğrulanacak değer
            min_val: Minimum değer
            name: Değerin adı
        
        Returns:
            bool: Geçerli ise True
        
        Raises:
            ValueError: Geçersiz ise
        """
        if not isinstance(value, int):
            raise ValueError(f"{name} bir tamsayı olmalıdır.")
        if value < min_val:
            raise ValueError(f"{name} {min_val} veya daha büyük olmalıdır.")
        return True
