from django.shortcuts import render, redirect, get_object_or_404
from recepti.models import RecipeModel
from recepti.forms import RecipeForm
from django.views import generic


class CreateReceptiView(generic.CreateView):
    template_name = 'recepti/create_recepti.html'
    form_class = RecipeForm
    success_url = '/recepti_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReceptiView, self).form_valid(form=form)

class ReceptiListView(generic.ListView):
    template_name = 'recepti/recepti_list.html'
    context_object_name = 'recepti_list'
    model = RecipeModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class ReceptiDetailView(generic.DetailView):
    template_name = 'recepti/recepti_detail.html'
    context_object_name = 'recepti_id'

    def get_object(self, **kwargs):
        recepti_id = self.kwargs.get('id')
        return get_object_or_404(RecipeModel, id=recepti_id)

class DeleteReceptiView(generic.DeleteView):
    template_name = 'recepti/confirm_delete.html'
    success_url = '/recepti_list/'

    def get_object(self, **kwargs):
        recepti_id = self.kwargs.get('id')
        return get_object_or_404(RecipeModel, id=recepti_id)