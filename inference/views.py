from django.views import View
from django.http import HttpResponse



class InferenceView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")
    
    def post(self, request):
        prompt = request.POST.get('prompt')
        negative_prompt = request.POST.get('negative_prompt')
        
        num_of_images = int(request.POST.get('num_of_images', 1))
        
    

