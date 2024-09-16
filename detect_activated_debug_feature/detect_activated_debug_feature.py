def detect_activated_debug_feature_noncompliant():
    from django.conf import settings
    settings.configure(DEBUG=True)