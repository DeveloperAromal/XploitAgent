from tools.runner import start_tools
from agent.decision_maker import analyse_the_site
from agent.decision_maker import plan_maker
from agent.decision_maker import attack_target
from reporting.report_maker import generateReportAndSendMail

def exectute(target):
    # start_tools(target)
    #  analyse_the_site()
    # plan_maker()
    # attack_target()
    receiver_email = "developeraromal@gmail.com"
    generateReportAndSendMail(receiver_email)
    