class Post: #first Post class
    def postFacebook(self):
        #post something on Facebook.
        #api - GET_POST_FACEBOOK(id, page_name) #calls other method/function with more code
        pass

    def postTwitter(self):
        #post something on Twitter.
        pass

    def postInstagram(self):
        #post something on Instagram
        pass

    def postYoutube(self):
        #Post something on Youtube
        pass

class Post2:
    def postToSocial(self,content,socialMedia):
        if socialMedia == "Facebook":
            postToFacebook()#psuedo function

post1 = Post()
post1.postFacebook("#postoftheday")

class notUserWorthy:
    def backEndFunction(self):
        pass
        #some function na maraming nangyayari

class userWorthy:
    nUW = notUserWorthy() #calls notUserWorthy class
    def functions(self):
        nUW.backEndFunction() #calls backEndFunction from notUserWorth class

run = userWorthy()
run.functions()
    


