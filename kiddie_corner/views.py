from django.shortcuts import render
# custom view for error 404


def error_404(request, exception):
    """"
    Handles HTTP 404 errors
    """
    return render(request, 'errors/404.html', status=404)


# def error_500(request,):
#     """"
#     Handles HTTP 500 errors
#     """
#     return render(request, 'errors/500.html')