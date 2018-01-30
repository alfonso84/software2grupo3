# -*- coding: utf-8 -*-
import datetime
import random

from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse

from groupthree.models import *



def get_usuarios_disponibles(request):
    """
    Obtienes todos los usuario excepto el que esta logeado
    """
    sala_id=request.GET.get('sala')
    los_usuarios_invitados = SalaUsuario.objects.filter(sala_id=sala_id)
    usuarios = User.objects.all().exclude(pk=request.user.pk).exclude(pk__in=los_usuarios_invitados.values_list('usuario_id', flat=True))

    usuarios_disponibles =''
    for usuario in usuarios:
        usuarios_disponibles += "<option value='%s'>%s</option>"%(usuario.pk,usuario.username)

    invitados =''
    for sala_usuario in los_usuarios_invitados:
        invitados += "<option value='%s'>%s</option>"%(sala_usuario.usuario.pk,sala_usuario.usuario.username)

    response = {}
    response['usuarios_disponibles'] = usuarios_disponibles
    response['invitados'] = invitados
    return JsonResponse(response)


def get_invitar_usuarios(request):
    """
    Invitar a los usuarios
    """
    sala_id=request.GET.get('sala')
    los_usuarios=request.GET.getlist('usuarios[]')
    for usuario in los_usuarios:
        SalaUsuario.objects.create(sala_id=sala_id,usuario_id=usuario)

    los_usuarios_invitados = SalaUsuario.objects.filter(sala_id=sala_id)
    usuarios = User.objects.all().exclude(pk=request.user.pk).exclude(pk__in=los_usuarios_invitados.values_list('usuario_id', flat=True))

    usuarios_disponibles =''
    for usuario in usuarios:
        usuarios_disponibles += "<option value='%s'>%s</option>"%(usuario.pk,usuario.username)

    invitados =''
    for sala_usuario in los_usuarios_invitados:
        invitados += "<option value='%s'>%s</option>"%(sala_usuario.usuario.pk,sala_usuario.usuario.username)

    response = {}
    response['usuarios_disponibles'] = usuarios_disponibles
    response['invitados'] = invitados
    return JsonResponse(response)


def get_iniciar(request):
    """
    Inciar
    """
    sala_id=request.GET.get('sala')
    los_juegos=request.GET.getlist('juegos[]')
    for juego in los_juegos:
        if juego!="on":
            SalaJuego.objects.create(sala_id=sala_id,juego_id=juego)


    response = {}
    return JsonResponse(response)
