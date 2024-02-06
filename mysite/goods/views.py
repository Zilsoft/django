from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Каталог магазина",
        "goods": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 12000.00,
            },
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 11000.00,
            },
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 15000.00,
            },
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 18000.00,
            },
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 22000.00,
            },
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 25000.00,
            },
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 8000.00,
            },
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 12500.00,
            },
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 25000.00,
            },
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 32000.00,
            },
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 11800.00,
            },
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик  и три стула",
                "description": "Комплек из трёх стульев и дизайнерский столик для гостинной",
                "price": 17000.00,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
