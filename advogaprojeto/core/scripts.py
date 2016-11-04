from docxtpl import DocxTemplate
import jinja2schema
MEDIA_ROOT = "docs/"

def is_template(documento):
    doc = DocxTemplate(MEDIA_ROOT + documento)
    xml = doc.get_xml()
    xml = doc.patch_xml(xml)  # patch xml for jinja2schema
    variables = jinja2schema.infer(xml)
    list_xml = list(variables.keys())  # create a nice list
    return list_xml

def clear_query(query):
    query.pop("csrfmiddlewaretoken", None)
    return query

def generate_download():
    pass
