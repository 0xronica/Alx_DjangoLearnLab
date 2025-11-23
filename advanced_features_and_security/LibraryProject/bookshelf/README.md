# Permissions & Groups Setup

This application uses Django’s permissions and groups system to control access.

# Custom Model Permissions
The `Article` model defines four custom permissions:

- can_view — Allows viewing articles
- can_create — Allows creating articles
- can_edit — Allows editing articles
- can_delete — Allows deleting articles

These are defined in `Article.Meta.permissions`.

Groups
Three groups are created:

1. Viewers
- can_view

2. Editors
- can_view
- can_create
- can_edit

3. Admins
- can_view
- can_create
- can_edit
- can_delete

# Usage in Views
Django's @permission_required decorator is used to restrict access


