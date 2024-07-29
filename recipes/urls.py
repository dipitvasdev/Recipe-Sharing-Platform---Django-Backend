from django.urls import path
from .views import RecipeListCreate, RecipeListByUser,RecipeUpdateByNameAndUid, RecipeDeleteByNameAndUid


urlpatterns = [
    path('recipes/', RecipeListCreate.as_view(), name='recipe-list-create'),
     path('recipes/user/<str:uid>/', RecipeListByUser.as_view(), name='recipe-list-by-user'),
     path('recipes/update/<str:name>/<str:uid>/', RecipeUpdateByNameAndUid.as_view(), name='recipe-update-by-name-uid'),
     path('recipes/delete/<str:name>/<str:uid>/', RecipeDeleteByNameAndUid.as_view(), name='recipe-delete-by-name-uid'),
]