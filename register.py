# -*- coding:utf-8 -*-
"""
用户登录模块
"""
from flask import Flask, request, render_template
import login_bal

APP = Flask(__name__)


@APP.route("/signup", methods=["POST", "GET"])
def signup():
    return render_template("register.html")


@APP.route("/signup/<cell_no>", methods=["POST", "GET"])
def get_valid_code(cell_no):
    """
    申请用户注册码
    :param cell_no: 申请注册码的手机号
    :return: 注册页面
    """
    print(cell_no)
    codes, status = login_bal.generate_validation_code(cell_no)
    print(codes)
    if status == 1:
        return "OK"
    return "Fail"


@APP.route("/signup/<cell_no>/<validation_code>", methods=["POST", "GET"])
def check_signup(cell_no, validation_code):
    """
    验证用户提交的注册信息
    :param cell_no: 手机号
    :param validation_code:验证码
    :return: 系统页面
    """
    pass


if __name__ == "__main__":
    APP.run()
