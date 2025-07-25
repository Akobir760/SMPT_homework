from django.shortcuts import render, redirect
from temp.forms import StudentForm

def contact_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = StudentForm()
        return render(request, 'home.html', {'form': form})


def success_page(request):
    return render(request, "success.html")
