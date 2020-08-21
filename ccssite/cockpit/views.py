from django.shortcuts import render
from django.http import HttpResponse
from .models import Production
import openpyxl, xlrd, datetime
# Create your views here.
def to_date(serial):
    seconds = (float(serial) - 25569) * 86400.0
    return datetime.datetime.utcfromtimestamp(seconds)

def index(request):
    data = Production.objects.all()
    data.delete()
    workbook = xlrd.open_workbook("gitpw32.xlsx")
    sheet = workbook.sheet_by_index(0)
    i = 0
    for rowx in range(sheet.nrows):
        value = sheet.row_values(rowx)
        #print(value)
        if(i > 0):
            newP = Production()
            newP.document_date = to_date(value[0])
            newP.posting_date = to_date(value[1])
            newP.plant = int(value[2])
            newP.material = str(value[3])
            newP.material_description = str(value[4])
            newP.movement_type = str(value[5])
            newP.cqe_1 = int(value[6])
            newP.cqe_2 = int(value[7])
            newP.que_1 = float(value[8])
            newP.que_2 = float(value[12])
            newP.ue = str(value[9])
            newP.alc_1 = float(value[10])
            newP.type = str(value[11])
            newP.week = int(value[13])
            newP.alc_2 = float(value[14])
            newP.save()
        if(i > 1000):
            break
        i += 1
    return HttpResponse("Load gitpw32")

def table(request):
    data = Production.objects.all()
    context = {
            'data': data
    }
    return render(request, 'cockpit/table.html', context=context)
