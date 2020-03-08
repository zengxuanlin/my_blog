from flask import jsonify

def formatSuccess(data,status=True):
    return jsonify({
        'code':200,
        'success':status,
        'data':data
    })

def responseData(message,data='',status=True):
    return jsonify({
        'code':200,
        'success':status,
        'data':data,
        'message':message
    })
