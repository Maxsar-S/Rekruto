from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.GET.get('name')
        context['message'] = self.request.GET.get('message')

        return context
