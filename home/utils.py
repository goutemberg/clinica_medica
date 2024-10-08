from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# def render_to_pdf(template_src, context_dict={}):
#     template_src = 'plantaopro/pages/print.html'
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     response = HttpResponse(content_type='application/pdf')
#     pdf_status = pisa.CreatePDF(html, dest=response)

#     if pdf_status.err:
#         return HttpResponse('Some errors were encountered <pre>' + html + '</pre>')

#     return response


def render_to_pdf(template_src, context_dict={}):
    try:
        template_src = 'plantaopro/pages/print.html'
        template = get_template(template_src)
        html = template.render(context_dict)
        response = HttpResponse(content_type='application/pdf')
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        if not pdf.err:
            response.write(result.getvalue())
            return response
        else:
            return HttpResponse('Error rendering PDF', status=500)
    except Exception as e:
        return HttpResponse(f'Error: {e}', status=500)