document.addEventListener('DOMContentLoaded', myfunction)

function myfunction(){

fetch('https://jxok1dkc2c.execute-api.us-east-1.amazonaws.com/buildresume',
    {method: 'POST',})
    .catch(error => console.log('error'))
}