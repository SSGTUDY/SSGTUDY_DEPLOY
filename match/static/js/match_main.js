let parse_about = document.querySelectorAll('.today');
const value_real_today = new Date();
let is_first_page = false;

let init_href = 'http://127.0.0.1:8000/match/';

for(let i = 0;i<parse_about.length;i++){
    let year = "";
    let month = "";
    let date = "";
    let temp = "";

    const item = parse_about[i].innerHTML;

    for(let j = 0;j<item.length;j++){
        if(item[j] == ' '){
            continue;
        }
        else{
            if(item[j] == '년'){
             year = temp;
             temp = '';
            }
            else if(item[j] == '월'){
              month = temp;
              temp = '';
            }
            else if(item[j] == '일'){
                date = temp;
                temp = '';
            }
            if(item[j] != ' ' && item[j] != '년' && item[j] != '월' && item[j] != '일'){
                temp += item[j];
            }
        }
    }
    let new_today = year + '-' + month + '-' + date;
    const new_today_ = new Date(new_today);
    const getDate = new_today_.getTime() - value_real_today.getTime();
    const getDiff = Math.abs(getDate/(60*60*24*1000));

    if(Math.floor(getDiff) < 0){
    document.querySelector('.today').innerHTML = '모집기간 종료'
}
else{

    parse_about[i].innerHTML = Math.floor(getDiff);
}
}

function change_page(){
    let href = document.location.href;
    let valid_index;
    is_first_page = false;
    let new_url = '';

    for(let i = 0;i<href.length;i++){

        if(href[i] == '/'){
            valid_index = i;
            new_url = '';
        }
        else{
            new_url += href[i];
        }
    }

    let temp_new = init_href + new_url;
    let next_ = parseInt(temp_new[temp_new.length-1]);
    let list_ = next_;

    next_++;
    next_ += '';
    console.log(list_);
    console.log(next_);
    temp_new.replace(list_,next_);

    if(valid_index == href.length-1 || new_url == ''){
        is_first_page = true;
    }
    if(is_first_page == true || temp_new[temp_new.length-1] == '/'){ //첫번쨰 페이지인 경우

    }
    else{ //첫번째 페이지가 아닌경우


    }
}

setTimeout(change_page(),1000);


