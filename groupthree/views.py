#-*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from groupthree.forms import *
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.shortcuts import render, redirect


class Login(LoginView):
    authentication_form = LoginForm


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'groupthree/home.html'

    def get_context_data(self, *arg, **kwargs):
        context = super(Home, self).get_context_data(*arg, **kwargs)
        return context

def registeruser(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home')
    else:
        f = CustomUserCreationForm()
    return render(request, 'groupthree/register.html', {'form': f})


class SalaPublicaListView(LoginRequiredMixin, TemplateView):
    template_name = 'groupthree/sala_publica.html'

    def get_context_data(self, *arg, **kwargs):
	    context = super(SalaPublicaListView, self).get_context_data(*arg, **kwargs)
	    return context

class CrearSalaView(LoginRequiredMixin, TemplateView):
    template_name = 'groupthree/crear_sala.html'

    def get_context_data(self, **kwargs):
        context = super(CrearSalaView, self).get_context_data()
        form = CrearSalaForm()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CrearSalaForm(request.POST)
        if form.is_valid():
            sala = form.save(commit=False)
            sala.usuario_organizador = request.user
            sala.save()
            if sala.es_publica:
                return redirect('sala_publica_list', **kwargs)
            else:
                url = reverse('crear_sala_privada', kwargs={'sala_id': sala.sala_id})
                return HttpResponseRedirect(url)
        context = self.get_context_data()
        context.update({
            'form': form,
        })
        return self.render_to_response(context)



class CrearSalaPrivadaView(LoginRequiredMixin, TemplateView):
    template_name = 'groupthree/crear_sala_privada.html'

    def get_context_data(self, **kwargs):
        context = super(CrearSalaPrivadaView, self).get_context_data()
        sala_id = self.kwargs.get('sala_id')
        sala = False
        es_privada = False
        sala_privada = Sala.objects.filter(sala_id=sala_id)
        if sala_privada.exists():
            sala = True
            sala_privada = sala_privada.get()
            if sala_privada.es_publica == False:
                es_privada = True

        context['sala_id'] = sala_id
        context['sala'] = sala
        context['es_privada'] = es_privada
        return context
