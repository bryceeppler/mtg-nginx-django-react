from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('gauntlet/', views.GauntletList.as_view()),
    path('houseOfCards/', views.HouseOfCardsList.as_view()),
    path('kanatacg/', views.KanatacgList.as_view()),
    path('fusion/', views.FusionList.as_view()),
    path('four01/', views.Four01List.as_view()),

    path('gauntletCheapest/', views.GauntletCheapest.as_view()),
    path('houseOfCardsCheapest/', views.HouseOfCardsCheapest.as_view()),
    path('kanatacgCheapest/', views.KanatacgCheapest.as_view()),
    path('fusionCheapest/', views.FusionCheapest.as_view()),
    path('four01Cheapest/', views.Four01Cheapest.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
