
from django.core.mail import send_mail
import ssl
import certifi
from django.conf import settings 

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
from django.contrib.auth.decorators import login_required


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
        username=request.POST.get('username')
        pwd=request.POST['pwd']
        cpwd=request.POST['cpwd']
       
        fullname=request.POST['fullname']
        public_visibility = 'public_visibility' in request.POST
        gender=request.POST['gender']
        
        age = request.POST['age']

        city=request.POST['city']
        state=request.POST['state']
        # cctype=request.POST['cctype']
        
        credit_num=request.POST['credit_num']
        cvc=request.POST['cvc']

        # expdate=request.POST.get('month') +', ' + request.POST.get('year')
        address = f'{city}, {state}' if city and state else ''

        if pwd != cpwd:
            return HttpResponse('passwords do not match')
        db = get_user_model()
        # user=db.objects.create_user(email=email,username=username,password=pwd,fullname=fullname,gender=gender,city=city,state=state,cctype=cctype,ccnumber=ccnumber,cvc=cvc,expdate=expdate,address=address)
        user=db.objects.create(email=email,
                               username=username,
                               password=pwd,
                               fullname=fullname,
                               gender=gender,
                               age=age,
                               city=city,
                               state=state, 
                               credit_num=credit_num,
                               cvc=cvc)
        print(user)
        print(user.email)
        user.set_password(pwd)
        user.save()


        # Send welcome email with SSL context
        subject = 'Welcome to the Social Book App'
        message = f'Hi {username} ,\n\n Welcome to the Social Book App! We are excited to have you join our community.'
        email_from = 'perficient50@gmail.com'
        recipient_list = [email]

        
        send_mail(subject,
                   message, 
                   email_from, 
                   recipient_list, 
                   fail_silently=False, )

            
        print("data saved")
        messages.success(request,'sucessfully registered')
        return render(request,'login.html')
    else:
        return render(request,'register.html')



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
            return render(request,'index.html',{'user':user})
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

@login_required
def registered_user(request):
    user_data = CustomUser.objects.filter(public_visibility=1)
    print(user_data)
    return render(request,'authsell.html',{'CustomUser':user_data})


@login_required
def upload_books(request):
    if request.method == 'POST' :
        title = request.POST['title']
        author = request.POST.get('author', '')
        category = request.POST.get('category', '')
        cost = request.POST.get('cost', '0.00')
        public_visibility = 'public_visibility' in request.POST
        
        cover = request.FILES.get('cover')
        file = request.FILES.get('file')
        
        book = Book(title=title, author=author, category=category, cost=cost, public_visibility=public_visibility, uploader=request.user)
        
        if cover:
            book.cover = cover
        if file:
            book.file = file
        
        book.save()

    # 12/2/23
        # Book_file = Book.objects.create(
        #                                title=Upload.name,
        #                                file=Upload
        #                               )
        # file_path= Book_file.file.path

        # fss = FileSystemStorage()
        # file = fss.save(Upload.name, Upload)
        # file_url = fss.url(file)
        

        # book = Book()
        # book.title = title
        # book.author = author
        # book.category = category
        # book.upload = upload
        # book = Book.objects.create(title=title,author=author,category=category)
      
        print("book saved")
        # return render(request, 'upload_books.html', {'file_url': file_url},{"file_path":file_path})
        return render(request, 'upload_books.html')
    
    return render(request, 'upload_books.html')

@login_required
def book_details(request):
    book_details = Book.objects.filter(public_visibility=True)
    # file = Book.objects.create(
    #                                    name=file.title,
    #                                    file=file
    #                                   )
    #     file_path= file.file.path

    return render(request,'book_details.html',{'book':book_details})



@login_required
def profile(request):
    return render(request,'profile.html')


@login_required

def my_books(request):
    books = Book.objects.filter(uploader=request.user)
    return render(request, 'my_books.html', {'book': books})