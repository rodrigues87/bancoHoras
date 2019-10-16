from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)
#------------------------------------------------------------------
""" main.js (with some code adapted from Django official site)
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== ‘’) {
        var cookies = document.cookie.split(‘;’);
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Check if this cookie string begin with the name we want
            if (cookie.substring(0, name.length + 1) === (name + ‘=’)) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
             }
         }
    }
    return cookieValue;
}
    
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader(“X-CSRFToken”, getCookie(‘csrftoken’));
        }
    }
});
// actual AJAX call
$.ajax({
    method: “POST”,
    url: “/postcodes”,
    contentType: ‘application/json’,
    data: JSON.stringify(input),
    dataType: “json”,
    success: function(data) {
        // do something
    }
 })
    """