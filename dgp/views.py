from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Run
from .forms import RunForm
from django.contrib.auth.decorators import login_required

def run_list(request):
    runs = Run.objects.all()
    return render(request, 'dgp/run_list.html', {'runs': runs})

def run_detail(request, pk):
    run = get_object_or_404(Run, pk=pk)
    return render(request, 'dgp/run_detail.html', {'run': run})

@login_required
def newRun(request):
    if request.method == "POST":
        form = RunForm(request.POST)
        if form.is_valid():
            run = form.save(commit=False)
            run.user = request.user
            run.date = timezone.now()
            run.log = "Ceci n'est pas un log"
            run.save()
            return redirect('run_detail', pk=run.pk)
    else:
        form = RunForm()
    return render(request, 'dgp/newRun.html', {'form': form})
