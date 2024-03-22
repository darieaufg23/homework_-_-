from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=300)

    def __str__(self) -> str:
        return f"<Product>:{str(self.name)[:40]}"
    
    def items(self):
        return {"name":self.name}.items()