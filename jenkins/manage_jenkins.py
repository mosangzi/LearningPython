# -*- coding:utf-8 -*-
import jenkins

class ManageJenkins:
    def __init__(self):
        self.jenkins_url = 'http://119.23.58.84:8080/'
        self.jenkins_user = 'admin'
        self.jenkins_cred = '118b994f2304cf085c5e682b051734b1cb'
        self.server = self._login()

    def _login(self):
        return jenkins.Jenkins(url=self.jenkins_url, username=self.jenkins_user, password=self.jenkins_cred)

    def create_node(self):
        print(self.server.crumb)
        self.server.create_node('test')

if __name__ == '__main__':
    manage_jenkins = ManageJenkins()
    manage_jenkins.create_node()