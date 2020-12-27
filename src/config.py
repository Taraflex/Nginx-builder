import distro
import platform


# Параметры системы
OS_RELEASE = distro.codename().split(' ')[0].lower()
PLATFORM_ARCH = platform.machine()
OS_DISTRIBUTION = distro.id().lower()
OS_VERSION = distro.major_version()

# Адрес загрузки исходного кода nginx
NGINX_URL = "http://nginx.org/download"
NGINX_SRPM_URL_MAINLINE = "http://nginx.org/packages/mainline/centos/{}/SRPMS".format(OS_VERSION)
NGINX_SRPM_URL_STABLE = "http://nginx.org/packages/centos/{}/SRPMS".format(OS_VERSION)

# Архив со скриптами для создания пакета
DEB_PACKAGE_SCRIPTS_URL_MAINLINE = "http://nginx.org/packages/mainline/{}/pool/nginx/n/nginx".format(OS_DISTRIBUTION)
DEB_PACKAGE_SCRIPTS_URL_STABLE = "http://nginx.org/packages/{}/pool/nginx/n/nginx".format(OS_DISTRIBUTION)

# Путь до директории сборки пакета
SRC_PATH = "/usr/src/nginx"

# Error build code
DPKG_FAIL_EXIT_CODE = 29

# Параметры компиляции nginx
DEFAULT_CONFIGURE_PARAMS = [
    "--prefix=/etc/nginx",
    "--sbin-path=/usr/sbin/nginx",
    "--conf-path=/etc/nginx/nginx.conf",
    "--modules-path=/usr/lib/nginx/modules",
    "--error-log-path=/var/log/nginx/error.log",
    "--pid-path=/var/run/nginx.pid",
    "--lock-path=/var/lock/nginx.lock",
    "--http-log-path=/var/log/nginx/access.log",
    "--http-client-body-temp-path=/var/cache/nginx/client_temp",
    "--http-proxy-temp-path=/var/cache/nginx/proxy_temp",
    "--without-http_geo_module",
    "--without-http_autoindex_module",
    "--without-http_empty_gif_module",
    "--without-http_fastcgi_module",
    "--without-http_memcached_module",
    "--without-http_scgi_module",
    "--without-http_split_clients_module",
    "--without-http_uwsgi_module",
    "--with-http_gunzip_module",
    "--with-http_gzip_static_module",
    "--with-http_realip_module",
    "--with-http_ssl_module",
    "--with-pcre-jit",
    "--with-compat",
    "--with-file-aio",
    "--with-threads",
    "--with-stream",
    "--with-stream_ssl_module",
    "--with-cc-opt=\"${CFLAGS}\"",
    "--with-ld-opt=\"${LDFLAGS}\""
]

# Путь к директории с модулями для файла rules
MODULESDIR = 'export MODULESDIR = $(CURDIR)/debian/modules'

# Адрес эл. почты для указания при сборке
EMAIL_CREATOR = "taraflex.red@gmail.com"

# Тип лицензии для указания при сборке
LICENSE_TYPE = "gpl"
