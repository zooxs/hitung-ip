from matkul import Matkul
from json import load

daftar_matkul = Matkul('Fisika Dasar 2', 4, 2)

rangkuman_nilai = {
            'UTS': {
                'porsi': 30,
                'nilai': [80]
            },
            'UAS': {
                'porsi': 30,
                'nilai': [80]
            },
            'TUGAS': {
                'porsi': 30,
                'nilai': [65, 70, 80]
            },
            'KUIS': {
                'porsi': 10,
                'nilai': [70, 80]
            }
        }
