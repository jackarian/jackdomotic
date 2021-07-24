# from django.contrib import admin
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.template.response import TemplateResponse
from django.urls import include, path
# Register your models here.
from control.models import Email, Configuration, Channel, Resource, ResourcePolicy, Plc, Ssc, Networklocation, ResourcePolicyAdmin, \
    NetworklocationAdmin, Users
from django.utils.translation import gettext_lazy
from django.contrib.auth import get_user_model


class MyAdminSite(admin.AdminSite):
    site_title = gettext_lazy('Smartstation admin')

    site_header = gettext_lazy('Smartstation administration')

    final_catch_all_view = True

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('prenotazioni/', self.prenotazioni, name="prenotazioni"),
            path('gestione-risorse/', self.gestioneRisorse, name="gestione-risorse"),
        ]
        return urls

    def prenotazioni(self, request):
        context = dict(
            # Include common variables for rendering the admin template.
            self.each_context(request),
        )
        return TemplateResponse(request, "control/index.html", context)

    def gestioneRisorse(self, request):
        context = dict(
            # Include common variables for rendering the admin template.
            self.each_context(request),
        )
        return TemplateResponse(request, "control/gestione_risorse.html", context)


admin_site: MyAdminSite = MyAdminSite(name='myadmin')

admin_site.register(Email)

admin_site.register(Configuration)

admin_site.register(Channel)

admin_site.register(Resource)

admin_site.register(ResourcePolicy, ResourcePolicyAdmin)

admin_site.register(Plc)

admin_site.register(Networklocation, NetworklocationAdmin)

admin_site.register(Ssc)

admin_site.register(get_user_model())

admin_site.register(Users)
