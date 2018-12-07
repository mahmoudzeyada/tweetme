
class UserRequiredMixin(object):
    def form_vaild(self,form):
        if self.request.user.is_authenticated():
            form.instance.created_by=self.request.user
            return super().form_vaild(form)
        else:
            form.add_error(None,"it must be user")
            return super().form_invaild(form)


class UserownerMixin(UserRequiredMixin , object):
    def form_valid(self,form):
        if self.request.user==form.instance.user:
            #print ("yes")
            return super().form_valid(form)

        else:
            #print ("no")
            form.add_error(None,"this user is not allowed to change")
            return self.form_invalid(form)
