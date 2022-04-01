from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

# Return a dictionary called contexts which we are about to create 
# This is a contexts processor - makes this dictionary available to all templates in the applicatio

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    if total < settings.ORDER_DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.ORDER_DISCOUNT_AMOUNT / 100)
        order_discount_delta = settings.ORDER_DISCOUNT_THRESHOLD - total
    else:
        discount = 10
        order_discount_delta = 10
 
    grand_total = discount + total
   
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'order_discount_delta': order_discount_delta,
        'order_discount_threshold': settings.ORDER_DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
