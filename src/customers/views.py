from django.shortcuts import render
from .models import Customer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from products.utils import get_image


def customer_corr_view(request):
    df = pd.DataFrame(Customer.objects.all().values())
    corr = round(df['budget'].corr(df['employment']), 2)

    plt.switch_backend('Agg')
    sns.jointplot(x='budget', y='employment', kind='reg', data=df).set_axis_labels('Presupuesto de la empresa', 'No de empleados')
    graph = get_image()

    context = {
        'graph': graph,
        'corr': corr,
    }

    return render(request, 'customers/main.html', context)

