from datetime import date

from django.contrib.messages.storage import session
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import *
from operation.models import *
from .forms import *
import random
from django.contrib.sessions import base_session
from django.contrib.auth import authenticate, login
# Create your views here.

def register(request):
    form = rFrom()
    if request.method == 'POST':
        regform = rFrom(request.POST)
        if regform.is_valid():
            n = regform.data['nom']
            pr = regform.data['prenom']
            c = regform.data['cne']
            pa = regform.data['password']
            p = regform.data['phone']
            a = regform.data['age']
            ad = regform.data['adress']

            con = Conseille.objects.get(address=ad)
            i=con.id

            u = Use.objects.create(nom=n,prenom=pr,cne=c,password=pa,phone=p,age=a,adress=ad, idC_id=i)
            print(u)
            u.save()
            #regform.save()
            messages.success(request,"User has been created")
    context = {'form': form}
    return render(request, 'register.html', context)


def getId(request):
    con = Conseille.objects.get(id=request.session.get('con_id'))

    op = Use.objects.get(id=request.session.get('user_id'))
    context={'i':op, 'c': con}
    return render(request, 'account/rib.html', context)

def dotationE(request):
    index = Use.objects.get(id=request.session.get('user_id'))
    e="Bloquer"
    t="Bloquer"
    if index.dotationE== "Bloquer":
        e="Debloquer"


    if index.dotationT== "Bloquer":
        t="Debloquer"

    con = Conseille.objects.get(id=request.session.get('con_id'))

    context = {'e': e,'t':t,'c': con,'i':index}
    return render(request, 'account/dotaionE.html', context)

def hT(request):
    con = Conseille.objects.get(id=request.session.get('con_id'))
    index = Operation.objects.all().filter(idR_id=request.session.get('user_id'), type="Telephonique").order_by("-id")
    return render(request, 'account/hT.html',{'i':index, 'c': con})
def conseille(request):
    con = Conseille.objects.get(idC=request.session.get('user_id'))
    index= Use.objects.get(id=request.session.get('user_id'))
    return render(request, 'account/conseiller.html',{'i':index,'c':con})
def hF(request):
    con = Conseille.objects.get(id=request.session.get('con_id'))
    index = Operation.objects.all().filter(idR_id=request.session.get('user_id'), type="Eau-Electricité").order_by("-id")
    return render(request, 'account/hF.html',{'i':index, 'c': con})
def home(request):
    con = Conseille.objects.get(id=request.session.get('con_id'))
    index = Use.objects.get(id=request.session.get('user_id'))
    return render(request, 'account/home.html',{'i':index, 'c': con})


def cheque(request):
    con = Conseille.objects.get(id=request.session.get('con_id'))
    index = Use.objects.get(id=request.session.get('user_id'))
    return render(request, 'account/cheque.html',{'i':index,'c':con})

def c(request):
    index = Use.objects.get(id=request.session.get('user_id'))
    if index.cheque == "non":
        index.cheque="Demandé"
        index.save()
    return redirect('cheque')
def reclamation(request):
    con = Conseille.objects.get(id=request.session.get('con_id'))
    index = Use.objects.get(id=request.session.get('user_id'))
    if request.method == 'POST':
        i=index.id
        r=request.POST.get('rec')
        re=Reclamation.objects.create(text=r,idU_id=i, Adate=date.today())
        re.save()
    context={'i':index, 'c': con}
    return render(request, 'account/reclamation.html', context)
def tele(request):
    con = Conseille.objects.get(id=request.session.get('con_id'))
    index = Use.objects.get(id=request.session.get('user_id'))
    if request.method== "POST":
        #return redirect('dotationE')
        m=request.POST.get('m')
        o=request.POST.get('o')
        t=request.POST.get('t')

        #s = regform.data['solde']
        s_float = float(m)

        if index.solde>=s_float:
            index.solde-=s_float
            Op= Operation.objects.create(solde=m, type="Telephonique",idR_id=request.session.get('user_id'),operation=o, telephobe=t,Adate=date.today())
            index.save()

            Op.save()
            messages.success(request, "Vous avez rechargé votre téléphone")

    context={'i':index, 'c': con}
    return render(request, 'account/telephonique.html',context)
def facture(request):
    n = random.randint(300, 500)
    index = Use.objects.get(id=request.session.get('user_id'))
    con = Conseille.objects.get(id=request.session.get('con_id'))
    if request.method== "POST":
        m=request.POST.get('m')
        o=request.POST.get('o')

       # s_float = float(m)
        index = Use.objects.get(id=request.session.get('user_id'))
        con = Conseille.objects.get(id=request.session.get('con_id'))
        if index.solde>=n:
            index.solde-=n
            Op= Operation.objects.create(solde=n, type="Eau-Electricité",idR_id=request.session.get('user_id'),operation=o, Adate=date.today())
            index.save()

            Op.save()
            messages.success(request, "Vous avez payé votre facture ")

    return render(request, 'account/facture.html',{'n':n,'i':index,'c':con})

def aE(request):
    index = Use.objects.get(id=request.session.get('user_id'))
    if index.dotationE== "Bloquer":
        if index.solde > 100:
            index.solde -= 100
            index.dotationE = "Debloquer"
            index.save()
    else:
        index.dotationE = "Bloquer"
        index.save()
    return redirect('dotationE')
def aT(request):
    index = Use.objects.get(id=request.session.get('user_id'))
    if index.dotationT=="Bloquer":
        if index.solde>100:
            index.solde-=100
            index.dotationT="Debloquer"
            index.save()
    else:
        index.dotationT="Bloquer"
        index.save()
    return redirect('dotationE')

def getSolde(request):
    op = Use.objects.get(id=request.session.get('user_id'))
    con = Conseille.objects.get(id=request.session.get('con_id'))
    context={'i':op, 'c': con}

    return render(request, 'account/solde.html', context)


def update(request):
    if request.session.get('user_id') is None:
        return redirect('/login')
    op= Use.objects.get(id=request.session.get('user_id'))
    form= tFrom(instance=op)
    if request.method == 'POST':
        form = tFrom(request.POST, instance=op)
        if form.is_valid():
            form.save()
            return redirect('/admins/index')
    con = Conseille.objects.get(id=request.session.get('con_id'))
    context= {'form':form, 'c': con,'i':op}
    return render(request, 'account/update.html', context)

def Mlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password= request.POST.get('password')
        au= Use.objects.all()
        for u in au:
            if u.cne == username:
                if u.password == password:
                    try:
                        con = Conseille.objects.get(cni=u.idC)
                        print(u.idC)
                        request.session['con_id'] = con.id
                        request.session['user_id']=u.id

                    except:
                        the_id= None
                    request.session.get('user_id',u.id)
                    request.session.get('con_id',u.idC)
                    if u.type == "admin":
                        return redirect('/admins/index')
                    return redirect('home')
    return render(request,'login.html')