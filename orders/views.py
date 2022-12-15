from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.admin.sites import site
# Create your views here.


class CustomView(TemplateView):
    template_name = "orders/order_tracking.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(site.each_context(self.request))
        return ctx
