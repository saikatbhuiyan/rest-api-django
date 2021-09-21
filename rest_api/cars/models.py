from django.db import models


class Cars(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)

    def __str__(self):
        return self.car_model


class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UpperModel(MyModel):
    """A proxy model is just another class that provides a different interface for the same underlying database model.
    That’s it. Really.
    A proxy model is a subclass of a database-table defining model. Typically creating a subclass of a model results in a
    new database table with a reference back to the original model’s table - multi-table inheritance.
    A proxy model doesn’t get its own database table. Instead it operates on the original table.
    """

    class Meta:
        proxy = True

    def __str__(self):
        return self.name.upper()
