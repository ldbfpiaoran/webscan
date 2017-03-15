from django.shortcuts import render
import logging
from django.conf import settings
from scantool.tool.cmscan import *
import scantool.tool.rule
from scantool.tool.scanport import *

logger = logging.getLogger('scantool.views')

def webscan(request):
    try:
        url = request.POST.get('url')
        information = main(url)
    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'cmscan.html',locals( ))




def portscan(request):
    try:
        ip = request.POST.get('ip')
        data = request.POST.get('port')
        information = scanport(ip=ip,data=data)
        print(information)
    except Exception as e:
        print(e)
        logger.error(e)
    return render(request,'portscan.html',locals( ))