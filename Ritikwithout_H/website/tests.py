from django.test import TestCase
from . models import Skill

class SkillTestCase(TestCase):
    def setUp(self):
        Skill.objects.create(skill_name = "Guitar", skill_image="image.jpg")
        Skill.objects.create(skill_name = "Drum", skill_image="image1.jpg")

    
 

    

# Create your tests here.
