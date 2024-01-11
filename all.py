#-*-coding:utf-8-*-

"""
@author: shencheng
@software: PyCharm
@description: 执行测试脚本
@time: 2022/4/13 9:34
"""
import os
import platform
import pytest

def set_report_env_on_results():
    """
    在allure-results报告的目录下生成一个写入了环境信息的文件：environment.properties(注意：不能放置中文，否则会出现乱码)
    @return:
    """
    # 需要写入的环境信息
    allure_env = {
        'OperatingEnvironment': 'dev',
        'BaseUrl': 'http://172.24.100.75:10006/#/',
        'PythonVersion': platform.python_version(),
        'Platform': platform.platform(),
        'PytestVersion': pytest.__version__,
    }
    allure_env_file = os.path.join('./temp', 'environment.properties')
    with open(allure_env_file, 'w', encoding='utf-8') as f:
        for _k, _v in allure_env.items():
            f.write(f'{_k}={_v}\n')


if __name__ == '__main__':
    pytest.main()
    set_report_env_on_results()
    os.system('allure generate temp -o reports --clean')