from django.shortcuts import render
from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decimal import Decimal
import json
from django.core import serializers

from .forms import FormPesquisa

# Create your views here.
def index(request):
	titulo = "Bem-Vindo"

	formulario = FormPesquisa(request.POST or None)
	
	if formulario.is_valid():
		fonte = formulario.cleaned_data.get("descricaoFonte")
		natureza = formulario.cleaned_data.get("descricaoNatureza")
		cursor = connection.cursor()

		if 'fonteNatureza' in request.POST:
			cursor.callproc("pesquisafontenatureza", [str(fonte), str(natureza), 500, 0])
			results = cursor.fetchall()
			results_json = json.dumps(results)
		elif 'valorMaximo' in request.POST:
			cursor.callproc("pesquisavalormaximo", [str(fonte), str(natureza), 500, 0])
			results = cursor.fetchall()
			results_json = json.dumps(results)
		elif 'valorMinimo' in request.POST:
			cursor.callproc("pesquisavalorminimo", [str(fonte), str(natureza), 500, 0])
			results = cursor.fetchall()
			results_json = json.dumps(results)
		elif 'valorMedia' in request.POST:
			cursor.callproc("pesquisavalormedia", [str(fonte), str(natureza), 500, 0])
			results = cursor.fetchall()
			#results_dict = [{'codigo':codigo,'data':data,'valor':valor,'municipio':municipio,'orgao':orgao,'natureza':natureza,'fonte':fonte} for codigo, data, valor, municipio, orgao, natureza, fonte in results]
			results_json = json.dumps(results)
			#print (results_json)
			# string_json = '{{"codigo":"{0}","data":"{1}","valor":"{2}","municipio":"{3}","orgao":"{4}","natureza":"{5}","fonte":"{6}"}}'
			# print (string_json)
			# # print (results)

			# results_json = "{"
			# results_json += ",".join([string_json.format(codigo, data, valor, municipio, orgao, natureza, fonte) for codigo, data, valor, municipio, orgao, natureza, fonte in results])
			# results_json += "}"
			# results_json = json.dumps(results_json)
			# # print (results_json)

		# paginator = Paginator(result_set, 10)

		# page = request.GET.get('page')
		# try:
		# 	results = paginator.page(page)
		# except PageNotAnInteger:
		# 	results = paginator.page(1)
		# except EmptyPage:
		# 	results = paginator.page(paginator.num_pages)

		context = {
			"titulo": titulo,
			"formulario": formulario,
			"results": results,
			"results_json": results_json
		}

		return render(request, "index.html", context)
	else:
		context = {
			"titulo": titulo,
			"formulario": formulario,
		}
		return render(request, "index.html", context)
