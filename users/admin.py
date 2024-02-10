from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'avatar',)


@admin.register(Payment)
class AdminPayment(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'course', 'lesson', 'amount',)
