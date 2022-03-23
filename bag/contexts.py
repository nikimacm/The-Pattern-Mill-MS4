from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FIRST_ORDER_DISCOUNT:
        discount = total * Decimal(settings.STANDARD_PRICE_PERCENTAGE / 100)
        standard_price_delta = settings.STANDARD_PRICE_PERCENTAGE - total
    else:
        price = 0
        first_order_delta = 0
    
    grand_total = price - total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'price': price,
        'standard_price_delta': fstandard_price_delta,
        'first_order_discount': settings.FIRST_ORDER_DISCOUNT,
        'grand_total': grand_total,
    }

    return context