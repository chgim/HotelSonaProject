# def kakao_email(request): # 템플릿에서 사용하고자 하는 컨텍스트 변수를 생성
#     if request.user.is_authenticated and 'kakao' in request.user.socialaccount_set.all()[0].provider:
#         return {'kakao_email': request.user.socialaccount_set.get(provider='kakao').extra_data.get('email', '')}
#     return {'kakao_email': ''} #  현재 로그인한 사용자가 카카오 로그인을 한 경우, 해당 사용자의 카카오 이메일을 반환합니다. 그렇지 않은 경우 None을 반환