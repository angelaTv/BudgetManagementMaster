from django.test import TestCase

# Create your tests here.
class BudgetReview(TemplateView):
    model_name = AddExpense
    form_class=ReviewForm
    template_name = 'mainapp/review.html'

    def get_queryset(self):
        data = self.model_name.objects.all()
        return data

    def get(self, request, *args, **kwargs):
        context = {}
        context['data'] = self.get_queryset()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass
        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     category=(request.POST.get("startdate"))
        #     startdate = (request.POST.get("startdate"))
        #     enddate = (request.POST.get("enddate"))
        #     print(startdate, enddate)
        #     at = self.model_name.objects.filter(budget_category__category_name='Transport').filter(
        #         entered_date__range=[startdate, enddate])
        #     for value in at:
        #         print(value)
        #         print(value.expense)
        #         lst = [item.expense for item in at]
        #         t = sum(lst)
        #     print(t)
        #     sumo = float(t)
        #     print(type(sumo))
        #     context={}
        #     context['t'] = sumo
        #     return render(request, self.template_name, context)
        #


# def BudgetReport(request):
#     r = request.user
#     print(r)
#     qs = AddExpense.objects.all()
#     context = {'data': qs}
#     return render(request, 'mainapp/budgetreport.html', context)


def BudgetReport(request):
    if request.method == 'POST':
        context = {}
        startdate = (request.POST.get("startdate"))
        enddate = (request.POST.get("enddate"))
        print(startdate, enddate)
        at = AddExpense.objects.filter(budget_category__category_name='Transport').filter(entered_date__range=[startdate,enddate])
        for value in at:
            print(value)
            print(value.expense)
            lst = [item.expense for item in at]
            t = sum(lst)
        print(t)
        sumo = float(t)
        print(type(sumo))
        context['t'] = sumo
        qs = AddExpense.objects.all()
        context['data']= qs
        return render(request, 'mainapp/budgetreport.html', context)
    return render(request, 'mainapp/enterdatereview.html')