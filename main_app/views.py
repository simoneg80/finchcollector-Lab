from django.shortcuts import render


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  # finches = Finch.objects.all()
  return render(request, 'finches/index.html', )