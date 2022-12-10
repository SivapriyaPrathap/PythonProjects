from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .models import Todo
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class Listview(ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'todo1'
class Detail_view(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'detail'

class Update_view(UpdateView):
    model = Todo
    template_name = 'edit.html'
    context_object_name = 'update'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('Detail_view',kwargs={'pk':self.object.id})



class Delete_view(DeleteView):

        model = Todo
        template_name = 'delete.html'
        context_object_name = 'detail'
        success_url = "index"



def index(request):
    todo1 = Todo.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        todo=Todo(name=name,priority=priority,date=date)
        todo.save()

    return render(request,"index.html",{'todo1':todo1})

#def detail(request):
    #todo=Todo.objects.all()
    #return render(request,"detail.html",{'todo':todo})

def delete(request,id):
    d=Todo.objects.get(id=id)
    if request.method == "POST":
          d.delete()
          return redirect("/index")

    return render(request,'delete.html')

def update(request,id):
    d=Todo.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=d)
    if form.is_valid():
        form.save()
        return redirect('/index')
    return render(request,'update.html',{'d':d,'form':form})