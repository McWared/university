class A:
    def doact(self):
        print('from A')
class B(A):
    pass
class C(A):
    pass
class D(C, B):
    pass

# obj = D()
# obj.doact()
# print(D.mro()) # Посмотреть последовательность унаследования

"""12. Написати клас ForumUser (користувач форуму). Користувач форуму ідентифікується ніком, уміє
писати повідомлення та знає кількість власних повідомлень. Користувач з порожнім іменем не
допускається (замість порожнього імені слід використовувати "noname"). Анонім писати повідомлення
не може."""
"""13. Модифікувати клас ForumUser, додавши обмеження на нік: має починатися з літери та не містить
лапок."""
"""14. Передбачити, що користувачі бувають забанені (на певну кількість повідомлень). Для забаненого
користувача написання повідомлень неможливе, але на кожну спробу написати на 1 зменшується бан."""

"""15. Написати клас Admin, що є похідним від ForumUser. Адміністратор може писати повідомлення, не
зважаючи на бан. Нік адміністратора повинен починатися з літери 'A'."""
"""16. До системи класів ForumUser-Admin додати метод «забанити». Передбачити, що 1) банити може
тільки адмін або користувач, в якого більше 10000 повідомлень; 2) адміна забанити не можна; 3) коли
користувача забанюють, лічильник його повідомлень обнулюється."""

class ForumUser:
    def __init__(self, nickname = 'noname', mess: list=[]):
        self.validate_nickname(nickname)
        self.nickname = nickname
        self.mess = mess
        self.message_count = len(mess)
        self.banned_messages = 0
        self.isAdmin = False

    @classmethod
    def validate_nickname(cls, nickname):
        if "'" in nickname or '"' in nickname:
            raise ValueError('error you have " in nickname')
        if not nickname[0].isalpha():
            raise ValueError('error your first symbol isnt alpha')

    def __repr__(self):
        return f"{self.nickname} = nickname  {self.mess} = mess  {self.message_count} = messagecount"

    def give_ban(self, user, value = 3):
        if self.message_count < 10000:
            print('You can not ban another users, rou have less then 10k messages')
        if user.isAdmin == False:
            user.banned_messages = value
            user.message_count = 0
            return value
        else:
            print('You can not ban Admin')
    
    def write_message(self, message, user):
        if self.banned_messages != 0:
            self.banned_messages -= 1
            return 'you are banned'
        if self.nickname != 'noname':
            user.mess.append(message)
            user.message_count += 1
            return message
        else:
            return 'error'

class Admin(ForumUser):
    def __init__(self, nickname='noname', mess: list = []):
        super().__init__(nickname, mess)
        self.isAdmin = True

    @classmethod
    def validate_nickname(cls, nickname):
        if nickname[0] != 'A':
            raise ValueError('error in Admin nickname')
        ForumUser.validate_nickname(nickname)
        
    def give_ban(self, user, value = 3):
        if user.isAdmin == False:
            user.banned_messages = value
            user.message_count = 0
            return value
        else:
            print('You can not ban Admin')
    
    def __repr__(self):
        return f'Admin({self.nickname = }; {self.mess = })'

adm1 = Admin('AKolya')
obg1 = ForumUser('Andrew')
obg2 = ForumUser('Maks')
obg1.give_ban(adm1, 1)
obg2.give_ban(obg1, 1)
adm1.write_message('hello', obg2)
print(adm1)
print(obg1)
print(obg2)