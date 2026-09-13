# create_superuser.py
import os

import django
from django.contrib.auth.models import User

# 1. 加载Django环境，必须写在最前面
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
# 配置账号信息
username = "Django123456"
password = "Django123456"

# 判断用户是否存在，避免重复创建报错
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password)
    print(f"✅ 超级管理员 {username} 创建成功")
else:
    print(f"ℹ️ 用户 {username} 已存在，跳过创建")
