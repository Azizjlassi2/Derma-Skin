from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


# Create your models here.

class AppUser(AbstractUser):
    CHOISES = (
        ('Patient','Patient'),
        ('Doctor','Doctor'),
        ('Admin','Admin'),
    )

    Genre = (
        ('Homme','Homme'),
        ('Femme','Femme')
    )

    id = models.AutoField(primary_key=True)
    age = models.IntegerField(blank=True,null=True)
    user_type= models.CharField(null=False,max_length=20, default="Patient" ,choices=CHOISES)
    genre = models.CharField(null=False,max_length=20, default="Homme", choices=Genre)
    gouvernorat = models.CharField(null=False,max_length=20)
    city = models.CharField(null=False,max_length=20)
    number = models.CharField(max_length=20 , null=True,blank=True)
    email = models.EmailField(default="exemple@gmail.com",blank=True,null=True)
    profil_image = models.ImageField(blank=True,null=True,upload_to='pics/')
    contacted_users =models.ManyToManyField('self', blank=True,symmetrical=True)

    created = models.DateTimeField(auto_now_add=True)

    def create_user(self, email, username,number, age, user_type, genre, gouvernorat, city,profil_image, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            number = number,
            age=age,
            user_type=user_type,
            genre=genre,
            gouvernorat=gouvernorat,
            city=city,
            profil_image = profil_image
            
        )
        USERNAME_FIELD = 'email'
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = False
        user.save(using=self._db)
        return user
        
    

    def __str__(self):
        return self.username
    

    def change_email(self,new_email:str):
        self.email = new_email
    

    def change_username(self,new_username:str):
        self.username = new_username

    def change_password(self,new_password:str):
        self.password = new_password

    def change_age(self,new_age):
        self.age = new_age

    def change_gouvernorat(self,new_gouvernorat):
        self.gouvernorat = new_gouvernorat
    
    def change_genre(self,new_genre):
        if new_genre == 'Male':
            self.genre = 'Homme'
        else:
            self.genre = 'Femme'
    

    def change_number(self,new_number):
        self.number = new_number

    def change_city(self,new_city):
        self.city = new_city

    def change_profil_image(self,new_profil_image):
        self.profil_image = new_profil_image




