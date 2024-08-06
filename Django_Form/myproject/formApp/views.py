from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data
            # form.save()  # if you're using a ModelForm and want to save to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = RegistrationForm()

    return render(request, "register.html", {'form': form})
