from django.db import models
from django.contrib.auth.models import AbstractUser

# Модель пользователя
class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'Обычный пользователь'),
        ('admin', 'Администратор'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='ticketsite_user_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='ticketsite_user_set',
        related_query_name='user',
    )

    def __str__(self):
        return self.username
    
# Города
class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Места проведения
class Place(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.city})"

# Мероприятия
class Event(models.Model):
    TYPE_CHOICES = [
        ('cinema', 'Кино'),
        ('theatre', 'Театр'),
        ('concert', 'Концерт'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)  
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    date_time = models.DateTimeField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/', blank=True, null=True)  
    min_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.get_type_display()})"
    
    def get_type_icon(self):
        icons = {
            'cinema': '🎬',
            'theatre': '🎭',
            'concert': '🎵'
        }
        return icons.get(self.type, '')

# Билеты
class Ticket(models.Model):
    STATUS_CHOICES = [
        ('available', 'Доступен'),
        ('booked', 'Забронирован'),
        ('sold', 'Продан'),
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"Билет на {self.event} (место {self.seat_number})"

# Заказы
class Order(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Ожидает оплаты'),
        ('paid', 'Оплачен'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Заказ #{self.id} ({self.user.username})"
