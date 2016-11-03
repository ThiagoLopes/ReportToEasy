from docxtpl import DocxTemplate
import jinja2schema

def is_valid_template(documento):
    doc = DocxTemplate(documento)
    xml = doc.get_xml()
    xml = doc.patch_xml(xml) # patch xml for jinja2schema
    variables = jinja2schema.infer(xml)
    list_xml = list(variables.keys()) # create a nice list
    if not list_xml:
        return False
    else:
        return True
    # list_xml = list(variables.keys()) # create a nice list
    # print(list_xml)
    # return True
