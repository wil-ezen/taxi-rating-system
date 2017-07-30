from django.db import models


class Taxi(models.Model):
    def __str__(self):
        return self.number_plate

    number_plate = models.CharField(max_length=20)
    overall_rating = models.FloatField(default=0)  # make sure this satisfies 0<= rating <=5


class Rating(models.Model):
    # def __str__(self):
    #     return self.rating_id
    #
    # rating_id = models.CharField(max_length=20)
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    score = models.FloatField(default=-1)
    date = models.DateTimeField('date')
