"""mainapp URL Configuration

"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from mainapp import views
from mainapp.views import BudgetReport, Analysis, BudgetReview, graphty, graphReport

#

urlpatterns = [
    path('createcategory', views.CreateCategory.as_view(), name='createcategory'),
    path('categorylist', views.CategoryList.as_view(), name='categorylist'),
    path('updatecategory/<int:pk>', views.CategoryUpdate.as_view(), name='updatecategory'),
    path('deletetecategory/<int:pk>', views.CategoryDelete.as_view(), name='deletecategory'),

    path('createaddexpense', views.CreateAddExpense.as_view(), name='createaddexpense'),
    path('addexpenselist', views.AddExpenseList.as_view(), name='addexpenselist'),
    path('addexpensedetail/<int:pk>', views.AddExpenseDetail.as_view(), name='addexpensedetail'),
    path('updateaddexpense/<int:pk>', views.AddExpenseUpdate.as_view(), name='updateaddexpense'),
    path('deleteteaddexpense/<int:pk>', views.AddExpenseDelete.as_view(), name='deleteaddexpense'),

    path('reporthome/', lambda request: render(request, "mainapp/homeeports.html"), name='reporthome'),
    path('reportbud/', BudgetReport, name='reportbudget'),
    path('analysis/', Analysis, name='analysis'),
    path('review/', views.BudgetReview.as_view(), name='review'),
    path('graph/', graphty, name='graphty'),
    path('graphrepo/', graphReport, name='graphrepo'),

]
# path('createbudget', views.CreateBudget.as_view(), name='createbudget'),
# path('budgetlist', views.BudgetList.as_view(), name='budgetlist'),
# path('updatebudget/<int:pk>', views.BudgetUpdate.as_view(), name='updatebudget'),
