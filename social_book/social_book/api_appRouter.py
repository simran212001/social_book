class api_appRouter:    

    def db_for_read(self, model, **hints):
            """
            Attempts to read auth and contenttypes models go to self.db_name.
            """
            if model._meta.app_label =='api_app':
                return 'api_app'
            return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to self.db_name.
        """
        if model._meta.app_label =='api_app':
            return 'api_app'
        
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if obj1._meta.app_label =='api_app' and obj2._meta.app_label =='api_app':
        
            return 'api_app'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        self.db_name database.
        """
        if app_label =='api_app':
            return 'api_app'
        return None