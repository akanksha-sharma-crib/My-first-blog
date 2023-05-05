from datetime import timezone
from django.shortcuts import get_object_or_404, render
import pkg_resources

# Create your views here.
from .models import Post


def post_list(request):
    post= get_object_or_404(Post, pk =pkg_resources )
    posts = Post.objects.filter(published_date__lte= timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})

