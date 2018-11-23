from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices


from .models import Listing 

def index(request):

	#we want to past listings and pull out ordored listings by descendant
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)

	paginator = Paginator(listings, 3)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)

	context = { 
	    'listings': paged_listings 
	}

	return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
	listing = get_object_or_404(Listing, pk=listing_id)

	context = {
	    'listing': listing
	}
    

	return render(request, 'listings/listing.html',context)



def search(request):
	#searchform filtering
	#get all the listing
	queryset_list = Listing.objects.order_by('-list_date')

	# Keywords
	#let test to see if keywords exist and
	#just want to make sure it's not an empty string
	if 'keywords' in request.GET:
	  keywords = request.GET['keywords']
	  if keywords:
	  	#search a description for any kind words typed in the keyword box, so we use __
	  	#if searching a whole paragraph, and add icontains after we done , 
	  	#like the whole paragraph contain that word which is the keywords
	  	queryset_list = queryset_list.filter(description__icontains=keywords)

	# City
	if 'city' in request.GET:
	  city = request.GET['city']
	  if city:
	    # here instead icontains, we gonna match the exact city so we will use iexact after we done , 
	  	#iexact is case insensitive. if we want case sensitive, we will use exact
	  	queryset_list = queryset_list.filter(city__iexact=city)
    

    # State
	if 'state' in request.GET:
	  state = request.GET['state']
	  if state:
	    # here instead icontains, we gonna match the exact city so we will use iexact after we done , 
	  	#iexact is case insensitive. if we want case sensitive, we will use exact
	  	queryset_list = queryset_list.filter(state__iexact=state)
    

    # bedrooms
	if 'bedrooms' in request.GET:
	  bedrooms = request.GET['bedrooms']
	  if bedrooms:
	    # here instead iexact, we not gonna match the exact bedroom but we will use, 
	  	# lte which means (less than or equal to), so we will use lte
	  	queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)


    # Price
	if 'price' in request.GET:
	  price = request.GET['price']
	  if price:
	    # here instead iexact, we not gonna match the exact bedroom but we will use, 
	  	# lte which means (less than or equal to), so we will use lte
	  	queryset_list = queryset_list.filter(price__lte=price)




	context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
	return render(request, 'listings/search.html', context)

