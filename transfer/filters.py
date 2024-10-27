from transfer.models import TransferEvent


def get_transfer_events_filter(request):
    """
    Generate filter criteria for TransferEvent queryset based on the provided request parameters.
    """
    filters = {}

    token_id = request.query_params.get('token_id')
    to_address = request.query_params.get('to_address')
    from_address = request.query_params.get('from_address')

    if token_id:
        filters['token_id'] = token_id

    if to_address:
        filters['to_address'] = to_address

    if from_address:
        filters['from_address'] = from_address

    return filters
