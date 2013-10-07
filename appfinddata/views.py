from appfinddata.forms import UrlInputForm, datainputform
from appfinddata.models import WebsiteData
from django.shortcuts import render_to_response,render
from django.template import RequestContext
from bs4 import BeautifulSoup
import urllib
import urllib2
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

def app_view1(request):
	template_name = 'UrlInputForm.html'
	form = UrlInputForm()
	if request.method == 'POST':
		form = UrlInputForm(data = request.POST)
		if form.is_valid():
			url = request.POST['urlname']
			url_data = urllib2.Request(url)
			filedatas = urllib2.urlopen(url_data)
			filedata = filedatas.read()
			soup = BeautifulSoup(filedata)
			title = soup.find('title').string
			try:
				meta_description = soup.find('meta', {'name':'description'})['content']
			except:
				meta_description = soup.findAll(attrs={'name':'description'})
			try:
				meta_keywords =soup.find('meta' ,{'name':'keywords'})['content']
			except:
				meta_keywords = soup.findAll(attrs={'name':'keywords'})
			seo_data = {'title':title,'meta_description':meta_description,'meta_keywords':meta_keywords}
			seo_form = datainputform(data=seo_data)
			return render_to_response('datainput.html',{'seo_form':seo_form}, context_instance= RequestContext(request))
	return render_to_response(template_name,{'form':form}, context_instance= RequestContext(request))



def app_view3(request, *args):
	messages.success( request, 'Test successful' )	
	if request.method == 'POST':
		form = datainputform(data = request.POST)
		if form.is_valid():
			form.save()
	return HttpResponseRedirect('/')



