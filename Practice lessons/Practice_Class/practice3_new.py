
"""12. Написати клас ForumUser (користувач форуму). Користувач форуму ідентифікується ніком, уміє
писати повідомлення та знає кількість власних повідомлень. Користувач з порожнім іменем не
допускається (замість порожнього імені слід використовувати "noname"). Анонім писати повідомлення
не може."""

"""14. Передбачити, що користувачі бувають забанені (на певну кількість повідомлень). Для забаненого
користувача написання повідомлень неможливе, але на кожну спробу написати на 1 зменшується бан."""


class ForumUser:
    def __init__(self, nickname='noname', messages=None):
        self.validate_nickname(nickname)
        self.nickname = nickname
        self.messages = messages if messages else []
        self.message_count = len(self.messages)
        self.banned_messages = 0

    @classmethod
    def validate_nickname(cls, nickname):
        if "'" in nickname or '"' in nickname:
            raise ValueError("""Error in ForumUser: nickname contains ' or " """)
        if not nickname[0].isalpha():
            raise ValueError('Error in ForumUser: nickname[0] is not alpha')

    def get_ban(self, value=3):
        self.banned_messages = value
        return value

    def write_message(self, message, user):
        if self.banned_messages > 0:
            self.banned_messages -= 1
            return 'you are banned'
        if self.nickname != 'noname':
            user.messages.append(message)
            user.message_count += 1
            return message
        else:
            return 'error'

    def __repr__(self):
        return f'{type(self).__name__} ({self.nickname = }; {self.messages = })'


"""15. Написати клас Admin, що є похідним від ForumUser. Адміністратор може писати повідомлення, не
зважаючи на бан. Нік адміністратора повинен починатися з літери 'A'."""


class Admin(ForumUser):
    def __init__(self, nickname = 'noname'):
        super().__init__(nickname = nickname)

    @classmethod
    def validate_nickname(cls, nickname):
        if nickname[0] != 'A':
            raise ValueError('error in Admin: nickname[0] must be "A"')
        ForumUser.validate_nickname(nickname)

    # def __repr__(self):
    #     return f'Admin({self.nickname = }; {self.messages = })'

"""17. Написати функцію, що сортує список користувачів форуму (див. клас ForumUser) спочатку за
спаданням кількості повідомлень, а в межах однакової кількості за їх ніками (за зростанням)."""

def sortUsers(user_list: list[Admin | ForumUser]):
    user_list.sort(key=lambda user: (-user.message_count, user.nickname))
    return user_list

u1 = Admin("A_Andrii")
u2 = ForumUser("Max")
u3 = ForumUser("Nazarii")
u4 = ForumUser("Dima")
u1.write_message("hello", u2)
u1.write_message("hello2", u2)
u1.write_message("hello3", u2)
u2.write_message("how are you", u2)
u2.write_message("how are you2", u2)
u3.write_message("how are", u3)
users = [u1, u3, u2, u4]

print(*sortUsers(users), sep='\n')