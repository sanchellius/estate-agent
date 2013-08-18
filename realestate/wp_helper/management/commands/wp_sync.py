# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from wp_helper.service import WPService
from settings import WP_PARAMS
from estatebase.models import Estate
from django.utils import translation

class Command(BaseCommand):
    def handle(self, *args, **options):
        translation.activate('ru')        
        wp_service = WPService(WP_PARAMS['site'])      
        estates = Estate.objects.filter(wp_meta__status=3)
        for estate in estates:            
            wp_service.sync_post(estate)                                 
                
        