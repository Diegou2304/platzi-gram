from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin as BaseUserAdmin
from users.models import Profile
from django.contrib.auth.models import  User
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
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            )
        }),

        ('Extra info',{
            'fields': (
                ('website','phone_number'),
                ('biography')
            )
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        })

    )

    #Para filtrar
    list_filter = ('created','modified','website','user__is_staff')
    #Read only
    readonly_fields = ('created','modified')

# De manera mas ordenada Todo esto sirve apra que se ingrese los datos correspondientes

class ProfileInLine(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',

    )

admin.site.unregister(User)
#El model y la clase
admin.site.register(User,UserAdmin)


