from django.shortcuts import render,redirect
from django.contrib import messages
from .models import voter,codes,cardidate
from django.shortcuts import get_object_or_404, redirect
import random

def voter_choose(request):
    return render(request, 'ask_voter.html')

def voter_num():
    while True:
        code = str(random.randint(10000, 99999))
        if not codes.objects.filter(code=code).exists():
            return code

def voter_reg(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        idname = request.POST.get('idname')

        if not firstname or not lastname or not idname :
                messages.error(request, 'Please fill in all fields.')
                return render(request, "voter_registration.html")
        if voter.objects.filter(idname=idname).exists():
                messages.error(request, 'the id number already exists.')
                return render(request, 'voter_registration.html')
        voter.objects.create(firstname=firstname, lastname=lastname, idname=idname)
        code = voter_num()
        codes.objects.create(code=code)
        return render(request, 'voter_code.html', {'voter_code': code})
    
    return render(request, 'voter_registration.html')

def cast_vote(request, candidate_id):
    if not request.session.get('voter_authenticated'):
        messages.error(request, "Access denied. Please enter your voter code.")
        return redirect('code_identification')
    
    candidate = get_object_or_404(cardidate, id=candidate_id)
    candidate.votes += 1
    candidate.save()
    request.session.flush()
    return redirect('done')  

def code_identification(request):
    if request.method == 'POST':
        code_input= request.POST.get('code_input')

        if not code_input:
            messages.error(request, 'Please fill in the field.')
            return render(request, "voter_entry.html")
        if codes.objects.filter(code=code_input).exists():
            codes.objects.filter(code=code_input).delete()
            request.session['voter_authenticated'] = True
            return redirect('voting')
        else:
            messages.error(request, 'Invalid voter code.')
            return render(request, 'voter_entry.html')
    return render(request, 'voter_entry.html')

def voting(request):
    if not request.session.get('voter_authenticated'):
        messages.error(request, "Access denied. Please enter your voter code.")
        return redirect('code_identification')
    
    cardidates= cardidate.objects.all()
    return render(request, 'dashboard.html', {'cardidates': cardidates})
    
def done(request):
    request.session.flush()

    return render(request , 'done.html')