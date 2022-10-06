from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password, identify_hasher
from django.db.models import EmailField, CharField, BooleanField, DateTimeField #для оптимизации приложения импортируем только те модули, которые применяем


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,  email, password=None, name=None, full_name=None, is_active=True, is_staff=None, is_admin=None):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        if not password:
            raise ValueError("The given password must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, name=None):
        user = self.create_user(email=email, name=name, password=password, is_staff=True, is_admin=True)
        return user

    def create_staffuser(self, email, password=None, name=None):
        user = self.create_user(email=email, name=name, password=password, is_staff=True, is_admin=False)
        return user



class User(AbstractBaseUser):
    email = EmailField(unique=True, max_length=50)
    name = CharField(blank=True, max_length=255, null=True)
    full_name = CharField(blank=True, max_length=255, null=True)
    is_active = BooleanField(default=True)
    staff = BooleanField(default=False)
    admin = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'# определяем поле, по которому будет проводиться верификация
    REQUIRED_FIELDS = []# доп. поля, запрашиваемые при верификации

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        if self.name:
            return self.name
        else:
            return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        else:
            return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):# функция для предоставления прав на модули
        return True

    @property
    def is_staff(self):
        if self.admin:
            return True
        else:
            return self.staff

    @property
    def is_admin(self):
        return self.admin

    def save(self, *args, **kwargs):
        try:
            _alg = identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

