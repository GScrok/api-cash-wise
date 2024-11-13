from django.urls import path

from finance_control.views.login_view import LoginView
from finance_control.views.user_view import UsersView
from finance_control.views.categories_view import CategoriesView
from finance_control.views.cards_view import CardsView
from infrastructure.api.finance_control.views.accounts_view import AccountView
from finance_control.views.subcategories_view import SubcategoryView, SubcategoryCustomView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('users/', UsersView.as_view(), name='users-list'),
    path('users/<uuid:pk>/', UsersView.as_view(), name='user-detail'),
    path('categories/', CategoriesView.as_view(), name='categories-list'),
    path('categories/<uuid:pk>/', CategoriesView.as_view(), name='category-detail'),
    path('cards/', CardsView.as_view(), name='cards-list'),
    path('cards/<uuid:pk>/', CardsView.as_view(), name='card-detail'),
    path('accounts/', AccountView.as_view(), name='accounts-list'),
    path('accounts/<uuid:pk>/', AccountView.as_view(), name='account-detail'),
    path('subcategories/', SubcategoryView.as_view(), name='subcategories-list'),
    path('subcategory/<uuid:pk>', SubcategoryView.as_view(), name='subcategory-detail'),
    path('subcategories/category/<uuid:pk>/', SubcategoryCustomView.as_view(), name='subcategories-by-category'),
]
