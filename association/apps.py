from django.apps import AppConfig


class AssociationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'association'

    def ready(self):
        try:
            from django.contrib.auth.models import User

            username = "admin"
            password = "Newlig2026@"

            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email="admin@example.com",
                    password=password,
                )
                print("✅ Default admin user created.")
        except Exception:
            # Ignore errors during startup (e.g. migrations not yet applied)
            pass