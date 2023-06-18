from accounts.models import UserProfile

# accounts 앱의 UserProfile 모델을 그대로 가져와서 사용합니다.
class UserProfile(UserProfile):
    class Meta:
        proxy = True

    def some_custom_method(self):
        # 추가적인 메소드나 속성을 정의할 수 있습니다.
        pass