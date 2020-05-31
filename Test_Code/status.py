# coding: utf-8
# Your code here!

class BaseStatus:
    def __init__(self,basic_param,var_param):
        self.LIMIT_PARAM    = 999
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
    def commit_param(self,status_dict):
        my_status = status_dict["my_status"]
        my_status["basic_life"] = self.basic_param
        my_status["var_life"] = self.var_param

        return(my_status)

class PowerStatus(BaseStatus):
    pass

class DefenceStatus(BaseStatus):
    pass

class test():
    @classmethod
    def test_method(self):
        my_char = charCreate(
            basic_life    = 100,
            basic_power   = 100,
            basic_defence = 100,
            var_life      = 100,
            var_power     = 100,
            var_defence   = 100,
            )


if __name__ == "__main__":

    def commit_test():
        pers_attr = {"my_status":{
            "basic_life":100,
            "var_life":100,
            "basic_pawer":100,
            "var_power":100,
            "basic_defence":100,
            "var_defence":100
        }}

        s = pers_attr["my_status"]

        print("***********************")
        print (pers_attr)
        print("***********************")

        userLife=LifeStatus(s["basic_life"],s["var_life"])

        print("{}".format(userLife.var_param))
        print("-----------------------")
        print("パラメータUP     ：{}".format(userLife.param_down(8)))
        print("MAXパラメータ    ：{}".format(userLife.basic_param))
        print("パラメータ       ：{}".format(userLife.var_param))
        print("-----------------------")
        print("パラメータ       ：{}".format(userLife.commit_param(pers_attr)))

    def method_test():
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

    method_test()