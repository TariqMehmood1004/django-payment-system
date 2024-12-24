from django.conf import settings
from django.shortcuts import render, redirect
import requests
import stripe
from django.core.mail import send_mail


headers = {
    'X-Api-Key': settings.API_NINJA_KEY
}


# Create your views here.
def index(request):

    # response = requests.get(f"{settings.API_NINJA_BASE_URL}/cats?name=abyssinian", headers=headers)
    response = requests.get(f"https://api.escuelajs.co/api/v1/products")

    response_data = response.json()
    first_image = response_data[0]['images'][0]
    print(f"\n\n IMAGE: {first_image.strip('["\"')}\n\n")

    if response.status_code == requests.codes.ok:
        # print(response.text)
        return render(request, 'index.html', context={
            'data': response_data
        })
    else:
        # print("Error:", response.status_code, response.text)
        return render(request, 'index.html', context={
            'data': response_data
        })

def checkout_session(request):
    """
    Using the stripe
    """

    cat_id = request.POST.get('cat_id')
    name = request.POST.get('name')
    origin = request.POST.get('origin')
    image_link = request.POST.get('image_link')
    price = request.POST.get('price')

    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            checkout_session_data = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': name,
                                'images': [
                                    image_link,
                                ],
                                'metadata': {
                                    'cat_id': cat_id,
                                    'origin': origin,
                                },
                            },
                            'unit_amount': price,
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=f'{settings.HOST}/success',
                cancel_url=f'{settings.HOST}/cancel',
            )


            # Send email to the customer
            send_mail(
                'Payment Confirmation',
                f'Your order has been placed successfully. Your order id is {checkout_session_data.id}.',
                settings.EMAIL_HOST_USER,
                ['johnbrrighte7427206@gmail.com'],  # Send email to the customer email
                fail_silently=False,
            )

            return redirect(checkout_session_data.url)
        except Exception as e:
            return render(request, 'cancel.html', context={'error': e})
    else:
        return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')