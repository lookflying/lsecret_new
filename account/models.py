from django.db import models

class Account(models.Model):
		username = models.CharField(max_length=255)
		income = models.DecimalField(max_digits=20, decimal_places=2, default=0)
		expense = models.DecimalField(max_digits=20, decimal_places=2, default=0)

		def balance(self):
				return income - expense

		def __unicode__(self):
				return self.username + "'s Account"

class AccountEvent(models.Model):
		account = models.ForeignKey(Account)
		item = models.CharField('item name', max_length=255)
		description = models.TextField('description')
		date = models.DateField()
		income = models.DecimalField(max_digits=20, decimal_places=2, default=0)
		expense = models.DecimalField(max_digits=20, decimal_places=2, default=0)
		
		def balance(self):
				return income - expense
		
		def __unicode__(self):
				return self.item
