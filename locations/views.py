from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.template import loader
from .models import TestQuestion, TestChoice

def index(request):
	latest_question_list = TestQuestion.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'locations/index.html', context)



# def index(request):
# 	latest_question_list = TestQuestion.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('locations/index.html')
# 	context = {
# 		'latest_question_list': latest_question_list,
# 	}
# 	return HttpResponse(template.render(context,request))
	

# Create your views here.
def detail(request, question_id):
	try:
		question = TestQuestion.objects.get(pk=question_id)
	except question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'locations/detail.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(TestQuestion, pk=question_id)
	return render(request, 'locations/results.html', {'question': question})



def vote(request, question_id):
	question = get_object_or_404(TestQuestion, pk=question_id)
	try:
		selected_choice = question.testchoice_set.get(pk=request.POST['choice'])
	except (KeyError, TestChoice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'locations/detail.html',{
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('locations:results', args=(question.id,)))

