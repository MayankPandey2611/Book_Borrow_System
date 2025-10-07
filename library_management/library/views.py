from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import User, Book, BorrowedBook
from .forms import  BookForm
from django.contrib import messages
from django.core.mail import send_mail

# Home Page
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html',{'books':books})

# Admin Login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user and user.is_admin:
            login(request, user)
            return redirect('admin_dashboard')
    return render(request, 'admin/admin_login.html')


def student_register(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate passwords
        if password != confirm_password:
            error = "Passwords do not match!"
        elif User.objects.filter(email=email).exists():
            error = "Email already registered!"
        elif User.objects.filter(username=username).exists():
            error = "Username already taken!"
        else:
            # Create student
            student = User.objects.create(
                username=username,
                email=email,
                password=make_password(password),
                is_student=True
            )
            return redirect('student_login')

    return render(request, 'students/student_register.html', {'error': error})

# Student Login
def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user and user.is_student:
            login(request, user)
            return redirect('student_dashboard')
    return render(request, 'students/student_login.html')


@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return redirect('home')

    books = Book.objects.all()
    students = User.objects.filter(is_student=True)  # ✅ All registered students
    return render(request, 'admin/admin_dashboard.html', {'books': books, 'students': students})


# Add Book
@login_required
def add_book(request):
    if not request.user.is_admin:
        return redirect('home')
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BookForm()
    return render(request, 'admin/add_book.html', {'form': form})

# Student Dashboard
@login_required
def student_dashboard(request):
    if not request.user.is_student:
        return redirect('home')
    books = Book.objects.filter(status=True)
    borrowed = BorrowedBook.objects.filter(student=request.user)
    return render(request, 'students/student_dashboard.html', {'books': books, 'borrowed': borrowed})




def borrow_book(request, book_id):
 
    if not request.user.is_authenticated:
        messages.warning(request, "Please register as a student before borrowing a book.")
        return redirect('student_register')

   
    if not request.user.is_student:
        messages.warning(request, "Only registered students can borrow books. Please register.")
        return redirect('student_register')

  
    book = get_object_or_404(Book, id=book_id)
    if book.status:
        BorrowedBook.objects.create(student=request.user, book=book)
        book.status = False
        book.save()
        messages.success(request, f'You have successfully borrowed "{book.title}".')
    else:
        messages.error(request, f'Sorry, "{book.title}" is already borrowed.')

    return redirect('student_dashboard')



@login_required
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book) 
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'admin/update_book.html', {'form': form})


@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('admin_dashboard')

def delete_student(req,student_id):
    student = get_object_or_404(User,id=student_id)
    student.delete()
    return redirect('admin_dashboard')

@login_required
def return_book(request, book_id):
    borrowed_record = get_object_or_404(BorrowedBook, id=book_id, student=request.user)

   
    borrowed_record.book.status = True
    borrowed_record.book.save()

  
    borrowed_record.delete()
    return redirect('student_dashboard')

def logout(req):
    req.session.flush()
    return redirect('home')


from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def mail(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        contact = req.POST.get('contact')
        msg = req.POST.get('msg')

        subject = f"New message from {name}"
        message = f"""
        You have received a new message:

        Name: {name}
        Email: {email}
        Contact: {contact}
        Message: {msg}
        """

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,    
            ["kitupnd@gmail.com"],        
            fail_silently=False,
        )

        return HttpResponse("Mail sent successfully")
