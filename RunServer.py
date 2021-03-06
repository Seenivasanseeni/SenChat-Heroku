from flask import Flask, render_template, request,session
import os
port=int(os.environ.get("PORT",8000))
app=Flask(__name__)

app.config["SECRET_KEY"]=b'qz\xc3\xf2\x80\xe1\xad\xf2\xf3\x93\x19(~\xac\xb4Ju\xdfl\xcd\xb5\xf9%\xdct\xc81]\xb6\xda\xed\x1c\xa5\x8d'

userid=0
def gen_user(): # todo generate ither users
    global userid
    userid_t=userid
    userid+=1
    return userid_t


def valid_user(user):
    global userid
    user=int(user)
    if(user<userid):
        return True
    return False


messages=[]


#create a register a page

@app.route('/')
def ChatMainPage():
    session["user"]=str(gen_user())
    return render_template("chat.html")



@app.route('/message/add',methods=["POST"])
def addMessage():
    try:
        if(not valid_user(session["user"])):
            return "invalid user"
    except:
        return "Invlaid User"
    global messages
    user=session["user"]
    message=request.get_data() #body will contain the messages #todo find other ways to do this
    message=user+":"+str(message)[2:-1]
    messages.append(message)
    print("Message addded")
    return "Message added"

def stringify(array):
    if (len(array)==0):
        return "[]"
    result="["
    for ai in range(len(array)-1):
        a=array[ai]
        result+="\""+a+"\","
    result+="\""+array[-1]+"\"" +"]"
    return result

def messagesJSON():
    return "{\"messages\":"+stringify(messages)+"}"

@app.route("/message/all")
def sendMessages():
    reply=messagesJSON()
    print(reply)
    return reply


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=port)
