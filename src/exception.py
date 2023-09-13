import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frmae.f_code.co_filename
    error_meassage="Error occured in python script name[{0}] line nmber [{1}] error message[{2}]".format()
    file_name,exc_tb.tb_lineno,str(error)
    
    return error_meassage

class CustomException(Exception):
    def __inti__(self,error_meesage, error_detail:sys):
        super().__init__(error_meesage)
        self.error_message = error_message_detail(error_meesage, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    
if __name__ == "_main_":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)

    
    
    