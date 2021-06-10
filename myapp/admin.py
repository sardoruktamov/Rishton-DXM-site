from django.contrib import admin
from .models import Worker, Markazlar, Employee, Yangilik, Biz, Galereya, Videolar, Xizmatlar, Contact
# Register your models here.

@admin.register(Contact) 
class PostModelContact(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'message']

@admin.register(Xizmatlar) 
class PostModelXizmatlar(admin.ModelAdmin):
    list_display = ['xizmatNomi', 'bajarilishMuddati', 'yigimMiqdori', 'qaror']

# admin.site.register(Galereya)
@admin.register(Galereya) 
class PostModelGalereya(admin.ModelAdmin):
    list_display = ['sarlavha', 'matn']
    

# admin.site.register(Videolar)
@admin.register(Videolar) 
class PostModelVideolar(admin.ModelAdmin):
    list_display = ['sarlavha', 'matn']

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
    list_display = ['sarlavha', 'matn1', 'sana', 'vaqt']

@admin.register(Biz) 
class Biz(admin.ModelAdmin):
    list_display = ['sarlavha1', 'sarlavha2', 'matn2']