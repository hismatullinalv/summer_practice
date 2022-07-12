from service.service_models import Services_models


def update_end_date():
    ses = Services_models()
    ses.create_objects()
    current_stats = ses.get_objects()
    return current_stats
