from tools.runner import start_tools
from agent.decision_maker import analyse_the_site
from agent.decision_maker import plan_maker


def exectute(target):
    start_tools(target)
    analyse_the_site()
    plan_maker()