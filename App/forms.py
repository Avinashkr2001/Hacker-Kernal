from django import forms
from .models import Author,Book
class author_form(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.CharField(label='Email')
    bio=forms.CharField(label='Bio')
class book_form(forms.Form):
    title = forms.CharField(label='Title')
    genre=forms.CharField(label='Genre')
    published_date=forms.DateField(label='Published Date',widget=forms.DateInput(attrs={'type':'date'}))
    
    def __init__(self, *args,**kwargs):
        super(book_form,self).__init__(*args,**kwargs)
        authors=Author.objects.all()
        author_choices=[(author.id,author.name) for author in authors]
        self.fields['author']=forms.ChoiceField(label='Author',choices=author_choices)
    
class record_form(forms.Form):
    user_name=forms.CharField(label='User_name')
    borrow_date=forms.CharField(label='Borrow Date',widget=forms.DateInput(attrs={'type':'date'}))
    return_date=forms.CharField(label='Return Date',widget=forms.DateInput(attrs={'type':'date'}))
    
    def  __init__(self, *args,**kwargs):
        super(record_form,self).__init__(*args,**kwargs)
        books=Book.objects.all()
        book_choices=[(book.id,book.title) for book in books]
        self.fields['book']=forms.ChoiceField(label='Book',choices=book_choices)
    
    