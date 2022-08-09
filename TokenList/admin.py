from django.contrib import admin
from TokenList.models import TokenModel
from TokenList.tools import format_json, update_json,write_json
# Register your models here.
class TokenListAdmin(admin.ModelAdmin):
    list_display = ('channel_id','symbol','decimals','address' )

#admin.site.register(TokenModel, TokenListAdmin)

from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from django.http import HttpResponse, JsonResponse
from django.contrib import admin
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt

class MyModelModelAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ('channel_id','symbol','decimals','address')
    @button(permission='TokenModel',
            change_form=True,
            html_attrs={'style': 'background-color:#88FF88;color:black'})
    def upload(self, request):
        try:
            TokenModel.objects.all().delete()
            update_json()
            self.message_user(request, 'uploaded the file')
        except:
            self.message_user(request, "error while uploading")

        # Optional: returns HttpResponse
        return HttpResponseRedirectToReferrer(request)
    
    @button(html_attrs={'style': 'background-color:#DC6C6C;color:black'})
    def save_json(self, request):
        # def _action(request):
        #     pass
        try:
            write_json()
            self.message_user(request, 'saved called')
        except:
            self.message_user(request, 'Error while saving')

        return HttpResponseRedirectToReferrer(request)
        #return confirm_action(self, request, _action, "Confirm action",
        #                  "Successfully executed", )

    @link(href=None, 
          change_list=False, 
          html_attrs={'target': '_new', 'style': 'background-color:var(--button-bg)'})
    def search_on_google(self, button):
        original = button.context['original']
        button.label = f"Search '{original.name}' on Google"
        button.href = f"https://www.google.com/?q={original.name}"

    @view()
    def select2_autocomplete(self, request):
        return JsonResponse({})

    @view(http_basic_auth=True)
    def api4(self, request):
        return HttpResponse("Basic Authentication allowed")

    @view(decorators=[csrf_exempt, xframe_options_sameorigin])
    def preview(self, request):
        if request.method == "POST":
            return HttpResponse("POST")
        return HttpResponse("GET")

admin.site.register(TokenModel, MyModelModelAdmin)