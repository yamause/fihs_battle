# coding: utf-8
# Your code here!

class BaseStatus:
    def __init__(self,basic_param,var_param):
        self.LIMIT_PARAM      = 999
        self.MIN_PARAM      = 0
        self.basic_param    = basic_param
        self.var_param      = var_param
        
    def basic_param_up(self,increase_val):
        tmp_param = self.basic_param
        self.basic_param += increase_val
        self.basic_param = self.LIMIT_PARAM if self.basic_param > self.LIMIT_PARAM else self.basic_param
        result_val = self.basic_param - tmp_param
        return(result_val)
        
    def basic_param_down(self,increase_val):
        tmp_param = self.basic_param
        self.basic_param -= increase_val
        self.basic_param = self.MIN_PARAM if self.basic_param > self.MIN_PARAM else self.basic_param
        result_val = tmp_param - self.basic_param
        return(result_val)
        
    def param_up(self,increase_val):
        tmp_param = self.var_param
        self.var_param += increase_val
        self.var_param = self.basic_param if self.var_param > self.basic_param else self.var_param
        result_val = self.var_param - tmp_param
    
        return(result_val)
        
    def param_down(self,increase_val):
        tmp_param = self.var_param
        self.var_param -= increase_val
        self.var_param = self.MIN_PARAM if self.var_param < self.MIN_PARAM else self.var_param
        result_val = tmp_param - self.var_param
    
        return(result_val)
        

class LifeStatus(BaseStatus):
    pass

class PowerStatus(BaseStatus):
    pass

class DefenceStatus(BaseStatus):
    pass

if __name__ == "__main__":

    user=BaseStatus(100,80)
    print(user.basic_param)
    print(user.var_param)
    print("-----------------------")
    print("パラメータUP     ：{}".format(user.param_up(8)))
    print("MAXパラメータ    ：{}".format(user.basic_param))
    print("パラメータ       ：{}".format(user.var_param))
    print("-----------------------")
    print("パラメータUP     ：{}".format(user.param_up(20)))
    print("MAXパラメータ    ：{}".format(user.basic_param))
    print("パラメータ       ：{}".format(user.var_param))
    print("-----------------------")
    print("パラメータDown   ：{}".format(user.param_down(10)))
    print("MAXパラメータ    ：{}".format(user.basic_param))
    print("パラメータ       ：{}".format(user.var_param))
    print("-----------------------")
    print("パラメータUP     ：{}".format(user.basic_param_up(10)))
    print("MAXパラメータ    ：{}".format(user.basic_param))
    print("パラメータ       ：{}".format(user.var_param))
    print("-----------------------")
    print("パラメータUP     ：{}".format(user.basic_param_up(1000)))
    print("MAXパラメータ    ：{}".format(user.basic_param))
    print("パラメータ       ：{}".format(user.var_param))
    print("-----------------------")