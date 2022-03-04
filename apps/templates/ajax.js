let fetchbtn = document.getElementById('fetchBtn');
fetchbtn.addEventListener('click',getdata)
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


    url='http://0.0.0.0:3000/app/dairy'
    fetch(url).then((response)=>{
        console.log('Inside first')
        return response.json();
    }).then((data)=>{
        console.log('inside second')
        console.log(data);
    })
}