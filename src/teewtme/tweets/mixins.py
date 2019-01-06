
class UserRequiredMixin(object):
    def form_valid(self,form):
        #import ipdb; ipdb.set_trace()
       
        if self.request.user.is_authenticated():
            form.instance.user=self.request.user
            print("yes")
            return super().form_valid(form)
        else:
            print("no")
            form.add_error(None,"it must be user")
            return super().form_invalid(form) 

class UserownerMixin(UserRequiredMixin,object):
    def form_valid(self,form):
        if self.request.user==form.instance.user:
            #print ("yes")
            return super().form_valid(form)

        else:
            #print ("no")
            form.add_error(None,"this user is not allowed to change")
            return self.form_invalid(form)
