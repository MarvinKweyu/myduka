"""
This module seeds data across the project
"""

from django_seed import Seed


from duka import models

seeder = Seed.seeder("en_US")


def main():
    """Populate the DB"""
    seeder.entity(models.Category, 10)
    seeder.entity(models.Product, 20)


if __name__ == "__main__":
    main()
