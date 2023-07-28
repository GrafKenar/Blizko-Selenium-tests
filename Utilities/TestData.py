import random


class TestData:
    set1 = {"sub_category": "Насосы",
            "category": "Строительство и ремонт",
            "times": 3,
            "price_low": "100",
            "price_high": "1000",
            "product_id": "242560351",
            "product_price": 770,
            "product_name": 'Насос поверхностный ДЖИЛЕКС "Джамбо" 60/35 Ч',
            "additional_filters": ['джамбо', '620 Вт']}

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
            "product_price": 100,
            "product_name": 'Пленка Oracal МТ95 (F099, 500)',
            "additional_filters": None}

    set4 = {"sub_category": "Весы",
            "category": "Оборудование",
            "times": 10,
            "price_low": "1000",
            "price_high": "2000",
            "product_id": "175110590",
            "product_price": 1390,
            "product_name": 'Набор гирек для калибровки (500 гр.)',
            "additional_filters": ["Китай"]}

    set5 = {"sub_category": "Смесители",
            "category": "Строительство и ремонт",
            "times": 5,
            "price_low": "0",
            "price_high": "100000",
            "product_id": "214999336",
            "product_price": 2355,
            "product_name": 'Смеситель д/раковины MAGNUS 8400',
            "additional_filters": ['однорычажный', 'встраиваемый', 'шаровый', 'сталь', 'аэратор', 'гибкая', 'Magnus']}

    data_sets = [set1, set2, set3, set4, set5]

    @staticmethod
    def random_data_set(quantity):
        return random.sample(TestData.data_sets, quantity)
