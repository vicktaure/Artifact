import time

def execute(action, *args):
    result = action(*args)
    if result and "data" in result:
        time.sleep(result["data"]["cooldown"]["total_seconds"])
    return result