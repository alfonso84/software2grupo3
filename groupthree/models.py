# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from decimal import Decimal


class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	saldo = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('500.00'))


class Juego(models.Model):
	juego_id = models.AutoField(primary_key=True)
	juego = models.CharField(max_length=250)

	def __str__(self):
		return self.juego


class Sala(models.Model):
	sala_id = models.AutoField(primary_key=True)
	capacidad_maxima = models.IntegerField()
	cantidad_usuarios = models.IntegerField(default=0)
	es_publica = models.BooleanField(default=0)
	usuario_organizador = models.ForeignKey(User)

	def __str__(self):
		return self.sala_id

class SalaUsuario(models.Model):
	sala_usuario_id = models.AutoField(primary_key=True)
	sala = models.ForeignKey(Sala)
	usuario = models.ForeignKey(User, related_name='+')

class SalaJuego(models.Model):
	sala_usuario_id = models.AutoField(primary_key=True)
	sala = models.ForeignKey(Sala)
	juego = models.ForeignKey(Juego, related_name='+')


def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Perfil.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
