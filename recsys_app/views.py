from django.shortcuts import render
from recsys_app.models import Case
import operator, math
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

def getRecommendations(lawtype):
    cases = Case.objects.filter(typeoflaw=lawtype)
    lawyer_scores = {}
    for case in cases:
        lawyer_scores[case.lawyer] = lawyer_scores.get(case.lawyer, 0) + math.log(case.rating)
    for key in lawyer_scores:
        lawyer_scores[key] = round(lawyer_scores[key], 1)
    sorted_scores = sorted(lawyer_scores.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_scores
        
def index(request):
    if request.method == "POST": #if user selects a law category
        selectedLawType = request.POST['lawvar']
        lwyers = getRecommendations(selectedLawType)
        #logger.error("lwers : {}".format(lwyers))
        recco_title = "Recommended Lawyers"
        recco_lawyers_colname1 = "Lawyer Name"
        recco_lawyers_colname2 = "Lawyer Score"
    else:
        lwyers = {}
        recco_title = ""
        recco_lawyers_colname1 = ""
        recco_lawyers_colname2 = ""
    
    law_types  = set([str(x.typeoflaw) for x in Case.objects.all()])
    kases = Case.objects.all()
    context = {'lawtypes': law_types, 'kases': kases , 
                'recco_title':recco_title , 'recco_lawyers_colname1': recco_lawyers_colname1, 
                'recco_lawyers_colname2':recco_lawyers_colname2, 'lwyers':lwyers}
    return render(request, 'index.html', context)
    
