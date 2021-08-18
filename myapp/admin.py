from django import forms
from django.contrib import admin

from .models import Worker, Markazlar, Employee, Yangilik, Biz, Galereya, Videolar, Xizmatlar, Contact
# Register your models here.

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class YangilikAdminForm(forms.ModelForm):
    matn1 = forms.CharField(label="Matn qism", widget=CKEditorUploadingWidget())
    matn2 = forms.CharField(label="Matn qism", widget=CKEditorUploadingWidget())
    class Meta:
        model = Yangilik
        fields = '__all__'

class VideolarAdminForm(forms.ModelForm):
    matn = forms.CharField(label="Matn qism", widget=CKEditorUploadingWidget())
    class Meta:
        model = Videolar
        fields = '__all__'

class XizmatlarAdminForm(forms.ModelForm):
    kerakliHujjatlar = forms.CharField(label="Matn qism", widget=CKEditorUploadingWidget())
    class Meta:
        model = Xizmatlar
        fields = '__all__'

@admin.register(Contact) 
class PostModelContact(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'message']

@admin.register(Xizmatlar) 
class PostModelXizmatlar(admin.ModelAdmin):
    list_display = ['xizmatNomi', 'bajarilishMuddati', 'yigimMiqdori']
    form = XizmatlarAdminForm
    list_filter = ['vdo', 'yigimMiqdori', 'bajarilishMuddati']

# admin.site.register(Galereya)
@admin.register(Galereya) 
class PostModelGalereya(admin.ModelAdmin):
    list_display = ['sarlavha', 'matn']
    

# admin.site.register(Videolar)
@admin.register(Videolar) 
class PostModelVideolar(admin.ModelAdmin):
    list_display = ['sarlavha', 'matn']
    form = VideolarAdminForm

# admin.site.register(Employee)
@admin.register(Employee) 
class PostModelAdminn(admin.ModelAdmin):
    list_display = ['eid', 'ename', 'econtact', 'eplastic']

@admin.register(Worker) 
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'berth', 'phone']

@admin.register(Markazlar)
class PostModelMarkaz(admin.ModelAdmin):
    list_display = ['id', 'markaz_Nomi', 'telefon', 'manzil', 'ish_Vaqti']

@admin.register(Yangilik)
class Yangilik(admin.ModelAdmin):
    list_display = ['sarlavha', 'sana', 'vaqt']
    list_filter = ['sana']
    form = YangilikAdminForm

@admin.register(Biz) 
class Biz(admin.ModelAdmin):
    list_display = ['sarlavha1', 'sarlavha2', 'matn2']

admin.site.site_title = "Django movies"
admin.site.site_header = "Rishton DXM saytining boshqaruv paneli"