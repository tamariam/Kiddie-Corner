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
        print(intent)
        message = f'Webhook received: {event["type"]}'
        return HttpResponse(
            content=message, status=200
            
        )

    def handle_payment_intent_failed(self, event):
        '''
        Handle  the payment_intent.failed webhook e
        '''
        message = f'Webhook received: {event["type"]}'
        return HttpResponse(
            content=message, status=200
            
        )

    