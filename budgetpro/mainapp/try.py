#
# # ------Model Budget ------------
# class BudgetSetup(models.Model):
#     mybuget = models.FloatField(default=2000)
#
#     def __str__(self):
#         return str(self.mybuget)
# -----End Model Budget ------------
# -----Form Budget ------------
# class BudgetSetupForm(ModelForm):
#     class Meta:
#         model = BudgetSetup
#         fields = ["mybuget"]
# -----Form Model Budget ------------

#
# ------Start view for BudgetSetup ------------
# class CreateBudget(CreateView):
#     model = BudgetSetup
#     fields = ['mybuget']
#     success_url = reverse_lazy('budgetlist')
#
#
# class BudgetList(ListView):
#     model = BudgetSetup
#
#
# class BudgetUpdate(UpdateView):
#     model = BudgetSetup
#     fields = ['mybuget']
#     success_url = reverse_lazy('budgetlist')
#
#
# # ------End view for BudgetSetup --------------