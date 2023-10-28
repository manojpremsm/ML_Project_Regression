import sys
import os 

def error_message_details(error_msg,error_details):
    _,_,exc_tb = sys.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error_msg))

    return error_message


class custom_error_handler(Exception):
    def __init__(self,error_msg,error_msg_details):
        super().__init__(error_msg)
        self.error_msg_details = error_message_details(error_msg,error_msg_details)

    #def __str__(self):
        #return self.error_msg