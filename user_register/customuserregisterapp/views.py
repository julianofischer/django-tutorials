from django.shortcuts import render, redirect

from .forms import ProfessorForm, UserForm
# Create your views here.

def professor_register(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/redirect')
    else:
        form = ProfessorForm()
        context = {'form': form}
        return render(request, 'reg_professor_form.html', context)

def professor_register2(request):
    if request.method == 'POST':
        professor_form = ProfesorForm(request.POST)
        user_form  = UserForm(request.POST)

        if professor_form.is_valid() and user_form.is_valid():
            professor_form.save()
            user_form.save()
            return redirect('/redirect')
    else:
        professor_form = ProfessorForm()
        user_form = UserForm()
        context = {'professor_form': professor_form, 'user_form': user_form}
        return render(request, 'reg_professor_form2.html', context)
