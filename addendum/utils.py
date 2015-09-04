import hmac


def generate_key(template_value, template_name):
    """Generate unique key for snippet without key
    """
    return hmac.new(
        template_name.encode(), template_value.encode()
    ).hexdigest()


def has_permission(user):
    """Check permission for Inline Editing
    """
    return user.is_staff and user.is_active
