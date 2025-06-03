from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.html import format_html

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image', 'type', 'date_time', 'place', 'min_price')
    list_filter = ('type', 'place__city', 'date_time')
    search_fields = ('title', 'description', 'place__name')
    readonly_fields = ('display_image',)
    fieldsets = (
        (None, {
            'fields': ('title', 'type', 'description', 'short_description')
        }),
        ('Дата и место', {
            'fields': ('date_time', 'place')
        }),
        ('Изображение и цена', {
            'fields': ('image', 'display_image', 'min_price')
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" />', obj.image.url)
        return "Нет изображения"
    display_image.short_description = 'Превью'

class TicketAdmin(admin.ModelAdmin):
    list_display = ('event', 'row', 'seat_no', 'price', 'status', 'order_link')
    list_filter = ('event', 'status', 'event__place')
    search_fields = ('event__title', 'seat_no', 'row')
    raw_id_fields = ('event', 'order')

    def order_link(self, obj):
        if obj.order:
            return format_html(
                '<a href="/admin/ticketsite/order/{}/change/">{}</a>',
                obj.order.id,
                obj.order.id
            )
        return "Нет заказа"
    order_link.short_description = 'Заказ'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'ticket_info', 'order_date', 'payment_status')
    list_filter = ('payment_status', 'order_date')
    search_fields = ('user__username', 'ticket__event__title')
    raw_id_fields = ('user', 'ticket')

    def ticket_info(self, obj):
        return f"{obj.ticket.event.title} (место {obj.ticket.seat_no})"
    ticket_info.short_description = 'Билет'

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address')
    list_filter = ('city',)
    search_fields = ('name', 'address')

admin.site.register(User, UserAdmin)
admin.site.register(City)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Order, OrderAdmin)

admin.site.site_header = "Администрирование билетной системы"
admin.site.site_title = "Билетная система"
admin.site.index_title = "Управление контентом"