from django.views.generic import ListView

class IndexView(ListView):
    template_name = "index.html"
    