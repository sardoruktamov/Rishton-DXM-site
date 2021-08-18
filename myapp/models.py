from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    econtact = models.CharField(max_length=30, blank=True)
    epetition = models.CharField(max_length=8, null=True)
    eplastic = models.CharField(max_length=12, null=True)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.ename
    
    class Meta:
        verbose_name = "Plastik"
        verbose_name_plural = "Kadastr plastiglari"

class Worker(models.Model):
    name = models.CharField(max_length=55)
    bolim = models.TextField(max_length=300, null=True)
    DIREKTOR = 'DIREKTOR'
    BOLIM = 'BO`LIM BOSHLIG`I'
    BOSH = 'BOSH MUTAXASSIS'
    YETAKCHI = 'YETAKCHI MUTAXASSIS'
    KATTA = 'KATTA MUTAXASSIS'
    TEXNIKA = 'XISOBLASH TEXNIKASI OPERATORI'
    ALOQA = 'ALOQA OPERATORI'
    QOROVUL = 'QOROVUL'
    FARROSH = 'FARROSH'
    AMALIYOT = 'AMALIYOTCHI'
    LAVOZIMLAR = [
        (DIREKTOR, 'DIREKTOR'),
        (BOLIM,'BO`LIM BOSHLIG`I'),
        (BOSH, 'BOSH MUTAXASSIS'),
        (YETAKCHI, 'YETAKCHI MUTAXASSIS'),
        (KATTA, 'KATTA MUTAXASSIS'),
        (TEXNIKA, 'XISOBLASH TEXNIKASI OPERATORI'),
        (ALOQA, 'ALOQA OPERATORI'),
        (QOROVUL, 'QOROVUL'),
        (FARROSH, 'FARROSH'),
        (AMALIYOT, 'AMALIYOTCHI')
    ]
    berth = models.CharField(max_length=100,choices=LAVOZIMLAR)
    phone = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Markaz xodimi"
        verbose_name_plural = "Markaz xodimlari"

class Markazlar(models.Model):
    markaz_Nomi = models.CharField(max_length=250)
    telefon = models.CharField(max_length=16)
    manzil = models.CharField(max_length=300)
    ish_Vaqti = models.CharField(max_length=50)

    def __str__(self):
        return self.markaz_Nomi
    
    class Meta:
        verbose_name = "Markaz"
        verbose_name_plural = "Markazlar"

class Yangilik(models.Model):
    sarlavha = models.CharField(max_length=200, blank=True)
    matn1 = models.TextField(max_length=3000, blank=True)
    rasm1 = models.ImageField(upload_to='yangiliklar/rasmlar/', blank=True)
    matn2 = models.TextField(max_length=2000, blank=True)
    rasm2 = models.ImageField(upload_to='yangiliklar/rasmlar/', blank=True)
    rasm3 = models.ImageField(upload_to='yangiliklar/rasmlar/', blank=True)
    sana = models.DateField(null=True, blank=True)
    vaqt = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.sarlavha

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

class Biz(models.Model):
    sarlavha1 = models.CharField(max_length=300, blank=True)
    sarlavha2 = models.CharField(max_length=300, blank=True)
    matn1 = models.TextField(max_length=3000, blank=True)
    matn2 = models.TextField(max_length=3000, blank=True)
    matn3 = models.TextField(max_length=3000, blank=True)
    manzil = models.CharField(max_length=300, blank=True)
    moljal = models.CharField(max_length=300, blank=True)
    telefon = models.CharField(max_length=20, blank=True)
    sana = models.DateField(null=True, blank=True)
    vaqt = models.TimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.sarlavha1
    
    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda"
    
class Galereya(models.Model):
    rasm = models.ImageField(upload_to='galereya/', blank=True)
    sarlavha = models.CharField(max_length=200, blank=True)
    matn = models.TextField(max_length=300, blank=True)
    sana = models.DateField(null=True, blank=True)
    vaqt = models.TimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = "galereya"
        verbose_name_plural = "Galereya"
    
class Videolar(models.Model):
    sarlavha = models.CharField(max_length=200, blank=True)
    matn = models.TextField(blank=True)
    video = models.FileField(upload_to="video/%y")
    sana = models.DateField(null=True, blank=True)
    vaqt = models.TimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.sarlavha

    class Meta:
        verbose_name = "video"
        verbose_name_plural = "Foydali videolar"
    
class Xizmatlar(models.Model):
    xizmatNomi = models.CharField(max_length=300)
    bajarilishMuddati = models.CharField(max_length=40, blank=True)
    vdo = models.CharField(max_length=300, blank=True)
    yigimMiqdori = models.CharField(max_length=100, blank=True)
    davlatBoji = models.CharField(max_length=100, blank=True)
    qaror = models.CharField(max_length=200, blank=True)
    kerakliHujjatlar = models.TextField(blank=True)

    def __str__(self):
        return self.xizmatNomi

    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmat turlari"

class SubscribeUser(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email     = models.EmailField()
    message   = models.TextField(max_length=300)

    def __str__(self):
        return self.full_name