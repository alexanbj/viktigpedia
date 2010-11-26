from django.conf import settings

from minidetector.useragents import search_strings

class Middleware(object):
    @staticmethod
    def process_request(request):
        """ Adds a "mobile" attribute to the request which is True or False
            depending on whether the request should be considered to come from a
            small-screen device such as a phone or a PDA"""
        
        if request.META.has_key("HTTP_X_OPERAMINI_FEATURES"):
            #Then it's running opera mini. 'Nuff said.
            #Reference from:
            # http://dev.opera.com/articles/view/opera-mini-request-headers/
            request.mobile = True
            return None
        
        if request.META.has_key("HTTP_ACCEPT"):
            s = request.META["HTTP_ACCEPT"].lower()
            if 'application/vnd.wap.xhtml+xml' in s:
                # Then it's a wap browser
                request.mobile = True
                request.wap = True
                
                return None
        
        if request.META.has_key("HTTP_USER_AGENT"):
            # This takes the most processing. Surprisingly enough, when I
            # Experimented on my own machine, this was the most efficient
            # algorithm. Certainly more so than regexes.
            # Also, Caching didn't help much, with real-world caches.
            s = request.META["HTTP_USER_AGENT"].lower()
            
            if 'applewebkit' in s:
                request.browser_is_webkit = True
            
            # some special checks for 'important' devices
            if 'ipad' in s:
                request.browser_is_ipad = True
                request.browser_is_ios = True
                
                request.mobile_device = 'ipad'
                request.touch_device = True
                request.wide_device = True
                
                # toggle setting for deciding if ipad is mobile or not
                request.mobile = getattr(settings, 'IPAD_IS_MOBILE', False)
                return None
            if 'iphone' in s or 'ipod' in s:
                request.browser_is_iphone = True
                request.browser_is_ios = True
                
                request.mobile_device = 'iphone'
                request.touch_device = True
                request.wide_device = False
                
                # toggle setting for deciding if iphone is mobile or not
                request.mobile = getattr(settings, 'IPHONE_IS_MOBILE', True)
            if 'android' in s:
                request.browser_is_android = True
                
                request.mobile_device = 'android'
                request.touch_device = True
                request.wide_device = False
                
                # toggle setting for deciding if iphone is mobile or not
                request.mobile = getattr(settings, 'ANDROID_IS_MOBILE', True)
            
            for ua in search_strings:
                if ua in s:
                    request.mobile = True
                    return None
        
        # desktop defaults
        request.mobile = False
        request.touch_device = False
        request.wide_device = True
        
        return None

def detect_mobile(view):
    """ View Decorator that adds a "mobile" attribute to the request which is
        True or False depending on whether the request should be considered
        to come from a small-screen device such as a phone or a PDA"""
    
    def detected(request, *args, **kwargs):
        middleware.process_request(request)
        return view(request, *args, **kwargs)
    detected.__doc__ = "%s\n[Wrapped by detect_mobile which detects if the request is from a phone]" % view.__doc__
    return detected

__all__ = ['Middleware', 'detect_mobile']