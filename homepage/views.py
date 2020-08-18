from django.shortcuts import render
from homepage.models import CowsayInput
from homepage.forms import InputForm
import subprocess


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = subprocess.run(['cowsay', '{}'.format(data.get('user_input'))], capture_output=True, text=True)
            CowsayInput.objects.create(
                user_input = data.get('user_input')
            )
            form = InputForm()
            return render(request, 'index.html', {'form': form, 'result': result.stdout})
            
    return render(request, 'index.html', {'form': form})

def history(request):
    allstrings =  CowsayInput.objects.all()
    return render(request, 'history.html', {'allstrings': allstrings})
