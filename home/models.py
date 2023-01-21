from django.db import models
from wagtail.models import Page
from wagtail_resume.models import BaseResumePage


class ResumePage(BaseResumePage):
    pass


class HomePage(Page):
    pass
