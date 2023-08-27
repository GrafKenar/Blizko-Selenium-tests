import random


class TestData:
    set1 = {"sub_category": "Насосы",
            "category": "Строительство и ремонт",
            "times": 3,
            "price_low": "1000",
            "price_high": "6000",
            "product_id": "123750536",
            "product_price": 2888,
            "product_name": 'Насос вибрационный, погружной &quot;Ручеек 1&quot; 25 м. верхний забор, БВ-0.12-40-У5',
            "additional_filters": ['Техноприбор', '225 Вт']}

    set2 = {"sub_category": "Крепежные изделия",
            "category": "Материалы",
            "times": 5,
            "price_low": "200",
            "price_high": "300",
            "product_id": "175852622",
            "product_price": 240,
            "product_name": 'Кронштейн B-1 NOTEDO',
            "additional_filters": None}

    set3 = {"sub_category": "Расходные материалы для оргтехники",
            "category": "Компьютеры, IT",
            "times": 2,
            "price_low": "100",
            "price_high": "10000",
            "product_id": "198477927",
            "product_price": 116,
            "product_name": 'Пленка Oracal МТ95 (F099, 500)',
            "additional_filters": None}

    set4 = {"sub_category": "Весы",
            "category": "Оборудование",
            "times": 1,
            "price_low": "3000",
            "price_high": "5000",
            "product_id": "163989833",
            "product_price": 3100,
            "product_name": 'Торговые весы Foodatlas 40кг/2гр ВТ-982S',
            "additional_filters": ["Россия"]}

    data_sets = [set1, set2, set3, set4]

    @staticmethod
    def random_data_set(quantity):
        return random.sample(TestData.data_sets, quantity)
