from django .http import HttpResponse


class StripeWH_Handler:
    '''Handle stripe webhooks'''
    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        '''
        Handle an unexpected webhook events
        '''
        message = f'Unhandled Webhook received: {event["type"]}'
        return HttpResponse(
            content=message, status=200
            
        )

    def handle_payment_intent_succeeded(self, event):
        '''
        Handle payment_intent.succeeded webhook
        '''
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details 
        shipping_details = intent.shipping
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        grand_total = round(stripe_charge.amount / 100, 2)
        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        try:
            order = Order.object.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    eircode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                message = f'Webhook received: {event["type"]}|SUCCESS:Verified order already in database'
                return HttpResponse(
                content=message, status=200
                )
        except Order.DoesNotExist:
            try:
             
                order = Order.objects.create(
                full_name=shipping_details.name,
                email=billing_details.email,
                phone_number=shipping_details.phone,
                country=shipping_details.address.country,
                eircode=shipping_details.address.postal_code,
                town_or_city=shipping_details.address.city,
                street_address1=shipping_details.address.line1,
                street_address2=shipping_details.address.line2,
                county=shipping_details.address.state,
                original_bag=bag,
                stripe_pid=pid,
            )
            for item_id, quantity in json.loads(bag).items():
                product = Product.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                )
                order_line_item.save()
        except Exception  as e:
            if order:
                order.delete()
            return HttpResponse(content=f'Webhook received:{event['type']} | Error:{e}',status=500)
        


    def handle_payment_intent_failed(self, event):
        '''
        Handle  the payment_intent.failed webhook e
        '''
        message = f'Webhook received: {event["type"]}'
        return HttpResponse(
            content=message, status=200
            
        )

    