document.addEventListener('DOMContentLoaded', myfunction)

//function myfunction(){

//fetch('https://jxok1dkc2c.execute-api.us-east-1.amazonaws.com/buildresume',
//    {method: 'POST',})
//    .catch(error => console.log('error'))
//}

//function mycount(){

    fetch('https://jxok1dkc2c.execute-api.us-east-1.amazonaws.com/count')
    .then(response => response.json())
    .then(data => {console.log(data)})
   // .catch(error => console.log(error));
//}

//mycount()