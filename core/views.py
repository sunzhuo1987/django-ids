from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from core.models import IdsRecord

@login_required
def report(request):
    top_attacks = IdsRecord.objects.top_attacks()
    top_attacks_by_tag = IdsRecord.objects.top_attacks_tag()
    top_attacks_paths = IdsRecord.objects.top_attacks_paths()
    attacks_trends = IdsRecord.objects.attacks_trends()
    return render_to_response('ids/report/report.html', {'top_attacks': top_attacks,
                                                         'top_attacks_by_tag':top_attacks_by_tag,
                                                         'top_attacks_paths':top_attacks_paths,
                                                         'attacks_trends':attacks_trends})
