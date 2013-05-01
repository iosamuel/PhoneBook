from django.db import models

class Datos(models.Model):
	nombres = models.CharField(max_length=150)
	apellidos = models.CharField(max_length=150)
	numero = models.IntegerField()
	direccion = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s %s" % (self.nombres, self.apellidos)