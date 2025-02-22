def beauty_func_name(name:str):
    return name.replace('_', " ").title()


def step(fn):

    def fn_with_log(*args, **kwargs):
        (print(f'{beauty_func_name(fn.__name__)} : {"".join( f"{k} = {v}" for k,v in kwargs.items())}') if kwargs else
        print( f'{beauty_func_name(fn.__name__)} : {"".join(args[1:])}') if len(args) > 1 else
        print(beauty_func_name(fn.__name__)))
    return fn_with_log


@step
def given_sing_up_form_opened():
    pass


class SignUpForm:
    @step
    def fill_email(self, value):
        pass

    @step
    def fill_password(self, value):
        pass

    @step
    def submit(self):
        pass


class DashBoard:
    @step
    def go_to_profile(self):
        pass


sign_up_form = SignUpForm()
dashboard = DashBoard()


given_sing_up_form_opened()
sign_up_form.fill_email('larra12@ya.ru')
sign_up_form.fill_password(value='123123')
sign_up_form.submit()
dashboard.go_to_profile()