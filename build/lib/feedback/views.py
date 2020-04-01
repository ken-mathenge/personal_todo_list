from django.views.generic.edit import FormView
from feedback.forms import FeedbackForm


class FeedbackView(FormView):
    template_name = 'contact.html'
    form_class = FeedbackForm
    success_url = '/'

    def form_valid(self, form):  # pragma: no cover
        form.send_email()
        return super(FeedbackView, self).form_valid(form)
