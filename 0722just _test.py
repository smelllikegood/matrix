class PoM_Exception(Exception):
    pass
class Time_Exception(Exception):
    pass
class Mode_Exception(Exception):
    pass
class Matrix():
    def __init__(self):
        import random
        self.ar=int(input("enter matrix A rows:  "))
        self.ac=int(input("enter matrix A clns:  "))
        self.br=int(input("enter matrix B rows:  "))
        self.bc=int(input("enter matrix B clns:  "))
        self.mark=input("which type of calculate would you choose   (plus+/minus-/times*)   :")    #times 包含trans
            
    def init_ma(self):
        import random
        self.ma_a=[]
        [self.ma_a.append([0]*self.ac)for j in range(self.ar)]
        for i in range (self.ar):
            for j in range(self.ac):
                self.ma_a[i][j]=random.randint(0,9)

        self.ma_b=[]
        [self.ma_b.append([0]*self.bc)for j in range(self.br)]
        for i in range (self.br):
            for j in range(self.bc):
                self.ma_b[i][j]=random.randint(0,9)

        print("the random A matrix is :")
        for i in range (self.ar):print(self.ma_a[i])
        print("-"*20)

        print("the random B matrix is :")
        for i in range (self.br): print(self.ma_b[i])
        print("-"*20)
    def judge(self):
        
        if (self.mark=='plus' or self.mark=='minus'):
            if ((self.ar==self.br)and (self.ac==self.bc)):
                return True
            else :
                return False
        elif (self.mark=='times'):
            if (self.ac==self.br):
                return True
            else :
                return False
        else:
            return True
    def cal(self):
        self.init_ma()
        try :
            if self.mark=='plus':
                if self.judge()==False:
                    raise PoM_Exception()
                else :
                    self.ma_plus= self.ma_a[:]
                    lens= [0]*self.ac                            #排版
                    for i in range (self.br):
                        for j in range (self.bc):
                            self.ma_plus[i][j]+=self.ma_b[i][j]

                            if len(str(self.ma_plus[i][j]))>lens[j]:
                                lens[j]=len(str(self.ma_plus[i][j]))

                    print(" A + B = :\n")
                    for i in range(self.ar):
                        for j in range(self.ac): 
                            if (j!=self.ac-1):
                                print(str(self.ma_a[i][j]).rjust(lens[j]),end=' ')
                            else:
                                print(str(self.ma_a[i][j]).rjust(lens[j]))
                    # for k in range (self.ar):print(self.ma_plus[k])
                    print('-'*20)


            elif self.mark=='minus':
                if self.judge()==False:
                    raise PoM_Exception()
                else :
                    self.ma_minus=self.ma_a[:]
                    lens= [0]*self.ac                            #排版
                    for i in range (self.br):
                        for j in range (self.bc):
                            self.ma_minus[i][j]-=self.ma_b[i][j]

                            if len(str(self.ma_minus[i][j]))>lens[j]:
                                lens[j]=len(str(self.ma_minus[i][j]))

                    print(" A - B = :\n")
                    for i in range(self.ar):
                        for j in range(self.ac): 
                            if (j!=self.ac-1):
                                print(str(self.ma_a[i][j]).rjust(lens[j]),end=' ')
                            else:
                                print(str(self.ma_a[i][j]).rjust(lens[j]))

            elif self.mark=='times':
                if self.judge()==False :
                    raise Time_Exception()
                else:
                    self.ma_time=[]
                    [self.ma_time.append([0]*self.bc)for i in range(self.ar)]
                    print(" A * B = :\n")

                    lens= [0]*self.bc
                    for i in range(self.ar):
                        for j in range(self.bc):
                            temp=0
                            for k in range(self.ac):
                                temp+=self.ma_a[i][k]*self.ma_b[k][j]
                            self.ma_time[i][j]+=temp
                            if len(str(self.ma_time[i][j]))>lens[j]:
                                lens[j]=len(str(self.ma_time[i][j]))
                    for i in range(self.ar):
                        for j in range(self.bc): 
                            if (j!=self.bc-1):
                                print(str(self.ma_time[i][j]).rjust(lens[j]),end=' ')
                            else:
                                print(str(self.ma_time[i][j]).rjust(lens[j]))
                    print('-'*20)



                    print("transpose of A * B is   :\n")
                    self.ma_trans=[]
                    [self.ma_trans.append([0]*self.ar)for i in range(self.bc)]
                    lens= [0]*self.ar
                    for i in range (self.bc):
                        for j in range(self.ar):
                            self.ma_trans[i][j]+=self.ma_time[j][i]
                            if len(str(self.ma_trans[i][j]))>lens[j]:
                                lens[j]=len(str(self.ma_trans[i][j]))

                    for i in range(self.bc):
                        for j in range(self.ar): 
                            if (j!=self.ar-1):
                                print(str(self.ma_trans[i][j]).rjust(lens[j]),end=' ')
                            else:
                                print(str(self.ma_trans[i][j]).rjust(lens[j]))
                    print('-'*20)
            else:
                raise Mode_Exception

        except Mode_Exception as e:
            print("choose correct mode !!! idiot")
        except PoM_Exception as e :
            print("None\nsize wrong ! \nboth rows and clns should be the same ~~ ")   
        except Time_Exception as e :
            print("None\nsize wrong ! \nA 's  clns should be equal to B 's rows ~~")
x=Matrix()
x.cal() 