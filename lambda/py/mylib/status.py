
class BaseStatus:
    def __init__(self,basic_param,var_param,training_param):
        self.LIMIT_PARAM            = 999
        self.LOWER_LIMIT_PARAM      = 0
        self.TRAINING_LIMIT_PARAM   = 300
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
        self.var_param = self.max_param if self.var_param > self.max_param else self.var_param
        result_val = self.var_param - tmp_param
    
        return(result_val)
        
    def var_param_down(self,increase_val):
        tmp_param = self.var_param
        self.var_param -= increase_val
        self.var_param = self.MIN_PARAM if self.var_param < self.MIN_PARAM else self.var_param
        result_val = tmp_param - self.var_param
    
        return(result_val)

    def training_param_up(self,increase_val):
        tmp_param = self.training_param
        self.training_param += increase_val
        self.training_param = self.TRAINING_LIMIT_PARAM if self.training_param > self.TRAINING_LIMIT_PARAM else self.training_param
        result_val = self.training_param - tmp_param
     
        return(result_val)
        
    def training_param_down(self,increase_val):
        tmp_param = self.training_param
        self.training_param -= increase_val
        self.training_param = self.MIN_PARAM if self.training_param > self.MIN_PARAM else self.training_param
        result_val = tmp_param - self.training_param
     
        return(result_val)
        

class LifeStatus(BaseStatus):
    def commit_param(self,status_dict):
        my_status_dict = status_dict["parameter"]["my_status"]
        my_status_dict["basic_status"]["basic_life"]         = self.basic_param
        my_status_dict["var_status"]["var_life"]             = self.var_param
        my_status_dict["training_status"]["training_life"]   = self.training_param
        status_dict["parameter"]["my_status"]                = my_status_dict

        return(status_dict)

class PowerStatus(BaseStatus):
    def commit_param(self,status_dict):
        my_status_dict = status_dict["parameter"]["my_status"]
        my_status_dict["basic_status"]["basic_power"]        = self.basic_param
        my_status_dict["var_status"]["var_power"]            = self.var_param
        my_status_dict["training_status"]["training_power"]  = self.training_param
        status_dict["parameter"]["my_status"]                = my_status_dict

        return(status_dict)

class DefenceStatus(BaseStatus):
    def commit_param(self,status_dict):
        my_status_dict = status_dict["parameter"]["my_status"]
        my_status_dict["basic_status"]["basic_defence"]       = self.basic_param
        my_status_dict["var_status"]["var_defence"]           = self.var_param
        my_status_dict["training_status"]["training_defence"] = self.training_param
        status_dict["parameter"]["my_status"]                 = my_status_dict

        return(status_dict)

class charCreate:
    def __init__(self,status_dict):

        my_status_dict      = status_dict["parameter"]["my_status"]

        basic_dict          = my_status_dict["basic_status"]
        var_dict            = my_status_dict["var_status"]
        training_dict       = my_status_dict["training_status"]

        basic_life          = basic_dict["basic_life"]
        basic_power         = basic_dict["basic_power"]
        basic_defence       = basic_dict["basic_defence"]

        var_life            = var_dict["var_life"]
        var_power           = var_dict["var_power"]
        var_defence         = var_dict["var_defence"]

        training_life       = training_dict["training_life"]
        training_power      = training_dict["training_power"]
        training_defence    = training_dict["training_defence"]

        self.life = LifeStatus(basic_life,var_life,training_life)
        self.power = PowerStatus(basic_power,var_power,training_power)
        self.defence = DefenceStatus(basic_defence,var_defence,training_defence)