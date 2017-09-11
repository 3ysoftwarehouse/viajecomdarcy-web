from django.shortcuts import render
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings

from weasyprint import HTML, CSS

class RespPdf(object):

	def __init__(self, template_name, context, css, url):
		self.template_name = template_name
		self.context = context
		self.css = css
		self.url = url

	def run(self):
		html_string = render_to_string(self.template_name, self.context)
		html = HTML(string=html_string, base_url=self.url)
		html.write_pdf(target='/tmp/mypdf.pdf');
		fs = FileSystemStorage('/tmp')
		with fs.open('mypdf.pdf') as pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			response['Content-Disposition'] = 'attachment; filename="recibo.pdf"'
			return response

		return response


'''
Exemplo de como utilizar em uma views
from .utils import RespPdf

class ExportPdf(View):
	def get(self, request):
		context = {}
		pdf = RespPdf('base_pdf.html', context, '/css/main.css', request.build_absolute_uri())
		return pdf.run()
		return render(request, 'pdf.html', context)
'''

	