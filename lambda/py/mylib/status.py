
class BaseStatus:
    def __init__(self,basic_param,var_param,training_param):
        self.LIMIT_PARAM            = 999
        self.LOWER_LIMIT_PARAM      = 0
        self.basic_param            = basic_param
        self.var_param              = var_param
        self.training_param         = training_param
        self.max_param              = basic_param + training_param

    def basic_param_up(self,increase_val):
        tmp_param = self.basic_param
        self.basic_param += increase_val
        self.basic_param = self.LIMIT_PARAM if self.max_param > self.LIMIT_PARAM else self.basic_param
        result_val = self.basic_param - tmp_param
     
        return(result_val)
        
    def basic_param_down(self,increase_val):
        tmp_param = self.basic_param
        self.basic_param -= increase_val
        self.basic_param = self.MIN_PARAM if self.max_param > self.MIN_PARAM else self.basic_param
        result_val = tmp_param - self.basic_param
     
        return(result_val)
        
    def var_param_up(self,increase_val):
        tmp_param = self.var_param
        self.var_param += increase_val
        self.var_param = self.basic_param if self.var_param > self.basic_param else self.var_param
        result_val = self.var_param - tmp_param
    
        return(result_val)
        
    def var_param_down(self,increase_val):
        tmp_param = self.var_param
        self.var_param -= increase_val
        self.var_param = self.MIN_PARAM if self.var_param < self.MIN_PARAM else self.var_param
        result_val = tmp_param - self.var_param
    
        return(result_val)
        

class LifeStatus(BaseStatus):
    def commit_param(self,status_dict):
        my_status = status_dict["parameter"]["my_status"]
        my_status["basic_status"]["basic_life"]         = self.basic_param
        my_status["var_status"]["var_life"]             = self.var_param
        my_status["training_status"]["training_life"]   = self.training_param
    
        return(my_status)

class PowerStatus(BaseStatus):
    def commit_param(self,status_dict):
        my_status = status_dict["parameter"]["my_status"]
        my_status["basic_status"]["basic_power"]        = self.basic_param
        my_status["var_status"]["var_power"]            = self.var_param
        my_status["training_status"]["training_power"]  = self.training_param

        return(my_status)

class DefenceStatus(BaseStatus):
    def commit_param(self,status_dict):
        my_status = status_dict["parameter"]["my_status"]
        my_status["basic_status"]["basic_defence"]       = self.basic_param
        my_status["var_status"]["var_defence"]           = self.var_param
        my_status["training_status"]["training_defence"] = self.training_param

        return(my_status)
