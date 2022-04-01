from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the licence type to the shopping bag """

    item_data = (request.POST.get('item_data'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] = item_data
    else:
        bag[item_id] = item_data

    request.session['bag'] = bag
    return redirect(redirect_url)
