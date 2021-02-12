from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class BaseUser(User):
    @property
    def full_name(self):
        """Returns the person's full name."""
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        proxy = True

    def has_access(self, right_id):

        try:
            right = Right.objects.get(id=right_id)
        except:
            right = None
        if right:
            for user_role in self.user_roles.all():
                if right in [role_right.right for role_right in user_role.role.role_rights.all()]:
                    return True

            user_right = self.user_rights.get(right=right.id)
            return user_right.has_access
        return False


def has_access(instance, user_id):
    return instance.has_access(user_id)


class Right(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    @staticmethod
    def has_access(user_id):
        raise NotImplementedError()


class RightByAccess(Right):

    def has_access(self, user_id):
        user_right = UserRight.objects.get(user=user_id, right=self.id)
        if user_right:
            if user_right.force_access:
                return True
        else:
            return False
        try:
            from backend.models import Abonnement
        except ImportError:
            return False
        else:
            return any([
                abonnement.est_valide and
                (self.id in [
                    right.id for right in abonnement.rights.all()
                ])
                for abonnement in Abonnement.objects.filter(
                    user=user_id
                ).all()
            ])


class UserRight(models.Model):
    user = models.ForeignKey(BaseUser, related_name='user_rights', on_delete=models.CASCADE)
    right = models.ForeignKey(Right, on_delete=models.CASCADE)
    force_access = models.BooleanField(default=False)

    @property
    def has_access(self):
        if hasattr(self.right, 'rightbyaccess'):
            return self.right.rightbyaccess.has_access(self.user.id)

        return self.right.has_access(self.user.id)

    def __str__(self):
        return self.right.name + " " + str(self.has_access)

    class Meta:
        unique_together = (("user", "right"),)


class Role(models.Model):
    name = models.CharField(_('name'), max_length=255, primary_key=True)


class UserRole(models.Model):
    user = models.ForeignKey(BaseUser, related_name='user_roles', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class RoleRight(models.Model):
    role = models.ForeignKey(Role, related_name='role_rights', on_delete=models.CASCADE)
    right = models.ForeignKey(Right, on_delete=models.CASCADE)
