from django.shortcuts import render
from django.http import JsonResponse
from .generation import generate_text

def generate_view(request):
    if request.method == "POST":
        prompt = request.POST.get('prompt', '')
        role = request.POST.get('role', 'user')
        temperature = float(request.POST.get('temperature', 0.7))
        max_tokens = int(request.POST.get('max_tokens', 100))
        top_p = float(request.POST.get('top_p', 1.0))
        top_k = int(request.POST.get('top_k', 50))

        generated_text = generate_text(prompt, role, temperature, max_tokens, top_p, top_k)
        return JsonResponse({'generated_text': generated_text})

    return render(request, 'textgen/generate.html')
