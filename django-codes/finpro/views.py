from django.shortcuts import render, get_object_or_404, redirect
import csv
import pandas as pd

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone

from .models import *
from .forms import *

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from wordcloud import WordCloud
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import TSNE
import pickle

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import io, base64
from django.db.models.functions import TruncDay
from matplotlib.ticker import LinearLocator

with open('saved_model.pkl','rb') as file:
  data = pickle.load(file)

model_final = data['model']
tfid_vectorizer = data['tfid_vectorizer']

def text_list(request):
    text = Text.objects.all().order_by('created_date')
    return render(request, 'finpro/text_list.html',{'texts':text})

def post_new(request):
    if request.method=="POST":
        form =PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            prediction = model_final.predict(tfid_vectorizer.transform([post.text]))[0]
            if prediction == 0:
                post.result = 'Negative'
            elif prediction == 1:
                post.result = 'Neutral'
            else:
                post.result = 'Positive'
            post.save()
            return redirect('text_detail',pk=post.pk)
    else: form = PostForm()
    return render(request, 'finpro/post_new.html', {'form':form})

def text_detail(request,pk):
    post = get_object_or_404(Text,pk=pk)
    test_text = [post.text]
    prediction = model_final.predict_proba(tfid_vectorizer.transform(test_text))
            
    x_label = ['Negative', 'Neutral', 'Positive']
    y_label = prediction[0]
    plt.bar(x_label, height = y_label, color = '#a7cdee')
    plt.savefig("output.jpg")
    
    flike = io.BytesIO()
    plt.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()

    context = {'text': post, 'image': b64}
    return render(request, 'finpro/text_detail.html', context)
