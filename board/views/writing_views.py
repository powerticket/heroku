from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import (require_http_methods, require_POST,
                                          require_safe)

from ..forms import WritingForm, CommentForm
from ..models import Writing, Comment


# board create, read
@require_safe
def index(request):
    """list writing

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    writings = Writing.objects.order_by('-pk')
    page = request.GET.get('page', '1')
    paginator = Paginator(writings, 20)
    page_obj = paginator.get_page(page)
    context = {
        'writings': page_obj,
    }
    return render(request, 'board/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    """create writing

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    if request.method == 'POST':
        writing_form = WritingForm(request.POST)
        if writing_form.is_valid():
            writing = writing_form.save(commit=False)
            writing.author = request.user
            writing.save()
            return redirect('board:detail', writing.pk)
    else:
        writing_form = WritingForm()
    context = {
        'writing_form': writing_form,
    }
    return render(request, 'board/writing.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, board_pk):
    """update writing

    Args:
        request ([type]): [description]
        board_pk ([type]): [description]

    Returns:
        [type]: [description]
    """
    writing = get_object_or_404(Writing, pk=board_pk)
    if request.method == 'POST':
        writing_form = WritingForm(request.POST, instance=writing)
        if writing_form.is_valid():
            writing = writing_form.save()
            return redirect('board:detail', writing.pk)
    else:
        writing_form = WritingForm(instance=writing)
    context = {
        'writing_form': writing_form,
    }
    return render(request, 'board/writing.html', context)


@login_required
@require_safe
def delete(request, board_pk):
    """delete writing

    Args:
        request ([type]): [description]
        board_pk ([type]): [description]

    Returns:
        [type]: [description]
    """
    writing = get_object_or_404(Writing, pk=board_pk)
    if writing.author == request.user:
        writing.delete()
    return redirect('board:index')


@login_required
@require_safe
def detail(request, board_pk):
    """detail writing

    Args:
        request ([type]): [description]
        board_pk ([type]): [description]

    Returns:
        [type]: [description]
    """
    writing = get_object_or_404(Writing, pk=board_pk)
    comment_form = CommentForm()
    comments = writing.comments.all()
    context = {
        'writing': writing,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'board/detail.html', context)
