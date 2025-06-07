from django.shortcuts import render
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from timelines.models import PostModel

# Create your views here.

model = SentenceTransformer('all-MiniLM-L6-v2')

def ai_search_view(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        posts = PostModel.objects.all()
        contents = [post.content for post in posts]
        content_embeddings = model.encode(contents)

        query_embedding = model.encode([query])[0]

        similarities = cosine_similarity([query_embedding],content_embeddings)[0]
        scored_posts = zip(posts, similarities)

        sorted_posts = sorted(scored_posts, key=lambda x: x[1], reverse=True)

        return render(request, 'ai_search/results.html',{'results':results,'query':query})