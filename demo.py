# from src.logger import logging

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# from src.exception import CustomException
# import sys
# from src.logger import logging

# try:
#     a = 1 / 0
# except Exception as e:  
#     logging.info("We are dividing by zero")
#     raise CustomException(e, sys) from e  

from src.pipeline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()