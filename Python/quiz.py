class Sorular:

    def __init__(self,soru_yazisi,secenekler,cevap):
        self.soru_yazisi = soru_yazisi
        self.secenekler = secenekler
        self.cevap = cevap
    def cevap_kontrol(self,cevap):
       return self.cevap == cevap.lower()
    
    
class Oyun():
    def __init__(self,sorular):
        self.sorular = sorular
        self.skor = 0
        self.soru_index = 0

    def soru_al(self):
        return self.sorular[self.soru_index]
    
    def soru_yazma(self):
        soru = self.soru_al()
        print(f"Soru: {soru.soru_yazisi}")
        
        for q in soru.secenekler:
            print(f"- {q}")
        cevap = input("Cevap: ").lower()
        self.tahmin(cevap)
        self.soru_yükle()

    def tahmin(self,cevap):
        soru = self.soru_al()
        if soru.cevap_kontrol(cevap):
            self.skor += 1
        self.soru_index += 1
        print("--------------------")
    def soru_yükle(self):
        if len(self.sorular) == self.soru_index:
            self.skoru_yaz()
        else:
            self.gelisme()
            self.soru_yazma()
    def skoru_yaz(self):
        print(f"Skorunuz: {self.skor}")
    def gelisme(self):
        soru_sayisi = len(self.sorular)
        index = self.soru_index + 1
        if index > soru_sayisi:
            print("Oyun Bitti")
        else:
            print(f"{soru_sayisi} den {index}.".center(99,"*"))


s1 = Sorular("Seni en çok kim sever?" , ["ahmed","ahmed","ahmed","ahmed"],"ahmed")
s2 = Sorular("Sen en çok kimi seversin?" , ["aslı","ahmed","ışıl","ahmed"],"ahmed")
s3 = Sorular("En iyi spor?" , ["basketbol","futbol","hokey","fitness"],"basketbol")
soru_listesi = [s1,s2,s3]

oyun1 = Oyun(soru_listesi)

oyun1.soru_yükle()
