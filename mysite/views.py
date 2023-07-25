from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import MainContent, Comment
from .forms import CommentForm


def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)

def detail(request, content_id):
    content_list = get_object_or_404(MainContent,pk=content_id)
    context = { 'content_list': content_list}
    return render(request, 'mysite/content_detail.html', context)

@login_required(login_url='accounts:login')
def comment_create(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = content_list
            comment.author = request.user
            comment.save()
            return redirect('detail', content_id=content_list.id)
    else:
        form = CommentForm()
    context = {'content_list': content_list, 'form': form}
    return render(request, 'mysite/content_detail.html', context)

@login_required(login_url='accounts:login') #비로그인 상태에서 댓글을 달기 시도시 로그인창으로 연결
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author: # 작성자가 아닌 사용자가 update를 시도하면
        raise PermissionDenied  #오류 일으킴
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment) #수정 시 최초 작성했던 댓글을 화면에 출력
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)

    context = {'comment': comment, 'form': form}
    return render(request, 'mysite/comment_form.html', context)

@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
     comment = get_object_or_404(Comment, pk=comment_id)
     if request.user != comment.author:
        raise PermissionDenied
     else:
        comment.delete()
     return redirect('detail', content_id=comment.content_list.id)
