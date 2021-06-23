"""Constants for the duckdns_ipv4_ipv6 integration."""
from datetime import timedelta

DOMAIN = "duckdns_ipv4_ipv6"

INTERVAL = timedelta(minutes=5)

CONF_HOSTNAME = "hostname"
CONF_IPV4_MODE = "ipv4_mode"
CONF_IPV6_MODE = "ipv6_mode"
CONF_IPV4_RESOLVER = "ipv4_resolver"
CONF_IPV6_RESOLVER = "ipv6_resolver"

UPDATE_URL = "https://www.duckdns.org/update"
DEFAULT_HOSTNAME = "myip.opendns.com"
DEFAULT_IPV4_MODE = "off"
DEFAULT_IPV6_MODE = "off"
DEFAULT_IPV4_RESOLVER = "208.67.222.222"
DEFAULT_IPV6_RESOLVER = "2620:0:ccc::2"

SERVICE_SET_TXT = "set_txt"
ATTR_TXT = "txt"

SERVICE_UPDATE_IP = "update_ip"
ATTR_HOSTNAME = "hostname"
ATTR_IPV4_MODE = "ipv4_mode"
ATTR_IPV6_MODE = "ipv6_mode"
ATTR_IPV4_RESOLVER = "ipv4_resolver"
ATTR_IPV6_RESOLVER = "ipv6_resolver"
ATTR_IPV4_ADDRESS = "ipv4_address"
ATTR_IPV6_ADDRESS = "ipv6_address"