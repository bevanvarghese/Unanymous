from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .models import Question, Choice

# Get and display questions
def index(request):
    latest_question_list = Question.objects.order_by('-published_on')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# Get and display results of question
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Display the voting form again
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return a HttpResponseRedirect after dealing with POST requests
        # to prevent data from being posted twice in the case of 'Back' pressed
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# Data of a single question - API endpoint for graphing
def resultsData(request, obj):
    voteData = []
    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()
    for i in votes:
        voteData.append({i.choice_text: i.votes})
    return JsonResponse(voteData, safe=False)
