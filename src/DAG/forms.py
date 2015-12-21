from django import forms

class FormPesquisa(forms.Form):
	descricaoFonte = forms.CharField(required = False, label='Fonte', max_length=200)
	descricaoNatureza = forms.CharField(required = False, label='Natureza', max_length=200)