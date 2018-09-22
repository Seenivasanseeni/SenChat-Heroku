var model={
    "messages":[],
     appendMessage:function(msg){
        this.messages.push(msg)
     },
     getAllMessages:function(){
        return this.messages;
     }
};


var controller={
    getAllMessages:function(){
        return model.getAllMessages();
     },
     sendMessage:function(message){
        fetch("/message/add",{
            method:"POST",
            body: message
         })       //add methods , cookies and other data
            .then(console.log("Message sent"));
         this.getFromServer();
     },
     getFromServer: function(){
        fetch("/message/all")
            .then(function(response){
                console.log(response);
                return response.json()
            },function(re){
                console.log("rehected response "+re);
            })
             .then(function(data){
                console.log(data)
                model.messages=data.messages;
                view.repaintMessages();
                 },function(r){
                    console.log("rejected data "+r);
                 })

     }
};


var submit = document.getElementById("submit");
var message=document.getElementById("message");
submit.addEventListener("click",(e)=>{
    e.preventDefault();
    controller.sendMessage(message.value);
});

var view={
    repaintMessages:function(){
        messages=controller.getAllMessages();
        let htmlcontent=messages.join("<br/>");
        var container=document.getElementById("container");
        container.innerHTML="";
        container.insertAdjacentHTML("afterbegin",htmlcontent);
    }
}

setInterval(()=>{
controller.getFromServer();
view.repaintMessages();
},2000)
