from django.contrib import admin

from api.models import Movie, Rating

# Register your models here.

admin.site.site_header = "Movie Rater App Corporate"
admin.site.site_title = "Movie Go"
admin.site.index_title = "Welcome to the Movie Go Admin Area"

#admin.site.register(Movie)
admin.site.register(Rating)



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ['title', 'description' , 'num_stars', 'avg_rating']
    list_filter= ['title']
    search_fields = ['title']



