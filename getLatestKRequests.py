def getLatestKRequests(requests, k):
    result = []
    recent_requests = set()
    i = len(requests) - 1

    while i >= 0 and k > 0:
        if requests[i] not in recent_requests:
            recent_requests.add(requests[i])
            result.append(requests[i])
            k -= 1
        i -= 1

    result.reverse()
    return result
