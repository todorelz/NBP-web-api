def get_currency_rates(exchange_rate_response_data: list[dict]):
    return exchange_rate_response_data[-1].get("rates")