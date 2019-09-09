from django.shortcuts import render, redirect, HttpResponse
from apps.login_reg.models import User, Book

# Create your views here.


def user_home(request):
    if request.session.get('user_id'):
        context = {
            'current_user': User.objects.get(id=request.session.get('user_id')),
            'books': Book.objects.all(),
        }
    return render(request, "fav_books/user_home.html", context)


def logout(request):
    request.session.clear()
    return redirect('/')


def add_book(request):
    current_user = User.objects.get(id=request.session['user_id'])
    new_book = Book.objects.create(title=request.POST['book_title'], description=request.POST['book_description'],
                                   uploaded_by=current_user)
    new_book.likers.add(current_user)
    return redirect('/redirect_to_user_home')


def details_book(request, book_id):
    current_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.get(id=book_id)
    print(this_book.title)

    context = {
        'this_book': Book.objects.filter(id=book_id),
        'this_book_likers': this_book.likers.all(),
    }
    return render(request, "fav_books/display_book.html", context)


def update_book(request, book_id):
    current_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.get(id=book_id)
    print(this_book.title)
    context = {
        'this_book': Book.objects.filter(id=book_id),
        'this_book_likers': this_book.likers.all(),
    }

    # this_book.title = request.POST.get('update_book_title', False)
    # this_book.description = request.POST.get('update_book_description', False)
    # this_book.uploaded_by = current_user
    # this_book.save()

    return render(request, "fav_books/update_book.html", context)


def post_update(request, book_id):
    current_user = User.objects.get(id=request.session['user_id'])
    updated_book = Book.objects.get(id=book_id)
    updated_book.title = request.POST['update_book_title']
    updated_book.description = request.POST['update_book_description']
    updated_book.uploaded_by = current_user
    updated_book.save()

    context = {
        'updated_book': Book.objects.get(id=book_id),
        'this_book': Book.objects.filter(id=book_id)
    }
    return render(request, "fav_books/update_book.html", context)
