from django.shortcuts import get_object_or_404, redirect, render

from homework_here.forms import Form
from homework_here.models import Person


def person(request):
    if request.method == "POST":
        form = Form(request.POST, instance=Person())
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = Form()
    return render(request, 'person.html', {'form': form})


def person_pk(request, pk):
    if request.method == "POST":
        person_p = get_object_or_404(Person, pk=pk)
        form = Form(request.POST, instance=person_p)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        person_p = get_object_or_404(Person, pk=pk)
        form = Form(instance=person_p)
    return render(request, 'person.html', {'form': form})