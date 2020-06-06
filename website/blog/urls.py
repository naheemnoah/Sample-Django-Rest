from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .apiviews import HelloView
from .apiviews import PollList, PollDetail,ChoiceList, CreateVote, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet

router = DefaultRouter()
router.register('blog', PollViewSet, basename='polls')

urlpatterns = [
    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    # path("accounts/login/", include('allauth.urls'), name="login"),
    # path("login/", obtain_auth_token, name='api_token_auth'),
    path('login/', LoginView.as_view(), name='login'),
    path('hello/', HelloView.as_view(), name='hello'),
    # path("rest-auth/", include('rest_auth.urls')),
    path("blog/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("blog/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),

]