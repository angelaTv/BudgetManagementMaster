from django.db import models
import datetime

from django.db.models import Sum, Q

from accounts.models import Users


# Create your models here.

class BudgetCategory(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class AddExpense(models.Model):
    user = models.CharField(max_length=120)
    budget_category = models.ForeignKey(BudgetCategory, related_name='category', on_delete=models.CASCADE, null=True,
                                        blank=True)
    expense = models.FloatField()
    remarks = models.TextField()
    entered_date = models.DateField(default=datetime.datetime.now)
    auto_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.expense)

    def monthd(self):
        return self.entered_date.strftime('%m')

    def day(self):
        return self.entered_date.strftime('%d')

    def weekday(self):
        return self.entered_date.strftime('%w') + self.entered_date.strftime('%A')

    def bud(self):
        ex = AddExpense.objects.all()
        # ex=AddExpense.objects.filter(budget_category=self.budget_category)
        total = 0
        sumt = 0
        totallist = []
        for e in ex:
            total = e.expense
            totallist.append(total)
            sumt += total
        return sumt
        # return str(sumt) + str(totallist)

    def budt(self):
        expense_total = AddExpense.objects.aggregate(expenses=Sum('expense', filter=Q(expense__gt=0)))
        return expense_total
