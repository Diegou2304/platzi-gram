from django.contrib import admin
from users.models import Profile
# Register your models here.
#Podemos registarlo asi, pero para añadir al admin mas opciones
#Haremos una clase
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user','phone_number','website','picture')
    #Nos lleva al detalle desde esos campos
    #list_display_links = ('user')

    #Nos permite editar
    list_editable = ('phone_number','website')
    #Para busquedas
    search_fields = (
        'phone_number',
        'website',
        'user__first_name',
        'user__last_name',
        'user__username'

    )

    #Para filtrar
    list_filter = ('created','modified','website','user__is_staff')




