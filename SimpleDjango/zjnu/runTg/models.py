from django.db import models

# Create your models here.
class RunRecord(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=16)
	content = models.CharField(max_length=255)
	time = models.DateTimeField()
	user_id = models.ForeignKey(
		'user.User',
		to_field='id',
		on_delete=models.CASCADE
	)
	num = models.IntegerField()
	isfull = models.BooleanField(default=False)

class RunJoinRecord(models.Model):
	runRecord_id = models.ForeignKey(
		'runTg.RunRecord',
		to_field='id',
		on_delete=models.CASCADE
	)
	user_id = models.ForeignKey(
		'user.User',
		to_field='id',
		on_delete=models.CASCADE
	)
