from django.db import models

# Create your models here.
class Ranking(models.Model):
	nth = models.PositiveSmallIntegerField()
	nyear = models.PositiveSmallIntegerField()
	
	rank = models.PositiveSmallIntegerField()
	previous_rank = models.PositiveSmallIntegerField(null=True)
	first_appearance = models.PositiveSmallIntegerField(null=True)
	first_rank = models.PositiveSmallIntegerField(null=True)
	name = models.CharField(max_length=64, null=True, blank=True)
	computer = models.CharField(max_length=256)
	site = models.CharField(max_length=64)
	manufacturer = models.CharField(max_length=32)
	reference = models.CharField(max_length=8)
	city = models.CharField(max_length=32, null=True, blank=True)
	year = models.CharField(max_length=32)
	segment = models.CharField(max_length=32)
	total_cores = models.IntegerField()
	accelerator_cores = models.IntegerField(null=True)
	rmax = models.FloatField()
	rpeak = models.FloatField()
	efficiency = models.FloatField()
	nmax = models.IntegerField(null=True)
	nhalf = models.IntegerField(null=True)
	power = models.FloatField(null=True)
	mflops_watt = models.FloatField(null=True)
	architecture = models.CharField(max_length=32, null=True, blank=True)
	processor = models.CharField(max_length=32, null=True, blank=True)
	processor_technology = models.CharField(max_length=32, null=True, blank=True)
	processor_speed = models.PositiveSmallIntegerField(null=True)
	operating_system = models.CharField(max_length=32, null=True, blank=True)
	os_family = models.CharField(max_length=12, null=True, blank=True)
	accelerator = models.CharField(max_length=32, null=True, blank=True)
	cores_per_socket = models.PositiveSmallIntegerField(null=True)
	processor_generation = models.CharField(max_length=32, null=True, blank=True)
	system_model = models.CharField(max_length=32, null=True, blank=True)
	system_family = models.CharField(max_length=32, null=True, blank=True)
	interconnect_family = models.CharField(max_length=32, null=True, blank=True)
	interconnect = models.CharField(max_length=32, null=True, blank=True)
	region = models.CharField(max_length=32, null=True, blank=True)
	
	def __unicode__(self):
		return self.computer
