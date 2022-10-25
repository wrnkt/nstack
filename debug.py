import pstats
import cProfile

def time_me(func):
    def wrapper(*args, **kwargs):
        with cProfile.Profile() as pr:
            res = func(*args, **kwargs)
        stats = pstats.Stats(pr)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        stats.dump_stats(filename=f"[LOG]: profiling {func.__name__}")
        return res
    return wrapper


def log_info(debugmode:bool = False):
    def wrapper(*args, **kwargs):
        if (debugmode):
            print(f"[LOG] calling {func.__name__}")
        res = func(*args, **kwargs)
        return res
    return wrapper
