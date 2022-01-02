import dj_database_url
from .settings import * # 含入原本的settings.py所有設定
# heroku使用的資料庫為PostgreSQL，所以要修改資料庫設定
DATABASES = {
    'default': dj_database_url.config(),
}
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # 設定HTTP連線方式
ALLOWED_HOSTS = ['*'] # 讓所有的網域都能瀏覽本網站
DEBUG = False # 關閉除錯模式