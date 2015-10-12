from django.conf import settings

default_inline_tinymce = {
    'inline': True,
    'plugins': [
        'advlist autolink lists link image charmap print preview anchor',
        'searchreplace visualblocks code fullscreen',
        'insertdatetime media table contextmenu paste'
    ],
    'toolbar': 'insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
    'extended_valid_elements': 'span'
}

ADDENDUM_INLINE_EDITING = getattr(settings, 'ADDENDUM_INLINE_EDITING', True)
ADDENDUM_INLINE_TINYMCE = getattr(settings, 'ADDENDUM_INLINE_TINYMCE', default_inline_tinymce)
