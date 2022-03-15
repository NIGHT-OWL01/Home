let fetchbtn = document.getElementById('fetchBtn');
fetchbtn.addEventListener('click',getCollection)


function getCollection(){
    var mainContainer = document.getElementById("myData");
    url='http://127.0.0.1:8000/collections'
    fetch(url).then(response=>response.json())
    .then(data=>{
        console.log(data)
        for (var i = 0; i < data.length; i++) {
            var div = document.createElement("div");
            div.innerHTML = 'Name: ' + data[i].id + ' ' + data[i].title;
            mainContainer.appendChild(div);
          }
    })
}


let collectionbtn=document.getElementById('add_collection')
collectionbtn.addEventListener('click',saveCollection)
function saveCollection(){
    console.log('Collection btn clicked')
    url='http://127.0.0.1:8000/collections'
    var title = document.getElementById('collection').value;
    console.log('title:'+title)
    d={"title":title,"user":1}
    console.log('token:'+localStorage.getItem('token'))
    params={
        method:'POST',
        headers:{
            'content-Type':'application/json',
            'token':localStorage.getItem('token')
        },
        body:JSON.stringify(d)
    }
    fetch(url,params).then(res=>res.json())
    .then(data=>{console.log(data)})
}
/*
function buttonclickhandler(){
    console.log('fetchbtn clicked')
    
    //instantiate an xhr object
    const xhr = new XMLHttpRequest();

    //open the object
    xhr.open('GET', 'data.txt', true);
    
    //what to do while in progress
    xhr.onprogress = function(){
        console.log('On progress')
    }

    xhr.onload = function(){
        console.log(this.responseText)
    }
    xhr.setRequestHeader('Access-Control-Allow-Origin', '*')
    xhr.send();
}
*/
let loginbtn = document.getElementById('login');


loginbtn.addEventListener('click',login)

function getCokie(){
  

fetch('http://127.0.0.1:8000/cookies',{
        method: 'GET',
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json",
            
        },
        credentials: 'same-origin',
        //credentials: 'include',
        //body: JSON.stringify({})

    

    })

}

function login(){
    var username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    console.log(username,password)
    console.log('inside func')
    url='http://127.0.0.1:8000/auth_user'
    body_data={"username":username,"password":password}
    params={
        method:'POST',
        headers:{
            'content-Type':'application/json'
        },
        body:JSON.stringify(body_data)
    }
    fetch(url,params).then((response)=>{
        console.log('Inside first')
        console.log(response)
        return response.json();
    }).then((res)=>{
        console.log('response git')
        token_data=res['data']
        console.log(res['data'])
        console.log(token_data['access'])
        localStorage.setItem('token', token_data['access']);
    }).catch(err=>{console.log('eror')
    console.log(err)
})
}
function getdata(){
    console.log('inside func')
    data=''
    params={
        method:'post',
        headers:{
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin':'*'
        },
        body:JSON.stringify(data)
    }


    url='http://127.0.0.1:8000/dairy'
    fetch(url).then((response)=>{
        console.log('Inside first')
        return response.json();
    }).then((data)=>{
        console.log(data['dairy items'])
        for(d in data['dairy items']){
            console.log(d);
        }
    })
}
function gettoken(){
    var username='user'
    var password='password321'
    console.log('inside func')
    url='http://127.0.0.1:8000/api-token-auth/'
    body_data={"username":"username","password":"password"}
    params={
        method:'POST',
        headers:{
            'content-Type':'application/json',
            'username':'user',
            'password':'password321',
        },
        data:JSON.stringify(body_data),
    }
    
    fetch(url,params).then((response)=>{
        console.log('Inside first')
        console.log(response)
        return response.json();
    }).then((res)=>{
        console.log('response git')
        console.log(res)
    }).catch(err=>{console.log('eror')
    console.log(err)
})
}