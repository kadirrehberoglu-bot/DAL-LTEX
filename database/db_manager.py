#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Veritabanı Yöneticisi
"""

import sqlite3
import os
from datetime import datetime
from typing import List, Tuple


class DatabaseManager:
    """
    SQLite veritabanı yöneticisi.
    """
    
    def __init__(self, db_name: str = "textile_calc.db"):
        """
        Veritabanı yöneticisini başlat.
        
        Args:
            db_name: Veritabanı dosya adı
        """
        self.db_name = db_name
        self.conn = None
    
    def initialize(self):
        """
        Veritabanını başlat ve tabloları oluştur.
        """
        self.connect()
        self.create_tables()
    
    def connect(self):
        """
        Veritabanına bağlan.
        """
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    
    def create_tables(self):
        """
        Veritabanı tablolarını oluştur.
        """
        # Hesaplama geçmişi tablosu
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS calculations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                calculation_type TEXT NOT NULL,
                input_value TEXT NOT NULL,
                output_value TEXT NOT NULL,
                result TEXT NOT NULL
            )
        """)
        
        self.conn.commit()
    
    def add_calculation(
        self,
        calc_type: str,
        input_val: str,
        output_val: str,
        result: str
    ):
        """
        Hesaplamayı veritabanına ekle.
        
        Args:
            calc_type: Hesaplama türü
            input_val: Giriş değeri
            output_val: Çıkış değeri
            result: Sonuç
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.cursor.execute("""
            INSERT INTO calculations (timestamp, calculation_type, input_value, output_value, result)
            VALUES (?, ?, ?, ?, ?)
        """, (timestamp, calc_type, input_val, output_val, result))
        
        self.conn.commit()
    
    def get_calculations_history(self) -> List[Tuple]:
        """
        Hesaplama geçmişini al.
        
        Returns:
            List[Tuple]: Hesaplama geçmişi
        """
        self.cursor.execute("SELECT * FROM calculations ORDER BY timestamp DESC")
        return self.cursor.fetchall()
    
    def clear_history(self):
        """
        Hesaplama geçmişini temizle.
        """
        self.cursor.execute("DELETE FROM calculations")
        self.conn.commit()
    
    def close(self):
        """
        Veritabanı bağlantısını kapat.
        """
        if self.conn:
            self.conn.close()
