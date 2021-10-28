from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd
from pyisemail import is_email


def index(request):

    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():

            csv_file = request.FILES['test_file']

            df = pd.read_csv( csv_file )

            df = df[ df['Correo Electronico'].apply(is_email) == True ]
            df = df.drop_duplicates()

            df['dup'] = ( df.duplicated(subset=['Nombre'], keep=False) |
                          df.duplicated(subset=['Correo Electronico'], keep=False) |
                          df.duplicated(subset=['Telefono'], keep=False) )

            df.columns = ['Nombre', 'Correo', 'Tel', 'dup']

            out_df = df.to_dict('records')


            context = { 'form':form,
                        'filename' : csv_file.name,
                        'content': out_df,

            }

            return render(request, 'baseapp/index.html', context )




    else:
        form = UploadFileForm()

    return render(request, 'baseapp/index.html', {'form':form})



