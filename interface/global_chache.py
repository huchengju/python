class User(object):

    def __init__(self, email):
        self.email = email


class GlobalCache(object):

    def __init__(self):

        self._user = None

    def set_user_cache(self, u):
        self._user = u

    @property
    def user(self):
        return self._user

global_cache = GlobalCache()


if __name__ == '__main__':

    user = User("abc@example.com")

    global_cache.set_user_cache(user)

    # get user from cache

    _user = global_cache.user
