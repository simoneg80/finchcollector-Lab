from django.shortcuts import render

# Temporary fake data until we connect to a database
finches = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]
# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {'finches': finches})