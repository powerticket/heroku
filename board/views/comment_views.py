from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import (require_http_methods, require_POST,
                                          require_safe)
from ..forms import WritingForm, CommentForm
from ..models import Writing, Comment


@login_required
@require_POST
def create(request, board_pk):
    """create comment

    Args:
        request ([type]): [description]
        writing_pk ([type]): [description]

    Returns:
        [type]: [description]
    """
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.writing = Writing.objects.get(pk=board_pk)
        comment.save()        
    return redirect('board:detail', board_pk)
