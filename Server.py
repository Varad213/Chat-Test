from flask import Flask, request, jsonify
app=Flask(__name__)

connected_devices={}

@app.route('/')
def index():
    return "Server"

@app.route('/connect', methods=['GET'])
def register():
    nickname=request.args.get('nickname')
    if not nickname:
        return jsonify({'error':'Nickname is required'}),400
    ip=request.args.get('ip')
    port=request.args.get('port',12345)

    connected_devices[nickname]=(ip,port)
    return jsonify({"message":f"{nickname} {ip} registered"}),200

@app.route('/unregister', methods=['GET'])
def unregister():
    nickname=request.args.get('nickname')

    if nickname in connected_devices:
        del connected_devices[nickname]
        return jsonify({'message':f'Device {nickname} unregistered'}),200
    else:
        return jsonify({'message':f'Device {nickname} not found'}),404

@app.route('/list',methods=['GET'])
def list_devices():
    return jsonify({'devices':connected_devices}),200

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

