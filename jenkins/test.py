# -*- coding:utf-8 -*-

import jenkinsapi
from jenkinsapi.jenkins import Jenkins


class TestJenkins:
    def __init__(self):
        self.jenkins_url = 'http://119.23.58.84:8080/'
        self.jenkins_user = 'admin'
        self.jenkins_cred = '118b994f2304cf085c5e682b051734b1cb'
        self.jenkins_crumb = 'ce74f9cbdd0686d79562aa3180c845f1c8d47e5a88c058745e32e4c544084dd2'
        self.server = self._login()

    def _login(self):
        return Jenkins(
            baseurl=self.jenkins_url,
            username=self.jenkins_user,
            password=self.jenkins_cred,
            useCrumb=self.jenkins_crumb)

    def test_script(self):
        script = 'printlnHello pythonapi")'
        print(self.server.run_groovy_script(script))

    def create_node(self):
        self.server.create_node(name='test1')


if __name__ == '__main__':
    test_jenkins = TestJenkins()
    # test_jenkins.create_node()
    test_jenkins.test_script()