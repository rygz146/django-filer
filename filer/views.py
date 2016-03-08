# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.http import Http404
from django.shortcuts import redirect, get_object_or_404

from .models import File


def canonical(request, uploaded_at, file_id):
    """
    Redirect to the current url of a public file
    """
    filer_file = get_object_or_404(File, pk=file_id, is_public=True)
    if (uploaded_at != filer_file.uploaded_at.strftime('%s') or
            not filer_file.file):
        raise Http404('No %s matches the given query.' % File._meta.object_name)
    return redirect(filer_file.url)
