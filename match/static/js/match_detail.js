let value_today = document.getElementById('today').innerHTML;
const value_real_today = new Date();

let year = "";
let month = "";
let date = "";
let temp = "";

for(let i = 0;i<value_today.length;i++){
    if(value_today[i] == ' '){
        continue;
    }
    else{
        if(value_today[i] == '년'){
            year = temp;
            temp = '';
        }
        else if(value_today[i] == '월'){
            month = temp;
            temp = '';
        }
        else if(value_today[i] == '일'){
            date = temp;
            temp = '';
        }
        if(value_today[i] != ' ' && value_today[i] != '년' && value_today[i] != '월' && value_today[i] != '일'){
            temp += value_today[i];
        }
    }
}

let new_today = year + '-' + month + '-' + date;
const new_today_ = new Date(new_today);

const getDate = new_today_.getTime() - value_real_today.getTime();
const getDiff = Math.abs(getDate/(1000 * 60 * 60 * 24));

if(Math.floor(getDiff) < 0){
    document.getElementById('today').innerHTML = '모집기간 종료'
}
else{
    document.getElementById('today').innerHTML = Math.floor(getDiff);
}









