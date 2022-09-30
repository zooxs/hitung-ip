from dataclasses import dataclass, field
from collections import defaultdict
from itertools import pairwise

def mean(ls:list):
    return sum(ls)/len(ls)

def konversi_nilai(num):
    ls_hufur = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'E']
    ls_angka = [4, 3.8, 3.4, 3, 2.8, 2.4, 2, 1, 0]
    ls_nilai = [100, 80, 75, 70, 65, 60, 50, 40, 20, 0]
    
    ls_nilai_batas = list(pairwise(ls_nilai))
    for i in ls_nilai_batas:
        if (i[0] > num) & (i[1] <= num):
            return ls_angka[ls_nilai_batas.index(i)]
    

@dataclass
class Matkul:
    nama: str
    sks: int
    smstr: int
    nilai: defaultdict[dict] = field(default_factory=lambda: defaultdict(dict))

    def __post_init__(self):
        self.nilai = {
            'UTS': {
                'porsi': 30,
                'nilai': [0]
            },
            'UAS': {
                'porsi': 30,
                'nilai': [0]
            },
            'TUGAS': {
                'porsi': 30,
                'nilai': [0]
            },
            'KUIS': {
                'porsi': 10,
                'nilai': [0]
            }
        }

    def nilai_akhir(self):
        # cek total persentase
        nilai_matkul = self.nilai
        persentase = (nilai_matkul[k]['porsi'] for k in nilai_matkul.keys())
        if sum(persentase) != 100:
            return 'Total persentase tidak 100%,\nperiksa kembali pembagian nilai!'
        else:
            nilai_hasil_porsi = (.01*nilai_matkul[k]['porsi']*mean(nilai_matkul[k]['nilai']) for k in nilai_matkul.keys())
            total_nilai = sum(nilai_hasil_porsi)
            return self.sks*konversi_nilai(total_nilai)
            
    def data_to_save(self, filename:str =None):
        data = {
            self.nama :
            {'sks': self.sks,
            'smstr': self.smstr,
            'nilai': self.nilai, 
            'nilai_akhir': self.nilai_akhir()}
        }

        if filename != None:
            from json import dump
            with open(filename, 'w') as fl:
                return dump(data, fl)

        else: return data