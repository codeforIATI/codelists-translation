from lxml import etree
import json
import os

nsmap = {"xml": "http://www.w3.org/XML/1998/namespace"}


class GenerateJSON():

    def escape_string(self, string):
        return source_string.encode('utf-8').replace(r'\\', r'\\\\')


    def get_lang_xpath(self):
        if self.lang == 'en':
            return 'not(@xml:lang)'
        else:
            return '@xml:lang="{}"'.format(self.lang)

    def get_metadata(self, code):
        out = {}
        lang_xpath = self.get_lang_xpath()
        for child in code.getchildren():
            if child.tag == 'category': continue
            narrative = child.xpath('narrative[{}]'.format(lang_xpath), namespaces=nsmap)
            if len(narrative) > 0:
                out[child.tag] = narrative[0].text
            else:
                out[child.tag] = None
        return out


    def get_code_data(self, code):
        out = {}
        lang_xpath = self.get_lang_xpath()
        code_code = code.find('code').text
        for child in code.getchildren():
            if child.tag == 'code': continue
            narrative = child.xpath('narrative[{}]'.format(lang_xpath), namespaces=nsmap)
            if len(narrative) > 0:
                out[child.tag] = narrative[0].text
            else:
                out[child.tag] = None
        return code_code, out


    def get_codelists(self, folder, codelist_name):
        doc = etree.parse(os.path.join("xml", folder, 'xml', '{}.xml'.format(codelist_name)))
        metadata = self.get_metadata(doc.find("metadata"))
        code_data = dict([self.get_code_data(code) for code in doc.xpath("/codelist/codelist-items/codelist-item")])
        data = {
            'metadata': metadata,
            'codelist-items': code_data
        }
        os.makedirs('json/{}/{}'.format(self.lang, folder), exist_ok=True)
        with open('json/{}/{}/{}.json'.format(self.lang, folder, codelist_name), 'w') as outfile:
            json.dump(data, outfile, indent=4)


    def get_folder(self, folder):
        codelists = [os.path.splitext(filename)[0] for filename in os.listdir(os.path.join("xml", folder, "xml")) if filename.endswith(".xml")]
        [self.get_codelists(folder, codelist_name) for codelist_name in codelists]


    def __init__(self, lang):
        self.lang = lang
        folders = os.listdir("xml")
        for folder in folders:
            self.get_folder(folder)


langs = ['en', 'fr', 'es', 'pt']

for lang in langs:
    GenerateJSON(lang=lang)
