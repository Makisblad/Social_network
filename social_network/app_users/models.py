from autoslug import AutoSlugField
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password, identify_hasher
from django.db.models import EmailField, CharField, BooleanField, DateTimeField, SET_NULL, TextField, ImageField, DateField, SlugField, ManyToManyField, ForeignKey# для оптимизации приложения импортируем только те модули, которые применяем
from django.urls import reverse


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,  email, password=None, username=None, is_active=True, is_staff=None, is_admin=None):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        if not password:
            raise ValueError("The given password must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, name=None):
        user = self.create_user(email=email, username=username, password=password, is_staff=True, is_admin=True)
        return user

    def create_staffuser(self, email, username, password=None, name=None):
        user = self.create_user(email=email, username=username, password=password, is_staff=True, is_admin=False)
        return user




class User(AbstractBaseUser):
    status_choices = [
        ('в активном поиске', 'в активном поиске'),
        ('без отношений', 'без отношений'),
        ('в отношениях с', 'в отношениях с'),
        ('в браке с', 'в браке с'),
        ('все сложно', 'все сложно'),
    ]
    username = CharField(max_length=30, unique=True, verbose_name='Ник')
    email = EmailField(max_length=40, unique=True, verbose_name='e-mail')
    slug = AutoSlugField(populate_from='username', verbose_name='slug')
    first_name = CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = CharField(max_length=30, blank=True, verbose_name='Фамилия')
    birth_date = DateField(blank=True, default='2022-01-01')
    info = TextField(blank=True)
    friends = ManyToManyField('User', blank=True, related_name='user_friends')
    status = CharField(max_length=50, choices=status_choices, default='без отношений')
    partner = ForeignKey('User', SET_NULL, null=True, default=None, blank=True, related_name='user_partner')
    photo = ImageField(upload_to='photo/%Y/%M/%D/', blank=True, null=True)
    staff = BooleanField(default=False)
    admin = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'# определяем поле, по которому будет проводиться верификация
    REQUIRED_FIELDS = ['username']# доп. поля, запрашиваемые при верификации

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        if self.first_name:
            return self.first_name
        else:
            return self.username

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

    def get_absolute_url(self):
        return reverse('user', kwargs={'slug': self.slug})
