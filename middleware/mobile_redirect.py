from django.http import HttpResponseRedirect

MOBILE_URL = 'http://localhost:8001/'

class MobileRedirect():
    def process_request(self, request):
        # Check user agent
        if not request.session.get('checked_ua', False):

            if request.mobile:
                request.session['checked_ua'] = True
                # Expire cookie on browser close
                request.session.set_expiry(0)
                return HttpResponseRedirect(MOBILE_URL)

        else: # Skip the check next time. Allows mobile users to browse normal
            # site if they want to
            request.session['checked_ua'] = True
            # Expire cookie on browser close
            request.session.set_expiry(0)
            return None
