from django.shortcuts import render
from .forms import PlagiarismModelForm
import sklearn
import nltk
import numpy as np
from .models import Plagiarism
# from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create your views here.
def index(request):
    return render(request, 'index.html')

def fetch(request):
        if request.method =='POST':
            form = PlagiarismModelForm(request.POST)
            if form.is_valid():
                #  print(form)
                 form.save()
        else:
              form = PlagiarismModelForm()
        return render(request, 'form.html', {'form':form})

def detect(request):
       # Get the submitted text
        text = Plagiarism.objects.get().text
        # Preprocess the text
        nltk.download('punkt')  # Download tokenizer data (only required once)
        tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
        preprocessed_text = ' '.join(tokenizer.tokenize(text.lower()))

        # Sample documents for comparison
        documents = [
            "This is the first document.",
            "This document is the second document.",
            "And this is the third one.",
            "Is this the first document?"
        ]

        # Preprocess the documents
        preprocessed_documents = [' '.join(tokenizer.tokenize(doc.lower())) for doc in documents]

        # Create the document-term matrix
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(preprocessed_documents)
        # Calculate cosine similarity between the text and documents
        text_vector = vectorizer.transform([preprocessed_text])
        similarity_scores = cosine_similarity(text_vector, X)[0]

        # # Determine the most similar document
        most_similar_index = similarity_scores.argmax()
        most_similar_score = similarity_scores[most_similar_index]
        most_similar_document = documents[most_similar_index]
      
            
        context = {
                'text':text, 
                'similarity':most_similar_score, 
                'document': most_similar_document
        }
          

        return render(request, 'result.html', context)

     
