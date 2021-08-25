from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, url  # 404 page
import myapp
from myapp import views
import os
import myapp
from webapp import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('adminstrator/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # yangiliklar va asosiy sahifa
    path('', views.welcome, name='welcome'),
    path('load_form', views.load_form, name='load_form'),  # yangi plastik qoshish
    path('add', views.add, name='add'),
    # path('load_form', views.show, name='show'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('search', views.search, name='search'),
    # biz haqimizda
    path('about', views.about, name='about'),
    path('about/map', views.map, name='map'),
    # auth
    path('signup', views.signup, name='signup'),
    # kirish
    path('login/', views.login_user, name='login_user'),
    # accountdan chiqish
    path('logout', views.logout_user, name='logout_user'),
    # operatorlar royxati
    path('employees', views.employees, name='employees'),
    # markazlar
    path('markazlar/', views.markazlar, name='markazlar'),
    # shaxsiy kabinet
    path('user/account', views.user_account, name='user_account'),
    # send email
    path('user/account/contact_message', views.sendmail, name='sendmail'),
    # parolni o`zgartirish
    path('changepassword', views.change_password, name='change_password'),
    # menu gallery
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<int:gal_id>', views.onegallery, name='onegallery'),
    # barcha yangiliklar
    path('allnews/', views.allnews, name='allnews'),
    # bitta yangilik
    path('allnews/<int:news_id>', views.newsdetail, name='newsdetail'),
    # barcha videolar
    path('allvideo/', views.allvideo, name='allvideo'),
    # bitta video
    path('allvideo/<int:video_id>', views.onevideo, name='onevideo'),
    # video1
    path('allvideo/<int:video_id>', views.video1, name='onevideo'),
    # barcha xizmatlar
    path('services/', views.services, name='services'),
    # bitta xizmat
    path('services/<int:serviceone_id>', views.serviceone, name='serviceone'),
    # RESET PASSWORD
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="reset_password/password_reset.html"),
         name='reset_password'),
    path('reset_password_sent',
         auth_views.PasswordResetDoneView.as_view(template_name="reset_password/password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="reset_password/password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name="reset_password/password_reset_done.html"),
         name='password_reset_complete')

]  # +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'myapp.views.error_404_view'  # 404 error page

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    settings.STATIC_ROOT
