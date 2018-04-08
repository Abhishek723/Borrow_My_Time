from django.views.generic import TemplateView
class DashboardPage(TemplateView):
    template_name='dashboard.html'
class ThanksPage(TemplateView):
    template_name='thanks.html'
class HomePage(TemplateView):
    template_name='index.html'
