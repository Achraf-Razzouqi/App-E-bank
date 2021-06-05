from django.shortcuts import render, redirect
from account.models import *
from account.forms import *
# Create your views here.
def index(request):
    if request.session.get('user_id') is None:
        return redirect('/login')
    u=Use.objects.all()
    context= {'i':u}
    return render(request, 'admin/index.html', context)
def Acheque(request):
    if request.session.get('user_id') is None:
        return redirect('/login')
    u=Use.objects.all().filter(cheque="Demandé")
    context= {'i':u}
    return render(request, 'admin/Acheque.html', context)

def AcC(request,pk):
    index = Use.objects.get(id=pk)
    index.cheque="Accepter"
    index.save()
    return redirect('Acheque')
def ReC(request,pk):
    index = Use.objects.get(id=pk)
    index.cheque="Refuser"
    index.save()
    return redirect('Acheque')

def Arec(request):
    index = Reclamation.objects.all()
    context={'i':index}

    return render(request,'admin/Areclamation.html',context)

def deleteR(request,pk):
    if request.session.get('user_id') is None:
        return redirect('login.html')
    op= Reclamation.objects.get(id=pk)
    op.delete()
    return redirect('/admins/Arec')

def update(request,pk):
    if request.session.get('user_id') is None:
        return redirect('/login')
    op= Use.objects.get(id=pk)
    form= UserFrom(instance=op)
    if request.method == 'POST':
        form = UserFrom(request.POST, instance=op)
        if form.is_valid():
            form.save()
            return redirect('/admins/index')
    context= {'form':form}
    return render(request, 'admin/update.html', context)

def create(request):
    if request.session.get('user_id') is None:
        return redirect('/login')
    form= UserFrom()
    if request.method == 'POST':
        form = UserFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admins/index')
    context= {'form':form}
    return render(request, 'admin/update.html', context)

def cip(request):
    if request.session.get('user_id') is None:
        return redirect('/login')
    op= Use.objects.get(id=request.session.get('user_id'))
    form= AdminFrom(instance=op)
    if request.method == 'POST':
        form = AdminFrom(request.POST, instance=op)
        if form.is_valid():
            form.save()
            return redirect('/admins/index')
    context= {'form':form ,'i':op}
    return render(request, 'admin/CIP.html', context)




def delete(request,pk):
    if request.session.get('user_id') is None:
        return redirect('login.html')
    op= Use.objects.get(id=pk)
    if request.method == 'POST':
        op.delete()
        return redirect('/admins/index')
    context= {'user':op}
    return render(request, 'admin/delete.html', context)

def logout(request):
    del request.session['user_id']
    del request.session['con_id']
    return redirect('/login')