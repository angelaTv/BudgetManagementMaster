from django.forms import ModelForm
from .models import *
from django import forms


class BudgetCategoryForm(ModelForm):
    class Meta:
        model = BudgetCategory
        fields = ["category_name"]


class AddExpenseForm(ModelForm):
    entered_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = AddExpense
        fields = ["budget_category", "expense", "remarks", "entered_date"]

    def clean(self):
        cleaned_data = super().clean()
        budget_category = cleaned_data.get("budget_category")
        expense = cleaned_data.get("expense")
        remarks = cleaned_data.get("remarks")
        entered_date = cleaned_data.get("entered_date")

        # if password != confirmpassword:
        #     msg = "password didnt match!provide valid price"
        #     self.add_error("price", msg)


class ReviewForm(ModelForm):
    startdate = forms.DateField(widget=forms.SelectDateWidget)
    enddate = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = AddExpense
        fields = ["budget_category", "startdate", "enddate"]
