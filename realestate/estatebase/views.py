from django.views.generic import TemplateView
from models import EstateTypeCategory

class EstateTypeView(TemplateView):    
    template_name = 'base.html'    
    def get_context_data(self, **kwargs):
        context = super(EstateTypeView, self).get_context_data(**kwargs)
        estate_categories = EstateTypeCategory.objects.all()        
        context.update({
            'title': 'base',
            'estate_categories': estate_categories
        })
        return context    