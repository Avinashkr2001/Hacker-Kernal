from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from .forms import author_form,book_form,record_form
from .models import Author,Book,BorrowRecord
from django.contrib import messages
from django .core.paginator import Paginator
import pandas as pd
import re

def home(request):
    all_data=Author.objects.all()
    paginator=Paginator(all_data,10)
    page_number=request.GET.get('page')
    data=paginator.get_page(page_number)
    total_page=data.paginator.num_pages
    list=[n+1 for n in range(total_page)]
    return render(request,'author.html',{'data':data,'page':list})
def books(request):
    all_data=Book.objects.all()
    paginator=Paginator(all_data,10)
    page_number=request.GET.get('page')
    data=paginator.get_page(page_number)
    total_page=data.paginator.num_pages
    list=[n+1 for n in range(total_page)]
    return render(request,'book.html',{'data':data,'page':list})
def records(request):
    all_data=BorrowRecord.objects.all()
    paginator=Paginator(all_data,10)
    page_number=request.GET.get('page')
    data=paginator.get_page(page_number)
    total_page=data.paginator.num_pages
    list=[n+1 for n in range(total_page)]
    return render(request,'record.html',{'data':data,'page':list})
def add_author(request):
    if request.method == 'POST':
        form = author_form(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            bio=form.cleaned_data['bio']
            pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$'
            if re.match(pattern,email):
                Author.objects.create(name=name,email=email,bio=bio)
                messages.success(request,'Author Added Successfully')
                return redirect('home')
            else:
                messages.error(request,'Please Enter valid Email')
                return
    else:
        form=author_form()
    return render(request,'add_author.html',{'form':form})      
def add_book(request):
    if request.method=='POST':
        form=book_form(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            genre=form.cleaned_data['genre']
            published_date=form.cleaned_data['published_date']
            author_id=form.cleaned_data['author']
            author=get_object_or_404(Author,id=author_id)
            Book.objects.create(title=title,genre=genre,published_date=published_date,author=author)
            messages.success(request,'Book Added Successfully')
            return redirect('books')
    else:
        form=book_form()
    return render(request,'add_book.html',{'form':form})
def add_record(request):
    if request.method=="POST":
        form=record_form(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['user_name']
            borrow_date=form.cleaned_data['borrow_date']
            return_date=form.cleaned_data['return_date']
            book_id=form.cleaned_data['book']
            book=get_object_or_404(Book,id=book_id)
            BorrowRecord.objects.create(user_name=user_name,borrow_date=borrow_date,return_date=return_date,book=book)
            messages.success(request,'Record Added Successfully')
            return redirect('records')
    else:
        form=record_form()
    return render(request,'add_record.html',{'form':form})

def export_records(request):
    records=BorrowRecord.objects.all()
    data=[]
    for record in records:
        data.append({
            'Id':record.id,
            'User Name':record.user_name,
            'Borrow Date':record.borrow_date,
            'Return Date':record.return_date,
            'Book':record.book
        })
        df=pd.DataFrame(data)
        response=HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheet.sheet')
        response['Content-Disposition']='attachment; filename="Records.xlsx"'
        
        with pd.ExcelWriter(response,engine='openpyxl') as writer:
            df.to_excel(writer,sheet_name='Records',index=False)
        return response
    
def export_book_records(request):
    records=Book.objects.all()
    data=[]
    for record in records:
        data.append({
            'Id':record.id,
            'Title':record.title,
            'Genre':record.genre,
            'Published Date':record.published_date,
            'Author':record.author
        })
        df=pd.DataFrame(data)
        response=HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheet.sheet')
        response['Content-Disposition']='attachment; filename="Book_Records.xlsx"'
        
        with pd.ExcelWriter(response,engine='openpyxl') as writer:
            df.to_excel(writer,sheet_name='Book_Records',index=False)
        return response
    
def export_author_records(request):
    records=Author.objects.all()
    data=[]
    for record in records:
        data.append({
            'Id':record.id,
            'Name':record.name,
            'Email':record.email,
            'Bio':record.bio
        })
        df=pd.DataFrame(data)
        response=HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheet.sheet')
        response['Content-Disposition']='attachment; filename="Author_Records.xlsx"'
        
        with pd.ExcelWriter(response,engine='openpyxl') as writer:
            df.to_excel(writer,sheet_name='Author_Records',index=False)
        return response
