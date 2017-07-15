class pikalist(list) :
    #pikalist can't have a sex, not like pikachu -''-
    def __init__(self, n=0) :
        super().__init__(self)
        self.append_sequence(n)
        self.append('pika')
        self.append('pika')
        
    def append_sequence(self, n=0) :
        for i in range(n) :
            self.append(i)
        
    def remove_odd_items(self) :
        #this is one of the way to copy a list
        #if we only do copy = self, any mutation happened to self
        #will affect copy too and that ruins the process
        copy = self[:]
        
        for each in copy :
            if type(each) is int and each%2 == 1 :
                self.remove(each)

    def remove_string_items(self) :
        #same comment as above
        copy = self[:]
        
        for each in copy :
            if type(each) is str :
                self.remove(each)


