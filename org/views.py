from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm,SubscriberForm,TeamForm, EventForm, TestimonialForm, PaymentForm
from . import Checksum
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    contact_form = ContactForm()
    subscriber_form = SubscriberForm()
    context = {'ContactForm': contact_form, 'SubscriberForm': subscriber_form }
    return render(request, 'home.html', context)

def contactFormView(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        contact_form = ContactForm(request.POST)
        # check whether it's valid:
        if contact_form.is_valid():
            # process the data in form.cleaned_data as required
            new_contact = contact_form.save()
            new_contact.save()
            # redirect to a new URL:
            return HttpResponseRedirect('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponseRedirect('home')

def subscriberFormView(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        subscriber_form = SubscriberForm(request.POST)
        # check whether it's valid:
        if subscriber_form.is_valid():
            # process the data in form.cleaned_data as required
            new_subscriber = subscriber_form.save()
            new_subscriber.save()
            # redirect to a new URL:
            return HttpResponseRedirect('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponseRedirect('home')

def thankYouView(request):
    subscriber_form = SubscriberForm()
    context = {'SubscriberForm': subscriber_form }
    return render(request, 'thanks.html', context)

def teamFormView(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('home')
    else:
        form = TeamForm()
    return render(request, 'upload.html', {
        'form': form
    })

def eventFormView(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('home')
    else:
        form = EventForm()
    return render(request, 'upload.html', {
        'form': form
    })

def testimonialFormView(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('home')
    else:
        form = TestimonialForm()
    return render(request, 'upload.html', {
        'form': form
    })

def paytm(request):
    form = PaymentForm()
    return render(request, 'html.html', {"form":form})


def payment(request):

    if request.method == 'POST':
        order_id = "12345"
        bill_amount = request.POST['amount']
        print(bill_amount)
        data_dict = {
            'MID': settings.PAYTM_MERCHANT_ID,
            'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
            'WEBSITE': settings.PAYTM_WEBSITE,
            'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
            'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
            'CUST_ID': '123123',
            'ORDER_ID':order_id,
            'TXN_AMOUNT': bill_amount,
        } # This data should ideally come from database
        data_dict['CHECKSUMHASH'] = Checksum.generateSignature(data_dict, settings.PAYTM_MERCHANT_KEY)
        context = {
            'payment_url': settings.PAYTM_PAYMENT_GATEWAY_URL,
            'comany_name': settings.PAYTM_COMPANY_NAME,
            'data_dict': data_dict
        }
        return render(request, 'payment.html', context)
    return HttpResponseRedirect('home')


@csrf_exempt
def response(request):
    resp = {}

    if resp['verified']:
        # save success details to db; details in resp['paytm']
        return HttpResponse("<center><h1>Transaction Successful</h1><center>", status=200)
    else:
        # check what happened; details in resp['paytm']
        return HttpResponse("<center><h1>Transaction Failed</h1><center>", status=400)
