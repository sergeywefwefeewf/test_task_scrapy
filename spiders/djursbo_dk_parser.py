import json
import logging
from typing import Iterable, List, Optional
from items import Parsed_data

logger = logging.getLogger(__name__)


class DjursboDkParserParser:
    @staticmethod
    def extract_description_department(department_data: dict) -> Optional[str]:
        description_department = department_data.get('DepartmentDescriptions')
        if not description_department:
            return
        try:
            return description_department[0].get('Text')
        except (IndexError, AttributeError):
            logger.info('Cannot find description data on the page')

    @classmethod
    def parse_page(cls, response) -> Iterable:
        json_data = json.loads(response.text)
        try:
            departments_data = json_data['Data']['Departments']
            if not departments_data:
                logger.info('Unable to find departments data')
                return
        except KeyError:
            logger.info('Not expected keys for json objects')
            return
        for department_data in departments_data:
            parsed_item = Parsed_data()
            parsed_item.address = department_data.get('Address')
            parsed_item.department_url = response.urljoin(department_data.get('DepartmentUrl'))
            parsed_item.description = cls.extract_description_department(department_data)
            parsed_item.images = cls.extract_images_data(response, department_data.get('Images'))
            parsed_item.max_rent = department_data.get(department_data.get('MaxRent'))
            parsed_item.min_rent = department_data.get('MinRent')
            parsed_item.name = department_data.get('Name')
            parsed_item.max_rooms = department_data.get('MaxRooms')
            parsed_item.min_rooms = department_data.get('MinRooms')
            yield parsed_item

    @classmethod
    def extract_images_data(cls, response, images_data: List) -> Optional[dict]:
        if not images_data:
            return
        images_dict = {}
        for image_item in images_data:
            image_url = response.urljoin(image_item.get('Url'))
            image_name = image_item.get('Name')
            if not image_name or not image_url:
                continue
            images_dict.update(name=image_name, image_url=image_url)
        return images_dict
