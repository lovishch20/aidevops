''' This script is for automating the process of building pipeline using Dvc. Whenever a new code and data is received a new
    pipeline is created from scratch, and if there is any updation in code or data files the pipeline will be reproduced.
'''
from os import path
import logging
import os
from datetime import datetime

from ai_devops_automation.src.automationService import gitIgnore,gitCommands,dataAndCodeInfo,checkForUpdates
from ai_devops_automation.src import dvcSteps
from ai_devops_automation.src import Constants

dirname = os.path.dirname(__file__)
file_date = datetime.now().strftime("%Y_%m_%d_%H")
filename = os.path.join(dirname, 'log/ai-devops-automation'+file_date+'.log')
logging.basicConfig(filename=filename, filemode='a',
                    format="%(asctime)s:%(levelname)s:%(message)s",
                    level=logging.INFO)
logger = logging.getLogger(__name__)

#Create a DVC pipeline for model generation and deployment

def createPipeline(args):

    Dvcfile_existence = path.exists(Constants.DVC_FILE)

    config = args.config_file
    operation = args.operation
    logger.info("Starting pipeline creation for operation::%s", operation)

    if operation == Constants.CREATE_OPERATION:

        if not Dvcfile_existence:
            print('\033[1m'+"\n****Got new Code, Started Building Pipeline****\n"+'\033[0m')
            logger.info("Creating new pipeline")

            #Dvc Initialization Steps
            dvcSteps.initialization()

            #Dvc Pipeline Building
            dvcSteps.dvcRepro()

            # Dvc Push Data
            dvcSteps.pushData()

            # Set gitIgnore and git Remote
            gitIgnore()

            # Run git Comamnds like status, commit, tag, push
            gitCommands()
            # Store data and code checksum info
            dataAndCodeInfo()
        else:
            print("DVC file already exists.")
            logger.info("DVC file already exists")
            exit(0)

    elif operation == Constants.UPDATE_OPERATION :
        if Dvcfile_existence:
            print("\033[1m\n****Checking for updates****\033[0m\n")
            logger.info("DVC file already exists , updating the file")
            #Check if there is any change in data or code, and push the changes to github and dvc remote.
            checkForUpdates()
        else:
            print("\033[1m\n****Dvcfile does not exist, create a new pipeline****\033[0m\n")
            logger.info("DVC file does not exists ,can not perform update operation")
    else:
        logger.error("Invalid operation %s", operation)
        exit(1)


























