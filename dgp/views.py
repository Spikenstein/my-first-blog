from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Run
from .forms import RunSelectionForm, RunParametersForm
from django.contrib.auth.decorators import login_required

def run_list(request):
    runs = Run.objects.all()
    paginator = Paginator(runs, 9)
    page = request.GET.get('page')
    try:
        paginatedRuns = paginator.page(page)
    except PageNotAnInteger:
        paginatedRuns = paginator.page(1)
    except EmptyPage:
        paginatedRuns = paginator.page(paginator.num_pages)
    return render(request, 'dgp/run_list.html', {'runs': paginatedRuns})

def run_detail(request, pk):
    run = get_object_or_404(Run, pk=pk)
    return render(request, 'dgp/run_detail.html', {'run': run})

@login_required
def newSelectionRun(request):
    if request.method == "POST":
        print(request.POST)
        selectionForm= RunSelectionForm(request.POST)
        if selectionForm.is_valid():
            run = selectionForm.save(commit=False)
            run.user = request.user
            run.date = timezone.now()
            run.log = "Ceci n'est pas un log de RunSelectionForm"
            run.save()
            return redirect('run_detail', pk=run.pk)
    else:
        selectionForm = RunSelectionForm()
    return render(request, 'dgp/newSelectionRun.html', {'selectionForm': selectionForm})

@login_required
def newParametersRun(request):
    if request.method == "POST":
        parametersForm = RunParametersForm(request.POST)
        if parametersForm.is_valid():
            #Test validité paramètres saisis
            run = parametersForm.save(commit=False)
            run.user = request.user
            run.date = timezone.now()
            run.log = "Ceci n'est pas un log de RunParametersForm"
            run.save()
            return redirect('run_detail', pk=run.pk)
    else:
        parametersForm = RunParametersForm()
    return render(request, 'dgp/newParametersRun.html', {'parametersForm':parametersForm})
