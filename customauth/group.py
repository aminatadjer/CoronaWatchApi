from django.contrib.auth.models import Group


def group_perms():
    editorPerm=['article.add_article', 'article.view_article']
    moderatorPerm=['article.delete_article', 'article.change_article']
    healthagentPerm=[]
    EDITOR = Group.objects.create(name='Editor')
    MODERATOR = Group.objects.create(name='Moderator')
    HEALTH_AGENT = Group.objects.create(name='Health Agent')

    EDITOR.permissions.set(editorPerm)
    MODERATOR.permissions.set(moderatorPerm)
    HEALTH_AGENT.permissions.set(healthagentPerm)

