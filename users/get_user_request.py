def get_user_request(request):
    return request.user if request.user.is_anonymous else None