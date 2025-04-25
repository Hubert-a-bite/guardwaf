import re

NGINX_REGEX = re.compile(r'^\d+\.\d+\.\d+\.\d+ - - \[[^\]]+\] ".*?" \d+ \d+ ".*?" ".*?"$')
APACHE_REGEX = re.compile(r'^\d+\.\d+\.\d+\.\d+ - \S+ \[[^\]]+\] ".*?" \d+ \d+ ".*?" ".*?"$')

def detect_log_type(line: str) -> str:
    if NGINX_REGEX.match(line):
        return "nginx"
    elif APACHE_REGEX.match(line):
        return "apache"
    return "unknown"
