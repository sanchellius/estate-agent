# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from models import EstateTypeCategory
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView, \
    DeleteView 
from estatebase.forms import ClientForm, ContactFormSet, \
    ClientFilterForm, ContactHistoryFormSet, ContactForm, \
    EstateCommunicationForm, \
    EstateParamForm, ApartmentForm, LevelForm, LevelFormSet, ImageUpdateForm, \
    SteadUpdateForm, EstateFilterForm, BidForm, from_to, BidFilterForm,\
    BidPicleForm, EstateRegisterForm, EstateRegisterFilterForm, EstateForm,\
    EstateCreateClientForm, EstateCreateForm
from estatebase.models import EstateType, Contact, Level, EstatePhoto, \
    prepare_history, Stead, Bid, EstateRegister, EstateClient, YES
from django.core.urlresolvers import reverse
from estatebase.models import Estate, Client
from django.utils import simplejson as json
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from estatebase.models import ExUser, Bidg
from estatebase.helpers.functions import safe_next_link
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from settings import CORRECT_DELTA
from estatebase.field_utils import check_value_list
from django.contrib.humanize.templatetags.humanize import intcomma


class BaseMixin(object):
    def get_success_url(self):   
        if '_save' in self.request.POST:     
            return self.request.REQUEST.get('next', '')
        return ''    

class DeleteMixin(object):
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.deleted = True
        self.object.save() 
        return HttpResponseRedirect(self.get_success_url())

class AjaxMixin(ModelFormMixin):
    def serializer_json(self, data):
        """Returns json format"""
        return json.dumps(data), 'application/json'    

    def no_ajax_response(self):
        return HttpResponse('Waiting for ajax reqiest!')

    def response_alternative(self, form, success=True):
        if success:        
            return HttpResponse(json.dumps({'result': 'success'}))
        else:
            return HttpResponse(json.dumps({'form': form.as_p().replace('\n', ''), 'result': 'error'}))

    def form_valid(self, form):        
        if not self.request.is_ajax():
            return super(AjaxMixin, self).form_valid(form)
        self.object = form.save();
        return self.response_alternative(form)

    def form_invalid(self, form):        
        if not self.request.is_ajax():
            return super(AjaxMixin, self).form_invalid(form)
        return self.response_alternative(form, False)

def upload_images(request):
    if request.method == 'POST':           
        for upfile in request.FILES.getlist('form_file'):
            estate_photo = EstatePhoto(estate_id=request.REQUEST.get('estate', None)) 
            file_content = ContentFile(upfile.read()) 
            estate_photo.image.save(upfile.name, file_content)
            estate_photo.save()  
            next_url = request.REQUEST.get('next', '')
            print next_url
    return HttpResponseRedirect(next_url)         


class SwapMixin(SingleObjectMixin, View):
    def get_context_data(self, **kwargs):
        context = super(SwapMixin, self).get_context_data(**kwargs)        
        context.update({        
            'next_url': safe_next_link(self.request.get_full_path()),
        })  
    def get(self, request, *args, **kwargs):        
        item = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])        
        try:
            if self.kwargs['direction'] == 'up':
                swap_item = self.get_queryset().filter(order__lt=item.order).order_by('-order')[0]
            else:
                swap_item = self.get_queryset().filter(order__gt=item.order).order_by('order')[0]    
        except IndexError:
            pass
        else:
            self.model.swap(item, swap_item)        
        return HttpResponseRedirect(request.REQUEST.get('next', ''))    

class SwapEstatePhotoView(SwapMixin):
    model = EstatePhoto
    def get_queryset(self):                        
        q = EstatePhoto.objects.filter(estate_id=self.kwargs['estate'])
        return q

class ImageUpdateView(BaseMixin, UpdateView):
    model = EstatePhoto
    template_name = 'image_update.html'
    form_class = ImageUpdateForm
    def get_context_data(self, **kwargs):
        context = super(ImageUpdateView, self).get_context_data(**kwargs)        
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
        })        
        return context    
    
class ImageDeleteView(DeleteView):
    model = EstatePhoto
    template_name = 'confirm.html'
    def get_context_data(self, **kwargs):
        context = super(ImageDeleteView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Удаление фото...',
            'dialig_body'  : u'Подтвердите удаление фотографии: %s' % self.object,
        })
        return context
    def get_success_url(self):   
        return self.request.REQUEST.get('next', '')                    

class EstateTypeView(TemplateView):    
    template_name = 'index.html'        
    def get_context_data(self, **kwargs):
        context = super(EstateTypeView, self).get_context_data(**kwargs)                
        estate_categories = EstateTypeCategory.objects.all()
        context.update({
            'title': 'base',
            'estate_categories': estate_categories,
            'next_url': safe_next_link(self.request.get_full_path()),
        })        
        return context 

class EstateTypeViewAjax(TemplateView):
    template_name = 'ajax/estate_type_select.html'
    def get_context_data(self, **kwargs):                
        context = super(EstateTypeViewAjax, self).get_context_data(**kwargs)   
        estate_categories = EstateType.objects.filter(estate_type_category__independent = True).order_by('estate_type_category','order')
        context.update({            
            'estate_categories': estate_categories,                                             
        })        
        return context

class PlaceableTypeViewAjax(TemplateView):
    template_name = 'ajax/placeable_select.html'
    def get_context_data(self, **kwargs):
        filter_dict = {}
        category = self.request.GET.get('category', None)
        if category == 'commerce':
            filter_dict.update({
            'estate_type_category__is_commerce' : True
            })
        elif category == 'independent':
            filter_dict.update({
            'estate_type_category__independent' : False
            })             
        estate_categories = EstateType.objects.filter(**filter_dict).select_related().order_by('estate_type_category','order')
        context = super(PlaceableTypeViewAjax, self).get_context_data(**kwargs)
        context.update({            
            'estate_categories': estate_categories,
            'estate': self.kwargs['estate'],                                   
        })        
        return context

class EstateMixin(BaseMixin, ModelFormMixin):
    model = Estate
    def form_valid(self, form):
        self.object = form.save(commit=False)         
        self.object.history = prepare_history(self.object.history, self.request.user.pk)        
        return super(EstateMixin, self).form_valid(form)

class EstateCreateView(EstateMixin, CreateView):
    template_name = 'estate_create.html'       
    form_class = EstateCreateForm    
    def get_initial(self):        
        initial = super(EstateCreateView, self).get_initial()
        if 'estate_type' in self.kwargs:                  
            initial['estate_type'] = self.kwargs['estate_type']        
        initial['estate_status'] = 2
        initial['broker'] = self.request.user            
        return initial
    def get_context_data(self, **kwargs):
        context = super(EstateCreateView, self).get_context_data(**kwargs)        
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
        })        
        return context
    def get_success_url(self):   
        next_url = self.request.REQUEST.get('next', '')                                  
        return '%s?%s' % (self.object.detail_link, safe_next_link(next_url))
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        category = form.cleaned_data['estate_type'].estate_type_category
        self.object.estate_category_id = category.pk 
        self.object._estate_type_id = form.cleaned_data['estate_type'].pk
        if category.is_commerce:
            self.object.com_status_id = YES         
        self.object.history = prepare_history(self.object.history, self.request.user.pk)       
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
class EstateCreateClientView(EstateCreateView):
    template_name = 'estate_create.html'       
    form_class = EstateCreateClientForm    
    def get_initial(self):        
        initial = super(EstateCreateClientView, self).get_initial()      
        initial['client_pk'] = self.kwargs['client']        
        initial['client_status'] = EstateClient.ESTATE_CLIENT_STATUS    
        return initial    
    def form_valid(self, form):
        super(EstateCreateClientView, self).form_valid(form) 
        client_pk = form.cleaned_data.get('client_pk') or EstateClient.ESTATE_CLIENT_STATUS
        estate_client_status = form.cleaned_data.get('client_status') or None
        if client_pk:
            EstateClient.objects.create(client_id=client_pk,
                                        estate_client_status=estate_client_status,
                                        estate=self.object)
        return HttpResponseRedirect(self.get_success_url())    
            
class EstateDetailView(DetailView):
    template_name = 'estate_detail.html'    
    def get_queryset(self):                        
        q = Estate.objects.all().select_related()
        return q
    def get_context_data(self, **kwargs):        
        context = super(EstateDetailView, self).get_context_data(**kwargs)
        r = (self.object.agency_price or 0) - (self.object.saler_price or 0)        
        p = float(r) / (self.object.saler_price or 1) * 100              
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
            'margin': '%d (%d%%)' % (r, p),
            'images': self.object.images.all()[:6],                       
        })        
        return context
    
class EstateUpdateView(EstateMixin, UpdateView):
    model = Estate
    template_name = 'estate_create.html'
    form_class = EstateForm
    def get_context_data(self, **kwargs):
        context = super(EstateUpdateView, self).get_context_data(**kwargs)        
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
            'estate_type': self.object.estate_type,
        })        
        return context       

class EstateDeleteView(DeleteMixin, EstateMixin, DeleteView):
    template_name = 'confirm.html'
    def get_context_data(self, **kwargs):
        context = super(EstateDeleteView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Удаление объекта...',
            'dialig_body'  : u'Подтвердите удаление объекта: %s' % self.object,
        })
        return context
    def get_success_url(self):   
        return self.request.REQUEST.get('next', '')

class EstateCommunicationUpdateView(EstateUpdateView):
    template_name = 'estate_comm.html'
    form_class = EstateCommunicationForm

class EstateParamUpdateView(EstateUpdateView):    
    template_name = 'estate_params.html'
    form_class = EstateParamForm

def set_estate_filter(q, filter_dict, force_valid=False, user=None):
    if 'Q' in filter_dict:
        q = q.filter(filter_dict.pop('Q'))
    if force_valid:
        filter_dict.update({
           'valid__exact' : True,
           'history__modificated__gt' : CORRECT_DELTA
        })
    if user:
        filter_dict.update({'region__geo_group__userprofile__user__exact': user })  
    if len(filter_dict):
        q = q.filter(**filter_dict)
    return q

class EstateListView(ListView):    
    template_name = 'estate_list.html'
    paginate_by = 25   
    def get_queryset(self):
        #q = Estate.objects.select_related('region','locality','microdistrict','street','estate_type','history','estate_status','contact__contact_state','contact__contact_type','contact__client__client_type')
        q = Estate.objects.select_related().prefetch_related('bidgs__estate_type__estate_type_category','history')        
        search_form = EstateFilterForm(self.request.GET)
        filter_dict = search_form.get_filter()        
        q = set_estate_filter(q, filter_dict, user=self.request.user)
        order_by = self.request.fields 
        if order_by:      
            return q.order_by(','.join(order_by))    
        return q
    def get_context_data(self, **kwargs):
        context = super(EstateListView, self).get_context_data(**kwargs)
        estate_filter_form = EstateFilterForm(self.request.GET)                                                                    
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
            'total_count': Estate.objects.count(),
            'filter_count' : self.get_queryset().count(),
            'fields': list(estate_filter_form),                                   
        })        
        return context

class EstateSelectListView(EstateListView):
    template_name = 'estate_select_list.html'
    def get_queryset(self):                  
        q = super(EstateSelectListView, self).get_queryset()
        selected = get_object_or_404(EstateRegister, pk=self.kwargs['selected'])
        q = q.exclude(id__in = selected.estates.all().values_list('id', flat=True))        
        return q
    def get_context_data(self, **kwargs):
        context = super(EstateSelectListView, self).get_context_data(**kwargs)
        context.update({            
            'selected': self.kwargs['selected'],                                               
        })
        return context
        
class EstateListDetailsView(EstateListView):   
    paginate_by = 10 
    template_name = 'estate_short_list.html'        
    def get_queryset(self):
        q = super(EstateListDetailsView, self).get_queryset()
        self.estate = None 
        if 'pk' in self.kwargs:                     
            self.estate = get_object_or_404(Estate, pk=self.kwargs['pk'])
        else:              
            r = list(q[:1])
            if r:
                self.estate = r[0]        
        return q
    def get_context_data(self, **kwargs):        
        context = super(EstateListDetailsView, self).get_context_data(**kwargs)
        r = p = 0
        if self.estate:      
            r = (self.estate.agency_price or 0) - (self.estate.saler_price or 0)        
            p = float(r) / (self.estate.saler_price or 1) * 100                                           
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
            'margin': '%s (%s%%)' % (intcomma(r), intcomma(p)),
            'images': self.estate and self.estate.images.all()[:6] or None,
            'estate': self.estate,                                                      
        })                
        return context        

class EstateImagesView(TemplateView): 
    template_name = 'estate_images.html'
    def get_context_data(self, **kwargs):
        context = super(EstateImagesView, self).get_context_data(**kwargs)        
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
            'estate': Estate.objects.get(pk=kwargs['estate'])            
        })        
        return context      

class ClientUpdateEstateView(DetailView):   
    model = Client
    template_name = 'confirm.html'
    def get_context_data(self, **kwargs):
        context = super(ClientUpdateEstateView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Привязка...',
            'dialig_body'  : u'Привязать заказчика %s к объекту [%s]?' % (self.object, self.kwargs['estate_pk']),
        })
        return context
    def update_object(self,client_pk,estate_pk):
        '''
        Вынесена для переопределения в потомках класса
        '''        
        EstateClient.objects.create(client_id=client_pk,estate_id=estate_pk,
                                    estate_client_status_id=EstateClient.ESTATE_CLIENT_STATUS)                
    def post(self, request, *args, **kwargs):       
        self.update_object(self.kwargs['pk'],self.kwargs['estate_pk'])       
        #Обновление истории и контакта у оъекта                            
        prepare_history(Estate.objects.get(pk=self.kwargs['estate_pk']).history, self.request.user.pk)      
        return HttpResponseRedirect(self.request.REQUEST.get('next', ''))    

class ClientRemoveEstateView(ClientUpdateEstateView):    
    def get_context_data(self, **kwargs):
        context = super(ClientRemoveEstateView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Отвязка...',
            'dialig_body'  : u'Отвязать заказчика %s от объекта [%s]?' % (self.object, self.kwargs['estate_pk']),
        })
        return context 
    def update_object(self,client_pk,estate_pk):
        EstateClient.objects.get(estate_id=estate_pk,client_id=client_pk).delete()                   
        
class ObjectMixin(ModelFormMixin):    
    model = Bidg    
    continue_url = None    
    def form_valid(self, form):
        prepare_history(self.get_estate().history, self.request.user.pk)       
        return super(ObjectMixin, self).form_valid(form)    
    def get_success_url(self):   
        next_url = self.request.REQUEST.get('next', '')         
        if '_continue' in self.request.POST:                  
            return '%s?%s' % (reverse(self.continue_url, args=[self.object.id]), safe_next_link(next_url)) 
        return next_url
    def get_estate(self):
        return self.object and self.object.estate or Estate.objects.get(pk=self.kwargs['estate'])            
    def get_context_data(self, **kwargs):
        context = super(ObjectMixin, self).get_context_data(**kwargs)        
        context.update({            
            'estate': self.get_estate(),
        })        
        return context

class ApartmentCreateView(ObjectMixin, CreateView):
    template_name = 'bidg_form.html'        
    form_class = ApartmentForm   
    continue_url = 'apartment_update'
    def get_initial(self):        
        initial = super(ApartmentCreateView, self).get_initial()                
        initial['estate'] = self.kwargs['estate']
        return initial

class ApartmentUpdateView(ObjectMixin, UpdateView):
    template_name = 'bidg_form.html'        
    form_class = ApartmentForm   
    continue_url = 'apartment_update'        

class ClientListView(ListView):
    template_name = 'client_list.html'
    context_object_name = "clients"
    paginate_by = 5    
    def get_queryset(self):                        
        q = Client.objects.select_related().prefetch_related('origin','contacts__contact_state','contacts__contact_type')
        search_form = ClientFilterForm(self.request.GET)
        filter_dict = search_form.get_filter()
        if len(filter_dict):
            q = q.filter(**filter_dict)        
        order_by = self.request.fields 
        if order_by:      
            return q.order_by(','.join(order_by))
        return q    
    def get_context_data(self, **kwargs):        
        try:
            context = super(ClientListView, self).get_context_data(**kwargs)
        except Http404:
            self.kwargs['page'] = 'last'
            context = super(ClientListView, self).get_context_data(**kwargs)                  
        context.update ({        
            'title': 'list',
            'next_url': safe_next_link(self.request.get_full_path()),
            'client_filter_form' : ClientFilterForm(self.request.GET),
        })        
        return context

class ClientSelectView(ClientListView):
    template_name = 'client_select.html'
    def get_estate(self):
        estate = Estate.objects.get(pk=self.kwargs['estate_pk'])
        return estate            
    def get_context_data(self, **kwargs):         
        context = super(ClientSelectView, self).get_context_data(**kwargs)                    
        context.update ({            
            'estate' : self.get_estate(),
            'client_filter_form' : ClientFilterForm(self.request.GET),
        })        
        return context
    def get_queryset(self):
        q = super(ClientSelectView, self).get_queryset()
        q = q.exclude(estates__id=self.kwargs['estate_pk'])
        return q   

class ClientMixin(ModelFormMixin):
    template_name = 'client_form.html'
    model = Client
    form_class = ClientForm          
    def form_valid(self, form):
        context = self.get_context_data()
        contact_form = context['contact_formset']
        if contact_form.is_valid():
            self.object = form.save(commit=False)             
            self.object.history = prepare_history(self.object.history, self.request.user.pk)
            self.object.save()            
            if contact_form.has_changed():
                contact_form.instance = self.object
                contacts = contact_form.save(commit=False)
                for contact in contacts:
                    contact.user_id = self.request.user.pk
                    contact.save()                                       
            return super(ModelFormMixin, self).form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
    def get_success_url(self):   
        next_url = self.request.REQUEST.get('next', '')         
        if '_continue' in self.request.POST:                  
            return '%s?%s' % (reverse('client_update', args=[self.object.id]), safe_next_link(next_url)) 
        return next_url
    def get_context_data(self, **kwargs):
        context = super(ClientMixin, self).get_context_data(**kwargs)                
        if self.request.POST:
            context['contact_formset'] = ContactFormSet(self.request.POST, instance=self.object)            
        else:
            context['contact_formset'] = ContactFormSet(instance=self.object)
        return context                        

class ClientCreateView(ClientMixin, CreateView):
    def get_context_data(self, **kwargs):
        context = super(ClientCreateView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Добавление нового заказчика'
        })        
        return context    
    def get_initial(self):        
        initial = super(ClientCreateView, self).get_initial()
        initial['broker'] = self.request.user.pk        
        return initial
      
class ClientUpdateView(ClientMixin, UpdateView):
    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Редактирование заказчика «%s»' % self.object 
        })        
        return context

class ClientDeleteView(DeleteMixin, ClientMixin, DeleteView):
    template_name = 'confirm.html'
    def get_context_data(self, **kwargs):
        context = super(ClientDeleteView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Удаление заказчика...',
            'dialig_body'  : u'Подтвердите удаление заказчика: %s' % self.object,
        })
        return context     
    
class ContactMixin(BaseMixin):
    model = Contact       
    
class ContactHistoryListView(ContactMixin, DetailView):
    '''  
    Пока не используется    
    '''    
    template_name = 'contact_history_list.html'        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        formset = ContactHistoryFormSet(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()                        
            return HttpResponseRedirect(self.get_success_url())                
        else:
            return self.render_to_response(self.get_context_data())
        
    def get_context_data(self, **kwargs): 
        context = super(ContactHistoryListView, self).get_context_data(**kwargs)        
        if self.request.POST:
            context['history_formset'] = ContactHistoryFormSet(self.request.POST, instance=self.object)            
        else:
            context['history_formset'] = ContactHistoryFormSet(instance=self.object)                
        context.update ({        
            'title': 'История контакта %s' % self.object,
            'next_url': safe_next_link(self.request.get_full_path()),
        })        
        return context
      
class ContactUpdateView(ContactMixin, UpdateView):    
    template_name = 'contact_update.html' 
    form_class = ContactForm
    def get_context_data(self, **kwargs): 
        context = super(ContactUpdateView, self).get_context_data(**kwargs)                        
        context.update ({        
            'title': 'Редактирование контакта %s' % self.object,
            'next_url': safe_next_link(self.request.get_full_path()),
        })        
        return context
    def form_valid(self, form):            
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.pk              
        prepare_history(self.object.client.history, self.request.user.pk)  
        return super(ContactUpdateView, self).form_valid(form)               
        
    
class LevelMixin(ModelFormMixin):
    template_name = 'layout_update.html'
    form_class = LevelForm
    model = Level
    def get_context_data(self, **kwargs):
        if 'bidg' in self.kwargs:
            bidg = Bidg.objects.get(pk=self.kwargs['bidg'])
        else:
            bidg = self.object.bidg                
        context = super(LevelMixin, self).get_context_data(**kwargs)
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
            'bidg': bidg,
        })                        
        if self.request.POST:
            context['layout_formset'] = LevelFormSet(self.request.POST, instance=self.object)            
        else:
            context['layout_formset'] = LevelFormSet(instance=self.object)
        return context  
    def get_success_url(self):   
        next_url = self.request.REQUEST.get('next', '')         
        if '_continue' in self.request.POST:                  
            return '%s?%s' % (reverse('level_update', args=[self.object.id]), safe_next_link(next_url)) 
        return next_url
    def form_valid(self, form):
        context = self.get_context_data()
        layout_form = context['layout_formset']
        if layout_form.is_valid():
            self.object = form.save(commit=False)                         
            self.object.save()             
            layout_form.instance = self.object            
            layout_form.save()
            #Обновление истории объекта                                 
            prepare_history(self.object.bidg.estate.history, ExUser.objects.get(pk=self.request.user.pk))
            return super(ModelFormMixin, self).form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class LevelCreateView(LevelMixin, CreateView):
    def get_initial(self):        
        initial = super(LevelCreateView, self).get_initial()                
        initial['bidg'] = self.kwargs['bidg']
        return initial

class LevelUpdateView(LevelMixin, UpdateView):
    pass
    
class LevelDeleteView(LevelMixin, DeleteView):
    template_name = 'confirm.html'
    def get_context_data(self, **kwargs):
        context = super(LevelDeleteView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Удаление уровня планировки...',
            'dialig_body'  : u'Подтвердите удаление уровня: %s' % self.object,
        })
        return context    

class SteadUpdateView(ObjectMixin, UpdateView):
    model = Stead
    template_name = 'stead_form.html'        
    form_class = SteadUpdateForm   
    continue_url = 'stead_update'

class BidgAppendView(TemplateView):    
    template_name = 'confirm.html'
    dialig_title = u'Добавление строения...'
    dialig_body = u'Добавить строение на участок?'    
    def get_context_data(self, **kwargs):        
        context = super(BidgAppendView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : self.dialig_title,
            'dialig_body'  : self.dialig_body,
        })
        return context
    def update_object(self):
        '''
        Вынесена для переопределения в потомках класса
        '''        
        bidg = Bidg(estate_id=self.kwargs['estate'], estate_type_id=self.kwargs['estate_type'])
        bidg.save()
        self.estate = bidg.estate     
    def post(self, request, *args, **kwargs):        
        self.update_object()
        user = ExUser.objects.get(pk=self.request.user.pk)        
        #Обновление истории объекта        
        prepare_history(self.estate.history, user)
        return HttpResponseRedirect(self.request.REQUEST.get('next', ''))      
    
class BidgRemoveView(BidgAppendView):
    dialig_title = u'Удаление строения...'
    dialig_body = u'Удалить строение из лота?'
    def update_object(self):                        
        bidg = Bidg.objects.get(pk=self.kwargs['pk'])
        self.estate = bidg.estate
        bidg.delete();        

class SteadAppendView(BidgAppendView):
    dialig_title = u'Добавление участка...'
    dialig_body = u'Добавить участок к лоту?'
    def update_object(self):   
        stead = Stead(estate_id=self.kwargs['estate'])
        stead.save()
        self.estate = stead.estate

class SteadRemoveView(BidgAppendView):
    dialig_title = u'Удаление участка...'
    dialig_body = u'Удалить участок из лота?'
    def update_object(self):   
        stead = Stead.objects.get(pk=self.kwargs['pk'])
        self.estate = stead.estate
        stead.delete();

class BidMixin(ModelFormMixin):
    template_name = 'bid_update.html'
    form_class = BidForm
    model = Bid
    def get_initial(self):        
        initial = super(BidMixin, self).get_initial()                
        initial['broker'] = self.request.user.pk
        return initial
    def get_context_data(self, **kwargs):
        client = None
        if 'client' in self.kwargs:
            client = Client.objects.get(pk=self.kwargs['client'])
        elif self.object:
            client = self.object.client                 
        context = super(BidMixin, self).get_context_data(**kwargs)
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
            'client': client,            
        })       
                           
        if self.request.POST:
            context['estate_filter_form'] = BidPicleForm(self.request.POST)            
        else:
            data = None
            if self.object:
                data = self.object.estate_filter                   
            context['estate_filter_form'] = BidPicleForm(data)                      
        return context  
    def get_success_url(self):   
        next_url = self.request.REQUEST.get('next', '')         
        if '_continue' in self.request.POST:                  
            return '%s?%s' % (reverse('bid_update', args=[self.object.id]), safe_next_link(next_url)) 
        return next_url
    def form_valid(self, form):
        context = self.get_context_data()
        estate_filter_form = context['estate_filter_form']
        if estate_filter_form.is_valid():
            self.object = form.save()                      
            # Запаковываем фильтр в поле
            self.object.estate_filter = estate_filter_form.data.copy()                        
            self.object.history = prepare_history(self.object.history, self.request.user.pk)
            self.object.estates = estate_filter_form['estates'].value()
            self.object.clients = estate_filter_form['clients'].value()
            self.object.contacts = estate_filter_form['contacts'].value()
            self.object.estate_types = estate_filter_form['estate_type'].value()
            self.object.regions = estate_filter_form['region'].value()            
            self.object.localities = estate_filter_form['locality'].value()
            if check_value_list(estate_filter_form['agency_price'].value()):                
                values = estate_filter_form['agency_price'].field.clean(estate_filter_form['agency_price'].value())                                  
                self.object.agency_price_min = values[0]                        
                self.object.agency_price_max = values[1]
            self.object.save()            
            return super(ModelFormMixin, self).form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))    

class BidCreateView(BidMixin, CreateView):
    def get_initial(self):        
        initial = super(BidCreateView, self).get_initial()
        if 'client' in self.kwargs:
            client_pk = self.kwargs['client']
            if not Client.objects.filter(pk=client_pk).exists():
                raise Exception(u'Заказчик с id %s не найден!' % client_pk)                
            initial['client'] = client_pk
        return initial

class BidUpdateView(BidMixin, UpdateView):    
    pass

class BidDeleteView(DeleteMixin, BidMixin, DeleteView):
    template_name = 'confirm.html'
    def get_context_data(self, **kwargs):
        context = super(BidDeleteView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Удаление заявки...',
            'dialig_body'  : u'Подтвердите удаление заявки: %s' % self.object,
        })
        return context    

class BidDetailView(BidMixin, DetailView):
    template_name = 'bid_detail.html'
    def get_context_data(self, **kwargs):
        context = super(BidDetailView, self).get_context_data(**kwargs)
#        form = BidPicleForm(self.object.estate_filter)
#        if form.is_valid():         
#            context.update({
#                'picle_form' : form.cleaned_data            
#            })
        q = self.object.estate_registers.all()
        order_by = self.request.fields
        if order_by:      
            q = q.order_by(','.join(order_by))
        context.update({
                'register_list' : q             
                })

        return context 

class BidListView(ListView):    
    template_name = 'bid_list.html'
    paginate_by = 20   
    def get_queryset(self):        
        q = Bid.objects.select_related().all()        
        search_form = BidFilterForm(self.request.GET)
        filter_dict = search_form.get_filter()
#        Если нужно и заявки только по гео-фактору показывать
#        filter_dict.update({'localities__geo_group__userprofile__user__exact': self.request.user })                                        
        if len(filter_dict):
            q = q.filter(**filter_dict)
        return q
    def get_context_data(self, **kwargs):
        context = super(BidListView, self).get_context_data(**kwargs)
        bid_filter_form = BidFilterForm(self.request.GET)                                                                    
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
            'bid_count': Bid.objects.count(),           
            'bid_filter_form': bid_filter_form,                                   
        })        
        return context    

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'
    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)                
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
        })        
        return context       
    
class EstateRegisterMixin(ModelFormMixin):
    template_name = 'register_update.html'
    form_class = EstateRegisterForm 
    model = EstateRegister   
    def get_initial(self):        
        initial = super(EstateRegisterMixin, self).get_initial()                
        initial['broker'] = self.request.user.pk
        if 'bid' in self.kwargs:                  
            initial['bids'] = [self.kwargs['bid']]
        return initial
    def get_context_data(self, **kwargs):                         
        context = super(EstateRegisterMixin, self).get_context_data(**kwargs)
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),            
        })
        return context
    def get_success_url(self):   
        next_url = self.request.REQUEST.get('next', '')         
        if '_continue' in self.request.POST:                  
            return '%s?%s' % (reverse('register_update', args=[self.object.id]), safe_next_link(next_url)) 
        return next_url
    def form_valid(self, form):
        self.object = form.save(commit=False)        
        self.object.history = prepare_history(self.object.history, self.request.user.pk)        
        return super(EstateRegisterMixin, self).form_valid(form)

class EstateRegisterCreateView(EstateRegisterMixin, CreateView):
    def get_initial(self):        
        initial = super(EstateRegisterCreateView, self).get_initial()
        rtype = self.request.REQUEST.get('type', None)
        if rtype == 'empty':
            initial['name'] = u'Ручная'
        elif rtype == 'based':
            initial['name'] = u'По заявке [%s]' % self.kwargs['bid']
            bid = Bid.objects.get(pk=self.kwargs['bid'])
            fltr = bid.estate_filter
            if fltr:            
                pickle_form = BidPicleForm(fltr)
                f = pickle_form.get_filter()
                q = Estate.objects.all()                 
                q = set_estate_filter(q, f, True)                
                initial['estates'] = q.values_list('id', flat=True)                                
        return initial     

class EstateRegisterUpdateView(EstateRegisterMixin, UpdateView):
    pass

class EstateRegisterDeleteView(DeleteMixin, EstateRegisterMixin, DeleteView):
    template_name = 'confirm.html'
    def get_context_data(self, **kwargs):
        context = super(EstateRegisterDeleteView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Удаление подборки...',
            'dialig_body'  : u'Подтвердите удаление подборки: %s' % self.object,
        })
        return context
    
class EstateRegisterDetailView(EstateRegisterMixin, DetailView):
    template_name = 'register_detail.html'
    def get_context_data(self, **kwargs):
        context = super(EstateRegisterDetailView, self).get_context_data(**kwargs)        
        estate_list = self.object.estates.all()  
        order_by = self.request.fields
        if order_by:      
            estate_list = estate_list.order_by(','.join(order_by))        
        paginator = Paginator(estate_list, 25)    
        page = self.request.GET.get('page')
        try:
            estates = paginator.page(page)
        except PageNotAnInteger:        
            estates = paginator.page(1)
        except EmptyPage:        
            estates = paginator.page(paginator.num_pages)        
        context.update({
                'paginator': paginator,
                'page_obj': estates,
                'is_paginated': estates.has_other_pages(),
                'object_list': estates.object_list
            })  
        return context  

class AddEstateToRegisterView(DetailView):   
    model = EstateRegister
    template_name = 'confirm.html'
    def get_context_data(self, **kwargs):
        context = super(AddEstateToRegisterView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Привязка...',
            'dialig_body'  : u'Привязать объект %s к подборке [%s]?' % (self.kwargs['estate_pk'], self.object),
        })
        return context
    def action(self, register, estate_pk):                
        register.estates.add(estate_pk)        
    def post(self, request, *args, **kwargs):
        register = self.model.objects.get(pk=self.kwargs['pk'])         
        self.action(register, self.kwargs['estate_pk'])              
        return HttpResponseRedirect(self.request.REQUEST.get('next', ''))

class RemoveEstateFromRegisterView(AddEstateToRegisterView):
    def get_context_data(self, **kwargs):
        context = super(RemoveEstateFromRegisterView, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Отвязка...',
            'dialig_body'  : u'Отвязать объект %s от подборки [%s]?' % (self.kwargs['estate_pk'], self.object),
        })
        return context
    def action(self, register, estate_pk):                
        register.estates.remove(estate_pk)
        
class  EstateRegisterListView(ListView):
    context_object_name = 'register_list'
    template_name = 'register_list.html'    
    paginate_by = 5   
    def get_queryset(self):        
        q = EstateRegister.objects.select_related()       
        search_form = EstateRegisterFilterForm(self.request.GET)
        filter_dict = search_form.get_filter()                                        
        if len(filter_dict):
            q = q.filter(**filter_dict)
        order_by = self.request.fields
        if order_by:      
            q = q.order_by(','.join(order_by))    
        return q
    def get_context_data(self, **kwargs):
        context = super(EstateRegisterListView, self).get_context_data(**kwargs)
        register_filter_form = EstateRegisterFilterForm(self.request.GET)                                                                    
        context.update({            
            'next_url': safe_next_link(self.request.get_full_path()),
            'bid_count': Bid.objects.count(),           
            'register_filter_form': register_filter_form,                                   
        })        
        return context

class EstateRegisterSelectView(EstateRegisterListView):
    template_name = 'register_select.html'                
    def get_context_data(self, **kwargs):         
        context = super(EstateRegisterSelectView, self).get_context_data(**kwargs)                    
        context.update ({            
            'bid_pk' : self.kwargs['bid_pk'],            
        })        
        return context
    def get_queryset(self):
        q = super(EstateRegisterSelectView, self).get_queryset()
        q = q.exclude(bids__id=self.kwargs['bid_pk'])
        return q

class AddRegisterToBid(DetailView):   
    model = EstateRegister
    template_name = 'confirm.html'
    def get_context_data(self, **kwargs):
        context = super(AddRegisterToBid, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Привязка...',
            'dialig_body'  : u'Привязать подборку %s к заявке [%s]?' % (self.kwargs['bid_pk'], self.object),
        })
        return context
    def action(self, register, bid_pk):                
        register.bids.add(bid_pk)        
    def post(self, request, *args, **kwargs):
        register = self.model.objects.get(pk=self.kwargs['pk'])         
        self.action(register, self.kwargs['bid_pk'])              
        return HttpResponseRedirect(self.request.REQUEST.get('next', ''))

class RemoveRegisterFromBid(AddRegisterToBid):   
    def get_context_data(self, **kwargs):
        context = super(RemoveRegisterFromBid, self).get_context_data(**kwargs)
        context.update({
            'dialig_title' : u'Отвязка...',
            'dialig_body'  : u'Отвязать подборку %s от заявки [%s]?' % (self.kwargs['bid_pk'], self.object),
        })
        return context
    def action(self, register, bid_pk):                
        register.bids.remove(bid_pk) 

class RegisterReportView(EstateRegisterMixin, DetailView):
    def get_context_data(self, **kwargs):
        context = super(RegisterReportView, self).get_context_data(**kwargs)        
        estate_list = self.object.estates.prefetch_related('beside', 'estate_category' , 'contact' , 'bidgs__wall_construcion', 'history', 
                                                           'clients__contacts','bidgs__estate_type__estate_type_category', 
                                                           'stead__estate_type__estate_type_category',
                                                           'bidgs__documents','bidgs__levels__layout_set',
                                                           'bidgs__exterior_finish','bidgs__roof','bidgs__window_type','bidgs__heating',
                                                           'bidgs__levels__level_name','bidgs__levels__layout_set__furniture',
                                                           'bidgs__levels__layout_set__interior','bidgs__levels__layout_set__layout_feature',
                                                           'bidgs__levels__layout_set__layout_type', 'estate_status', 'origin',
                                                           'region','locality')
        
        order_by = self.request.fields
        if order_by:      
            estate_list = estate_list.order_by(','.join(order_by))       
        context.update({
                'estate_list': estate_list
            })  
        return context