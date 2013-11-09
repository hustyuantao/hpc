from django.db import models

# Create your models here.
# Field types: 
# 	AutoField, BigIntegerField, BinaryField, BooleanField
# 	CharField, CommaSeparatedIntegerField, DateField, DateTimeField
# 	DecimalField, EmailField, FileField, FilePathField
# 	FloatField, ImageField, IntegerField, IPAddressField
#	GenericIPAddressField, NullBooleanField, PositiveIntegerField
#	PositiveSmallIntegerField, SlugField, SmallIntegerField
#	TextField, TimeField, URLField
# Relationship fields:
#	ForeignKey, ManyToManyField, OneToOneField
class TopOneHundred(models.Model):
	nth = models.PositiveSmallIntegerField()
	rank = models.PositiveSmallIntegerField()
	previous_rank = models.PositiveSmallIntegerField(null=True)
	first_appearance = models.PositiveSmallIntegerField(null=True)
	first_rank = models.PositiveSmallIntegerField(null=True)
	name = models.CharField(max_length=64, null=True, blank=True)
	computer = models.CharField(max_length=256)
	site = models.CharField(max_length=64)
	manufacturer = models.CharField(max_length=32)
	reference = models.CharField(max_length=1)
	city = models.CharField(max_length=32, null=True, blank=True)
	year = models.PositiveSmallIntegerField()
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


class TopFiveHundred(models.Model):
	nth = models.PositiveSmallIntegerField()
	rank = models.PositiveSmallIntegerField()
	previous_rank = models.PositiveSmallIntegerField(null=True)
	first_appearance = models.PositiveSmallIntegerField()
	first_rank = models.PositiveSmallIntegerField()
	name = models.CharField(max_length=64, null=True, blank=True)
	computer = models.CharField(max_length=256)
	site = models.CharField(max_length=64)
	manufacturer = models.CharField(max_length=32)
	country = models.CharField(max_length=32)
	year = models.PositiveSmallIntegerField()
	segment = models.CharField(max_length=32)
	total_cores = models.IntegerField()
	accelerator_cores = models.IntegerField()
	rmax = models.FloatField()
	rpeak = models.FloatField()
	efficiency = models.FloatField()
	nmax = models.IntegerField()
	nhalf = models.IntegerField()
	power = models.FloatField(null=True)
	mflops_watt = models.FloatField(null=True)
	architecture = models.CharField(max_length=32)
	processor = models.CharField(max_length=32)
	processor_technology = models.CharField(max_length=32)
	processor_speed = models.PositiveSmallIntegerField()
	operating_system = models.CharField(max_length=32)
	os_family = models.CharField(max_length=12)
	accelerator = models.CharField(max_length=32)
	cores_per_socket = models.PositiveSmallIntegerField()
	processor_generation = models.CharField(max_length=32)
	system_model = models.CharField(max_length=32)
	system_family = models.CharField(max_length=32)
	interconnect_family = models.CharField(max_length=32)
	interconnect = models.CharField(max_length=32)
	region = models.CharField(max_length=32)
	continent = models.CharField(max_length=32)
	
	
	def __unicode__(self):
		return self.computer
