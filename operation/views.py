import hashlib
from datetime import date
from hashlib import md5

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import OperForm
from .models import Operation
from account.models import *
from django.db.models import Q
#foreign key conseiller kayn fe user
# Create your views here.
def index(request):
    ind = Use.objects.get(id=request.session.get('user_id'))
    #Item.objects.filter(Q(creator=owner) | Q(moderated=False))
    index = Operation.objects.filter(idR=request.session.get('user_id')).filter (Q(type="Credit") | Q(type="Debit")).order_by("-id")
    #var=Use.objects.filter(id)
    con = Conseille.objects.get(id =request.session.get('con_id'))
    context = {'i':index, 'c':con,'in':ind}
    return render(request, 'index.html', context)


def create(request):
    if request.session.get('user_id') is None:
        return redirect('/login')
    form = OperForm()

    op = Use.objects.get(id=request.session.get('user_id'))
    con=Conseille.objects.get(id=request.session.get('con_id'))

    if request.method == 'POST':
        regform = OperForm(request.POST)
        s= regform.data['solde']
        s_float= float(s)


        if regform.is_valid():
            idr=request.session.get('user_id')
            idd=regform.data['idD']
            so= regform.data['solde']
            t=regform.data['type']
            oa = Use.objects.get(id=idd)
            o= Operation.objects.create(idR_id=idr,idD_id=idd,type=t, solde=so, Adate=date.today())
            if regform.data['type'] == "Credit":
                if s_float<op.solde:
                    op.solde -= s_float
                    op.solde -= 1

                    oa.solde+=s_float
                    oa.save()
            else:
                op.solde+=s_float
            if op.type == "particulier":
                op.solde-=5
            op.save()
            blockchain = Blockchain()
            print(blockchain.chain)

            transaction = "Operation"
            transaction.encode('utf-8')
            i=b.objects.count()

            result = hashlib.md5(transaction.encode())
            blockchain.add_new_transaction(result)
            i=b.objects.create(text=result.hexdigest())

            messages.success(request, "Transaction est effectue avec succes")
    context = {'forms': form,'i': op, 'c':con}
    return render(request, 'create.html', context)

def logout(request):
    del request.session['user_id']
    del request.session['con_id']
    return redirect('/login')