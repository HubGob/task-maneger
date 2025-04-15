from django.shortcuts import render
from django.views.generic import ListView
from .models import Task
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin 


class TaskListView(LoginRequiredMixin, ListView):  # Add LoginRequiredMixin
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        # Only show tasks for logged-in users
        return Task.objects.filter(user=self.request.user)
    
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description']  # Fields to include in form
    success_url = reverse_lazy('task-list')  # Where to redirect after submit

    def form_valid(self, form):
        # Assign task to current user before saving
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']  # Editable fields
    template_name = 'tasks/task_form.html'  # Reuse create template
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        # Optional: Add custom logic before saving
        return super().form_valid(form)
    
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
@require_POST
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task-list')