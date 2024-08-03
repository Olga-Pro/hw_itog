from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Review
from .forms import ReviewForm

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)