#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tekstil Hesaplama Servisi

Tüm tekstil mühendisliği hesaplamalarını içerir.
"""

import math
from typing import Union, Literal


class TextileCalculations:
    """
    Tekstil üretim hesaplamaları için servis sınıfı.
    """
    
    @staticmethod
    def calculate_draft(
        output_count: float,
        doubling: int,
        input_count: float
    ) -> float:
        """
        Çekim hesabı (Draft Calculation)
        
        Formül: Çekim = (Nm_çıkış × Dublaj) / Nm_giriş
        veya: Çekim = (ktex_giriş × Dublaj) / ktex_çıkış
        
        Args:
            output_count: Çıkış numarası (Nm veya ktex)
            doubling: Dublaj sayısı
            input_count: Giriş numarası (Nm veya ktex)
        
        Returns:
            float: Çekim oranı
        
        Raises:
            ValueError: Geçersiz değerler için
        """
        if input_count <= 0:
            raise ValueError("Giriş numarası sıfırdan büyük olmalıdır.")
        if output_count <= 0:
            raise ValueError("Çıkış numarası sıfırdan büyük olmalıdır.")
        if doubling < 1:
            raise ValueError("Dublaj sayısı 1 veya daha fazla olmalıdır.")
        
        return (output_count * doubling) / input_count
    
    @staticmethod
    def calculate_comber(
        output_ktex: float,
        waste_percent: float,
        doubling: int,
        input_ktex: float
    ) -> float:
        """
        Tarama Hesabı (Comber Calculation)
        
        Formül: Tarama = [Çıkış ktex × (100 − Telef%) × Dublaj] / (100 × Giriş ktex)
        
        Args:
            output_ktex: Çıkış ktex
            waste_percent: Telef yüzdesi (0-100)
            doubling: Dublaj sayısı
            input_ktex: Giriş ktex
        
        Returns:
            float: Tarama oranı
        
        Raises:
            ValueError: Geçersiz değerler için
        """
        if output_ktex <= 0:
            raise ValueError("Çıkış ktex sıfırdan büyük olmalıdır.")
        if input_ktex <= 0:
            raise ValueError("Giriş ktex sıfırdan büyük olmalıdır.")
        if waste_percent < 0 or waste_percent > 100:
            raise ValueError("Telef yüzdesi 0-100 arasında olmalıdır.")
        if doubling < 1:
            raise ValueError("Dublaj sayısı 1 veya daha fazla olmalıdır.")
        
        return (output_ktex * (100 - waste_percent) * doubling) / (100 * input_ktex)
    
    @staticmethod
    def calculate_twist(
        alpha_m: float,
        nm: float
    ) -> float:
        """
        Büküm Hesabı (Twist Calculation)
        
        Formül: T/m = αm × √Nm
        
        Args:
            alpha_m: αm katsayısı
            nm: İplik numarası (Nm)
        
        Returns:
            float: Büküm (T/m)
        
        Raises:
            ValueError: Geçersiz değerler için
        """
        if nm <= 0:
            raise ValueError("Nm sıfırdan büyük olmalıdır.")
        if alpha_m < 0:
            raise ValueError("αm katsayısı negatif olamaz.")
        
        return alpha_m * math.sqrt(nm)
    
    @staticmethod
    def convert_count(
        value: float,
        direction: Literal['nm_to_ktex', 'ktex_to_nm']
    ) -> float:
        """
        Nm ↔ ktex Dönüşümü
        
        Formül:
        - Nm → ktex: ktex = 1000 / Nm
        - ktex → Nm: Nm = 1000 / ktex
        
        Args:
            value: Dönüştürülecek değer
            direction: Dönüşüm yönü ('nm_to_ktex' veya 'ktex_to_nm')
        
        Returns:
            float: Dönüştürülen değer
        
        Raises:
            ValueError: Geçersiz değerler için
        """
        if value <= 0:
            raise ValueError("Değer sıfırdan büyük olmalıdır.")
        
        if direction == 'nm_to_ktex':
            return 1000 / value
        elif direction == 'ktex_to_nm':
            return 1000 / value
        else:
            raise ValueError(f"Geçersiz dönüşüm yönü: {direction}")
    
    @staticmethod
    def calculate_delivery_speed(
        spindle_rpm: int,
        twist_per_meter: float
    ) -> float:
        """
        İplik Teslim Hızı (Delivery Speed)
        
        Formül: L = ni / (T/m)
        Burada ni = spindle_rpm (iğ devri)
        
        Args:
            spindle_rpm: İğ devri (RPM)
            twist_per_meter: Büküm (T/m)
        
        Returns:
            float: İplik hızı (m/dk)
        
        Raises:
            ValueError: Geçersiz değerler için
        """
        if spindle_rpm <= 0:
            raise ValueError("İğ devri sıfırdan büyük olmalıdır.")
        if twist_per_meter <= 0:
            raise ValueError("Büküm sıfırdan büyük olmalıdır.")
        
        return spindle_rpm / twist_per_meter
    
    @staticmethod
    def calculate_daily_production(
        machine_speed: float,
        efficiency: float,
        spindle_count: int,
        nm: float
    ) -> float:
        """
        Günlük Üretim Hesabı (Daily Production)
        
        Formül: Günlük Üretim = (m/dk × 60 × 24 × verim × iğ sayısı) / (1000 × Nm)
        
        Args:
            machine_speed: Makine hızı (m/dk)
            efficiency: Verim (0-1 arasında)
            spindle_count: İğ sayısı
            nm: İplik numarası (Nm)
        
        Returns:
            float: Günlük üretim (kg/gün)
        
        Raises:
            ValueError: Geçersiz değerler için
        """
        if machine_speed <= 0:
            raise ValueError("Makine hızı sıfırdan büyük olmalıdır.")
        if efficiency < 0 or efficiency > 1:
            raise ValueError("Verim 0-1 arasında olmalıdır.")
        if spindle_count <= 0:
            raise ValueError("İğ sayısı sıfırdan büyük olmalıdır.")
        if nm <= 0:
            raise ValueError("Nm sıfırdan büyük olmalıdır.")
        
        # Günlük üretim formülü
        production = (machine_speed * 60 * 24 * efficiency * spindle_count) / (1000 * nm)
        
        return production
    
    @staticmethod
    def calculate_passage_draft(
        passage_num: int,
        input_count: float,
        output_count: float,
        doubling: int = 1
    ) -> float:
        """
        Pasaj Çekim Hesabı (Passage Draft)
        
        Args:
            passage_num: Pasaj numarası (1, 2 veya 3)
            input_count: Giriş numarası
            output_count: Çıkış numarası
            doubling: Dublaj sayısı
        
        Returns:
            float: Pasaj çekim oranı
        """
        if passage_num not in [1, 2, 3]:
            raise ValueError("Pasaj numarası 1, 2 veya 3 olmalıdır.")
        
        return TextileCalculations.calculate_draft(output_count, doubling, input_count)
