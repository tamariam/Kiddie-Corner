from django .http import HttpResponse


class StripeWH_Handler:
    '''Handle stripe webhooks'''
    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        '''
        Handle an unexpected webhook events
        '''
        message = f'Webhook received: {event["type"]}'
        return HttpResponse(
            content=message, status=200
            
        )
    