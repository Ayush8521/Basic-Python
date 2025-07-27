def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal server Error"
        case _:
            return "Unknown status"
        # usage print(http_status(200))  # Output: OK
# usage print(http_status(404))  # Output: Not Found
# usage print(http_status(500))  # Output: Internal server Error

print(http_status(5007))