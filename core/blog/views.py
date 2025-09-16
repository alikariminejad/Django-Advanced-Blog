from django.shortcuts import render

def indexView(request):
    name = "Ali"
    context = {"name": name}
    return render(request, "index.html", context)
