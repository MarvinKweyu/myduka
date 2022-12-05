"""
This module seeds data across the project
"""

from django_seed import Seed

seeder = Seed.seeder("en_US")

# from ..models import Category, Product

from duka.models import Category, Product

seeder.entity(Category, 10)
seeder.entity(Product(Product, 20))
