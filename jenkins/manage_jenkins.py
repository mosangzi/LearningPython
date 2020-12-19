# -*- coding:utf-8 -*-
import jenkins


class ManageJenkins:
    def __init__(self):
        self.jenkins_url = 'http://119.23.58.84:8080/'
        self.jenkins_user = 'admin'
        self.jenkins_cred = '118b994f2304cf085c5e682b051734b1cb'
        self.jenkins_crumb = 'ce74f9cbdd0686d79562aa3180c845f1c8d47e5a88c058745e32e4c544084dd2'
        self.server = self._login()

    def _login(self):
        return jenkins.Jenkins(
            url=self.jenkins_url,
            username=self.jenkins_user,
            password=self.jenkins_cred)

    def create_node(self):
        print(self.server.crumb)
        # self.server.create_node('test5',launcher=jenkins.LAUNCHER_COMMAND)
        # self.server.create_node('test6', launcher=jenkins.LAUNCHER_SSH)
        # self.server.create_node('test7', launcher=jenkins.LAUNCHER_JNLP)
        # self.server.create_node('test8', launcher=jenkins.LAUNCHER_WINDOWS_SERVICE)
        self.server.create_node('test8',launcher=jenkins.LAUNCHER_COMMAND,launcher_params={'command':'exec java -jar ~/bin/agent.jar'})


if __name__ == '__main__':
    manage_jenkins = ManageJenkins()
    manage_jenkins.create_node()
