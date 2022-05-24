from django.shortcuts import render
from django.views.generic import FormView
from .forms import BioForm


class HomeView(FormView):
    template_name = 'biotools/index.html'
    form_class = BioForm

def seq(request):
    if request.method == 'POST':
        filled_form = BioForm(request.POST)
        if filled_form.is_valid():
            note = f"The input sequence: {filled_form.cleaned_data['input_seq']}."
            new_form = BioForm()
            return render(request, 'biotools/seq.html', {'seq_info':new_form, 'note':note})
    else:
        form = BioForm()
        return render(request, 'biotools/seq.html', {'seq_info': form})
