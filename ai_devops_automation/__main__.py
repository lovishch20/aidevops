from ai_devops_automation.app import createPipeline
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", help="Json file which contains user inputs")
    parser.add_argument("operation", help="Operations Like Create or Update pipeline")
    args = parser.parse_args()

    createPipeline(args)

class Main:
    if __name__ == '__main__':
        main()
