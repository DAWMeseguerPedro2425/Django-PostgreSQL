from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


#----UD8.1.b----
# Manager para el modelo MyUser
class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

#----UD8.1.b----
#Modelo de usuario
# Cambiado de AbstractBaseUser a AbstractUser
class MyUser(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['email']
        
    
    #----UD8.1.d----
    #Añadir los campos groups y user_permissions para que herede de AbstractUser
    #y poder usar los grupos y permisos de django
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myuser_set',
        blank=True,
    )
    #Añadir los campos groups y user_permissions para que herede de AbstractUser
    #y poder usar los grupos y permisos de django
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myuser_set',
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()


