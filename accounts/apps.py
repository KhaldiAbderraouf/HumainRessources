from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from .models import RightByAccess, BaseUser, UserRight, Role
        right_names = [
            'journal officiel',
            'code',
            'constitution',
            'jurisprudence'
        ]
        for right_name in right_names:
            right = RightByAccess.objects.filter(name=right_name).first()
            if not right:
                right = RightByAccess(name=right_name)
                right.save()

        for user in BaseUser.objects.all():
            for right in RightByAccess.objects.all():
                user_right = UserRight.objects.filter(user=user.id, right=right.id).first()
                if not user_right:
                    user_right = UserRight(
                        user=user,
                        right=right
                    )
                    user_right.save()

        role_names = [
            'admin',
            'manager',
            'employee'
        ]
        for role_name in role_names:
            role = Role.objects.filter(name=role_name).first()
            if not role:
                role = Role(name=role_name)
                role.save()
