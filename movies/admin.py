from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Movies, Tag

class MoviesResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Movies
        fields = ('id', 'rank', 'title', 'image', 'date', 'time', 'content')
        import_id_fields = ('title', )
        skip_unchanged = True
        exclude = ('imported', )
 
@admin.register(Movies)

class MoviesAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    list_display = ('rank', 'title', 'image', 'date', 'time', 'content', 'check', 'score', '_tags' )
    def _tags(self, row):
        return ','.join([x.name for x in row.tags.all()])

    # django-import-exportsの設定
    resource_class = MoviesResource

@admin.register(Tag)

class TagsAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    list_display = ('id', 'name')

# Register your models here.
