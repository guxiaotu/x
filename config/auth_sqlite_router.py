class AuthSqliteRouter:
    """
    用户认证相关表走 SQLite
    其余表走 default（PostgreSQL）
    """

    AUTH_APPS = {
        "auth",
        "contenttypes",
        "sessions",
        "admin",
    }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.AUTH_APPS:
            return "sqlite"
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.AUTH_APPS:
            return "sqlite"
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        # 允许 auth 内部关系
        if (
                obj1._meta.app_label in self.AUTH_APPS and
                obj2._meta.app_label in self.AUTH_APPS
        ):
            return True

        # 允许业务 app 内部关系
        if (
                obj1._meta.app_label not in self.AUTH_APPS and
                obj2._meta.app_label not in self.AUTH_APPS
        ):
            return True

        # 禁止 auth 与业务表跨库关联
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.AUTH_APPS:
            return db == "sqlite"
        return db == "default"
