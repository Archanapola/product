from django.db import models


# Create your models here.
SIZE=(
  ('10','10'),
  ('20','20'),
  ('30','30'),
  )

QUALITY=(('High','High'),('Low','Low'),('Medium','Medium'))

class productMainModel(models.Model):
 title=models.CharField(max_length=20)
 description=models.TextField()
 price=models.DecimalField(max_digits=10,decimal_places=2)
 unique_code=models.UUIDField(primary_key=True)
 size=models.IntegerField(choices=SIZE)
 quality=models.CharField(max_length=6, choices=QUALITY)
def __str__(self):
  return self.title
class Meta:
    db_tables="productMainModel"

COLOUR=(
   ('red','red'),
   ('blue','blue'),
   ('green','green'),
   ('black','black'),
   )
class productColourModel(models.Model):
 product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
 colour=models.CharField(max_length=6, choices=COLOUR)
def __str__(self):
  return self.colour
class productImageModel(models.Model):
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    image=models.ImageField()
def __str__(self):
  return self.image
