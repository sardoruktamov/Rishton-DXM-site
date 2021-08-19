from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Employee, Worker, Markazlar, Yangilik, Biz, Galereya, Videolar, Xizmatlar, SubscribeUser, Contact, \
    Videos
from .forms import EmployeeForm, SignUpForm, LoginForm, UserAccountForm, SubscribeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings




# asosiy sahifa
def welcome(request):
    news = Yangilik.objects.order_by('-sana')[:4]
    tashkil = Biz.objects.all()
    vid = Videos.objects.order_by('-sana')[:1]
    videos = Videos.objects.order_by('-sana')[:5]
    return render(request, 'index.html', {'news': news, 'tashkil': tashkil, 'videos': videos, 'vid': vid})


# jadval va jadvalga qo`shish
@login_required
def load_form(request):
    if request.method == 'GET':
        if len(request.user.groups.filter(name='Admin')) != 0:
            author = Employee.author == request.user
            muallif = request.user
            employee = Employee.objects.order_by('-date')
            p = Paginator(employee, 5)
            page_num = request.GET.get('page', 1)
            # page_sart = page.start_index(1,2,3)
            # page_end = page.end_index(4,5,6,7)
            try:
                page = p.page(page_num)
            except PageNotAnInteger:
                page = p.page(1)
            except EmptyPage:
                page = p.page(p.num_pages)
            return render(request, 'kadastr.html',
                          {'form': EmployeeForm, 'employee': page, 'page_num': page_num, 'author': author,
                           'muallif': muallif})
        return redirect('welcome')
    else:
        form = EmployeeForm(request.POST)
        new_form = form.save(commit=False)
        new_form.auther = request.user
        new_form.save()
        return redirect('load_form')


def load_form_censel(request):
    return render(request, 'kadastr.html')


# about
def about(request):
    haqida = Biz.objects.all()
    xodim = Worker.objects.all()
    return render(request, 'about.html', {'haqida': haqida, 'xodim': xodim})


def map(request):
    return render(request, 'aboutt.html')


@login_required
def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/show')


@login_required
def edit(request, id):
    employee = Employee.objects.get(pk=id)
    return render(request, 'edit.html', {'employee': employee})


@login_required
def update(request, id):
    author = Employee.author == request.user
    muallif = request.user
    employee = Employee.objects.get(pk=id)
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('load_form')


@login_required
def delete(request, id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('load_form')


def search(request):
    given_name = request.POST['given_name']
    # if request.method == "GET":
    if given_name is None:
        return redirect(request, 'load_form')
    else:
        employee = Employee.objects.filter(ename__contains=given_name)
        return render(request, 'kadastr.html', {'employee': employee})


# royxatdan o`tish
def signup(request):
    if request.method == "GET":
        users = User.objects.all()[:5]
        user = SignUpForm()
        return render(request, 'signup.html', {'form': user, 'users': users})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'], email=request.POST['email'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return render(request, 'index.html')
            except IntegrityError:
                return render(request, 'signup.html',
                              {'form': SignUpForm(), 'error': 'Bunday foydalanuvchi avval ro`yxatdan o`tgan!'})
        else:
            return render(request, 'signup.html',
                          {'form': SignUpForm(), 'error': 'Siz kiritgan parollar bir xil emas!'})


# shaxsiy kabinet
def user_account(request):
    user = User.objects.get(username=request.user)

    if request.method == 'GET':
        form = UserAccountForm(instance=user)
        return render(request, 'account.html', {'form': form})
    else:
        form = UserAccountForm(request.POST, instance=user)
        form.save()
        return render(request, 'account.html', {'form': form})


# parolni o'zgartirish
def change_password(request):
    if request.method == 'GET':
        form = PasswordChangeForm(request.user)
        return render(request, 'changepassword.html', {'form': form})

    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('change_password')
    return render(request, 'changepassword.html', {'form': form})


# akkountga kirish
def login_user(request):
    if request.method == 'GET':
        user = LoginForm()
        return render(request, 'login_user.html', {'form': user})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login_user.html',
                          {'form': LoginForm(), 'error': 'Login yoki parol xato kiritildi!'})
        else:
            login(request, user)
            return HttpResponseRedirect('/')


# akkountdan chiqish
@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect('/')


# operatorlar
@login_required
def employees(request):
    worker = Worker.objects.all()
    return render(request, 'employees.html', {'worker': worker})


# markazlar xaqida
def markazlar(request):
    center = Markazlar.objects.all()
    return render(request, 'markazlar.html', {'center': center})


# galereya menyusi
def gallery(request):
    image = Galereya.objects.order_by('-sana')
    pgn = Paginator(image, 8)
    page_num = request.GET.get('page', 1)
    try:
        page = pgn.page(page_num)
    except EmptyPage:
        page = pgn.page(1)
    return render(request, 'gallery.html', {'image': page})


# bitta galereya rasmi
def onegallery(request, gal_id):
    oneimage = get_object_or_404(Galereya, pk=gal_id)
    return render(request, 'onegallery.html', {'oneimage': oneimage})


# barcha yangiliklar
def allnews(request):
    news = Yangilik.objects.order_by('-sana')
    pgn = Paginator(news, 8)
    page_nums = request.GET.get('page', 1)
    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)

    return render(request, 'all_news.html', {'news': page})


# bitta yangilik
def newsdetail(request, news_id):
    newsss = get_object_or_404(Yangilik, pk=news_id)
    return render(request, 'newsdetail.html', {'newsss': newsss})


# barcha videolarni chiqarish
def allvideo(request):
    videos = Videos.objects.order_by('-sana')
    pgn = Paginator(videos, 6)
    page_nums = request.GET.get('page', 1)
    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)
    return render(request, 'all_video.html', {'videos': page})


# bitta video haqida batafsil
@login_required
def onevideo(request, video_id):
    videos = get_object_or_404(Videos, pk=video_id)
    return render(request, 'onevideo.html', {'videos': videos})


# bitta video
def video1(request, video_id):
    videosw = Videolar.objects.all()[:1]
    return render(request, 'index.html', {'videosw': videosw})


def services(request):
    xizmatlar = Xizmatlar.objects.all()
    pgn = Paginator(xizmatlar, 10)
    page_nums = request.GET.get('page', 1)
    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)
    return render(request, 'services.html', {'xizmatlar': page})


# bitta yangilik
@login_required
def serviceone(request, serviceone_id):
    xizmat = get_object_or_404(Xizmatlar, pk=serviceone_id)
    return render(request, 'serviceone.html', {'xizmat': xizmat})


def sendmail(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        msg = 'Sizga Rishton DXM saytidan ' + full_name + ' xabar yubordi. ' + '\n' + 'elektron pochtasi: ' + email + '\n' + 'xabar mazmuni: ' + '\n' + message
        send_mail(
            'Yangi xabar',
            msg,
            settings.EMAIL_HOST_USER,
            ['sardorbek.uktamov.1@mail.ru'],
            fail_silently=False,
        )

        contact_user = Contact(
            full_name=full_name,
            email=email,
            message=message
        )
        contact_user.save()
        return render(request, 'contact.html')
    else:
        print('555555555555555555555555555555555555555555555')
        return redirect('services')
