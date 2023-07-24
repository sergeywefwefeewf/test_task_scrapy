import logging
from typing import Iterable

import scrapy
from spiders.djursbo_dk_parser import DjursboDkParserParser

logger = logging.getLogger(__name__)


class DjursboDkCrawler(scrapy.Spider):
    name = 'djursbo_dk'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = DjursboDkParserParser

    allowed_domains = ["djursbo.dk"]

    @staticmethod
    def domain_url() -> str:
        return "https://djursbo.dk"

    @classmethod
    def page_url(cls) -> str:
        return f"{cls.domain_url()}/Umbraco/api/TenancySearch/GetSearchResults"

    @staticmethod
    def _search_headers() -> dict:
        return {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8"}

    def body(self) -> str:
        return '{"Areas":[{"Id":1,"Selected":false,"Text":"Pindstrup"},{"Id":10,"Selected":false,"Text":"Nimtofte"}' \
               ',{"Id":11,"Selected":false,"Text":"Mørke"},{"Id":12,"Selected":false,"Text":"Lime"},{"Id":13,"Selec' \
               'ted":false,"Text":"Mols"},{"Id":14,"Selected":false,"Text":"Tirstrup/ Balle"},{"Id":15,"Selected":f' \
               'alse,"Text":"Ebeltoft"},{"Id":2,"Selected":false,"Text":"Kolind"},{"Id":3,"Selected":false,"Text":"' \
               'Ryomgård"},{"Id":4,"Selected":false,"Text":"Hornslet"},{"Id":5,"Selected":false,"Text":"Thorsager"}' \
               ',{"Id":6,"Selected":false,"Text":"Rønde"},{"Id":7,"Selected":false,"Text":"Auning"},{"Id":8,"Select' \
               'ed":false,"Text":"Pederstrup"},{"Id":9,"Selected":false,"Text":"Skødstrup"}],"TenancyTypes":[{"Id":' \
               '1,"Selected":false,"Text":"Lejligheder"},{"Id":2,"Selected":false,"Text":"Ungdomsboliger"},{"Id":5,' \
               '"Selected":false,"Text":"Værelser"},{"Id":10,"Selected":false,"Text":"Ældreboliger "}],"ApartmentTy' \
               'pes":[{"Id":6,"Selected":false,"Text":"Etagebyggeri"},{"Id":7,"Selected":false,"Text":"Rækkehuse"},' \
               '{"Id":8,"Selected":false,"Text":"Dobbelthuse"},{"Id":9,"Selected":false,"Text":"Enkelthuse"}],"Room' \
               's":{"SelectedFrom":1,"SelectedTo":5},"Rent":{"SelectedTo":9000},"Size":{"SelectedFrom":0,"SelectedT' \
               'o":140},"WaitTimes":[{"Id":2,"Selected":false,"Text":"Under 1 år"},{"Id":3,"Selected":false,"Text":' \
               '"Over 1 år"},{"Id":4,"Selected":false,"Text":"Over 3 år"}],"Premises":[{"Id":7,"Selected":false,"Te' \
               'xt":"Altan"},{"Id":16,"Selected":false,"Text":"Elevator"},{"Id":17,"Selected":false,"Text":"Have"}]' \
               ',"ShowOnlyAvailable":false,"OnlyWherePetAllowed":false,"Companies":[{"Departments":[{"Id":118,"Sele' \
               'cted":false,"Text":"Plejeboligerne Søhusvej"},{"Id":1,"Selected":false,"Text":"Tendrupvej - Ballesv' \
               'ej"},{"Id":120,"Selected":false,"Text":"Carl Th. Dreyers Vej 15A - 25D"},{"Id":114,"Selected":false' \
               ',"Text":"Reberbanen"},{"Id":115,"Selected":false,"Text":"Hyrdeledet"},{"Id":11,"Selected":false,"Te' \
               'xt":"Mørke - Lime - Hornslet"},{"Id":5,"Selected":false,"Text":"Tendrupvej"},{"Id":2,"Selected":fal' \
               'se,"Text":"Ballesvej"},{"Id":28,"Selected":false,"Text":"Søvej"},{"Id":27,"Selected":false,"Text":"' \
               'Thorsgade -  Lille Randers"},{"Id":17,"Selected":false,"Text":"Elkjærslund"},{"Id":7,"Selected":fal' \
               'se,"Text":"Alpedalen"},{"Id":3,"Selected":false,"Text":"Ballesvej - Tendrupvej"},{"Id":32,"Selected' \
               '":false,"Text":"Begoniavej"},{"Id":29,"Selected":false,"Text":"Vagtelvej Rønde"},{"Id":14,"Selected' \
               '":false,"Text":"Ungdomsboliger Rodskovvej"},{"Id":6,"Selected":false,"Text":"Degnevænget - Brogårdv' \
               'ej - Åsen - Skolevej"},{"Id":80,"Selected":false,"Text":"Nannas Vænge"},{"Id":41,"Selected":false,"' \
               'Text":"Enighedsvej"},{"Id":113,"Selected":false,"Text":"Energivej - Knebel - Lysningen"},{"Id":20,"' \
               'Selected":false,"Text":"Købmandshaven 5 - 9"},{"Id":73,"Selected":false,"Text":"Tendrup Møllevej Bo' \
               'fællesskab"},{"Id":55,"Selected":false,"Text":"Ryomgård - Nimtofte"},{"Id":79,"Selected":false,"Tex' \
               't":"Søhusvej træhuse"},{"Id":102,"Selected":false,"Text":"Strandgårdshøj etageboliger"},{"Id":21,"S' \
               'elected":false,"Text":"Engvangen"},{"Id":65,"Selected":false,"Text":"Skovparken Bofællesskab"},{"Id' \
               '":77,"Selected":false,"Text":"Tendrup Møllevej"},{"Id":25,"Selected":false,"Text":"Thorsgade - Thor' \
               'sager"},{"Id":71,"Selected":false,"Text":"Egevej ældreboliger - Hornslet"},{"Id":31,"Selected":fals' \
               'e,"Text":"Gartnerhaven - Vorrevej"},{"Id":42,"Selected":false,"Text":"Banevænget"},{"Id":67,"Select' \
               'ed":false,"Text":"Bugtrupvej  9A - 9F - Enggårdsbakken 8A-12B"},{"Id":81,"Selected":false,"Text":"T' \
               'oftehøjen"},{"Id":26,"Selected":false,"Text":"Baunehøjparken"},{"Id":107,"Selected":false,"Text":"S' \
               'kanseparken I"},{"Id":111,"Selected":false,"Text":"Tirstrup - Balle - Knebel"},{"Id":112,"Selected"' \
               ':false,"Text":"Fyrreparken - Ilbjergvej - Flintehaven"},{"Id":78,"Selected":false,"Text":"Plejeboli' \
               'ger Tendrup Møllevej"},{"Id":110,"Selected":false,"Text":"Granparken"},{"Id":54,"Selected":false,"T' \
               'ext":"Kolind - Pindstrup - Pederstrup"},{"Id":51,"Selected":false,"Text":"Rugvangen"},{"Id":101,"Se' \
               'lected":false,"Text":"Strandgårdshøj dobbelthuse"},{"Id":117,"Selected":false,"Text":"Søhusparken æ' \
               'ldreboliger"},{"Id":56,"Selected":false,"Text":"Ryomgård Midtpunkt"},{"Id":103,"Selected":false,"Te' \
               'xt":"Nørreallé,Østerallé.Arbogavej,Bakkehegnet,Bryggerivej"},{"Id":75,"Selected":false,"Text":"Horn' \
               'slet bymidte"}],"Id":1,"Selected":false,"Text":"djursBO"}]}'

    def start_requests(self) -> Iterable:
        yield scrapy.Request(url=self.page_url(),
                             method="POST",
                             headers=self._search_headers(),
                             body=self.body(),
                             callback=self.parse_documents)

    def parse_documents(self, response) -> Iterable:
        documents = self.parser.parse_page(response)
        counter = 0
        for document in documents:
            counter += 1
            yield document
        logger.info(f'From source djursbo.dk {counter} objects parsed')
