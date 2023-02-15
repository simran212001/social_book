


from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import CustomUser
from django.contrib.auth import authenticate

from django.core.files.storage import FileSystemStorage
from .models import Book

# User = settings.AUTH_USER_MODEL
# import social_book.users.models
# AUTH_USER_MODEL = 'users.CustomUser'

def home(request):
    return render(request,'index.html')
# Create your views here.
def register(request):
    # print(request.POST)
    if request.method=='POST':
        # print("Simran")
        
        email=request.POST.get('email')
        username=request.POST['username']
        pwd=request.POST['pwd']
        cpwd=request.POST['cpwd']
        # print(email,'emaildnwofjef')
        fullname=request.POST['fullname']
        gender=request.POST['gender']
        
        Birth_year = request.POST.get('Birth_year')

        city=request.POST['city']
        state=request.POST['state']
        # cctype=request.POST['cctype']
        
        credit_num=request.POST['credit_num']
        cvc=request.POST['cvc']

        # expdate=request.POST.get('month') +', ' + request.POST.get('year')
        address = city + ', ' + state
        if pwd != cpwd:
            return HttpResponse('passwords do not match')
        db = get_user_model()
        # user=db.objects.create_user(email=email,username=username,password=pwd,fullname=fullname,gender=gender,city=city,state=state,cctype=cctype,ccnumber=ccnumber,cvc=cvc,expdate=expdate,address=address)
        user=db.objects.create(email=email,username=username,password=pwd,fullname=fullname,gender=gender)
        print(user)
        user.set_password(pwd)
        user.save()


        # 9/2/23
        # if user.is_active:
        #     data = CustomUser.objects.all()
        #     return render(request,'register.html',{'data',data})
            
            
        print("data saved")
        messages.success(request,'sucessfully registered')
        return render(request,'login.html')
    else:
        return render(request,'register.html')
    # return HttpResponse('register')

        # User = get_user_model()
    #     if pwd==cpwd:
    #         if User.objects.filter(username=username).exists():
    #             messages.info(request, 'Email is exist ')
    #             return render(request,'register.html')
    #         else:
    #             user = User.objects.create(username=username,pwd=pwd, email=email)
    #             user.set_password(pwd)
    #             user.save()
    #             messages.success(request,'sucessfully registered')
    #             print("success")
    #             return render(request,'login.html')
    #     else:
    #         messages.info(request, 'Both passwords are not matching')
    #         return render(request,'register.html')
    # else:
    #     print("no post method")
    #     return render(request, 'register.html') 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method=='POST':
        
        uname=request.POST['uname']
        print(uname,'username')
        pwd=request.POST['pwd']
        print(pwd,'password')

        user=auth.authenticate(username=uname,password=pwd)
        print(user,'authenticate')
    
        if user is not None:

            auth.login(request,user)
            messages.success(request,'login sucessfully')
            return render(request,'index.html')
        else:
            messages.info(request,'Invalid userid and password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'sucessfully logout')
    return render(request,'login.html')



def dashboard1(request):
    return render(request,'index.html')


def registered_user(request):
    user_data = CustomUser.objects.filter(public_visibility=1)
    print(user_data)
    return render(request,'authsell.html',{'CustomUser':user_data})



def upload_books(request):
    if request.method == 'POST' and request.FILES['Upload']:
        title=request.POST.get('title')
        author=request.POST['author']
        category=request.POST['category']
        Upload = request.FILES['Upload']

    # 12/2/23
        Book_file = Book.objects.create(
                                       title=Upload.name,
                                       file=Upload
                                      )
        file_path= Book_file.file.path

        fss = FileSystemStorage()
        file = fss.save(Upload.name, Upload)
        file_url = fss.url(file)
        

        book = Book()
        book.title = title
        book.author = author
        book.category = category
        # book.upload = upload
        # book = Book.objects.create(title=title,author=author,category=category)
        book.save()
        print("book saved")
        return render(request, 'upload_books.html', {'file_url': file_url},{"file_path":file_path})
    return render(request, 'upload_books.html')


def book_details(request):
    book_details = Book.objects.all()
    # file = Book.objects.create(
    #                                    name=file.title,
    #                                    file=file
    #                                   )
    #     file_path= file.file.path

    return render(request,'book_details.html',{'book':book_details})








