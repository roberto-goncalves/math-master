""" math_master DOCSTRING 1.0"""


from flask import Flask, request, jsonify
from logging_module import Log
from resources import Factorial, Ackermann, Fibonacci

app = Flask(__name__)

logger = Log(app).get_logger()

@app.route("/math/fibonacci", methods=['POST'])
def fibonacci():
    """ math_master DOCSTRING 1.0"""
    result, time = Fibonacci(n=request.json["n"]).calculate()
    logger.info("execution result",
        extra= {"input": request.json["n"], "result" : result, "time" : time})
    return jsonify(result, time)


@app.route("/math/ackermann", methods=['POST'])
def ackermann():
    """ math_master DOCSTRING 1.0"""
    result, time = Ackermann(n=request.json["n"],
        m=request.json["m"]).calculate(m=request.json["m"], n=request.json["n"])
    logger.info("execution result",
        extra= {"input_n": request.json["n"], "input_m" : request.json["m"], "result" : result, "time" : time})
    return jsonify(result, time)

@app.route("/math/factorial", methods=['POST'])
def factorial():
    """ math_master DOCSTRING 1.0"""
    result, time = Factorial(n=request.json["n"]).calculate()
    logger.info("execution result",
        extra= {"input": request.json["n"], "result" : result, "time" : time})
    return jsonify(result, time)
