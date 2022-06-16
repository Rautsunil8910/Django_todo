
from django.contrib import messages
from todo_app.forms import Todoform
from todo_app.models import TodoList
from django.shortcuts import redirect, render
from .models import TodoList

# Create your views here.
def search(request):
    if request.method =='POST':

    
        query_data = request.POST['content']

        #query_data = request.POST.get('content',None)
     
        if query_data:
            
            results = TodoList.objects.filter(content = query_data)
            return render(request ,'search.html',{'results':results})

           

        else:
            messages.info(request,'data does not exist')
            return redirect('search')
    return render(request,'search.html')



#

# def home(request):
    if request.method == 'POST':
        content = request.POST['content']
        
        if TodoList.objects.filter(content=content).exists():

                messages.info(request,'content already exists')
                return redirect('/')
        else:
            try:
                user = TodoList.objects.create(content = content)
               
            except:
                
                return redirect('/')
            user.save()
       
    items = TodoList.objects.all()
 
    return render(request ,'home.html',{'items':items})


def home(request):
    if request.method == 'POST':
        content = request.POST['content']
        
        try:
            user = TodoList.objects.create(content = content)
           
        except:
            
            return redirect('/')
        user.save()
    items = TodoList.objects.all()
 
    return render(request ,'home.html',{'items':items})



def update(request ,i):
    i = int(i)
    try:
        boid = TodoList.objects.get(id= i)

    except TodoList.DoesNotExist:
        return redirect('/')
    book_form = Todoform(request.POST or None, instance=boid)
    if book_form.is_valid():
        book_form.save()
        return redirect('/')
    return render(request ,'form.html',{'dest':book_form})

# def home(request):

#     if request.method == 'POST':
#         content = request.POST['content']
#         user = TodoList.objects.create(content = content)
#         user.save()
#     items = TodoList.objects.all()
#     return render(request ,'home.html',{'items':items})
    

# create delete todo list
def delete(request,i):
    i = int(i)
    try:
        data = TodoList.objects.get(id = i)
    except TodoList.DoesNotExist:
    
        return redirect('/')
    data.delete()
    return redirect('/')
# def delete(request ,i):
#     i = int(i)
#     data = TodoList.objects.get(id = i)
#     data.delete()
#     return redirect('/')
    


    