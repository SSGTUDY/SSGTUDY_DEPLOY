let parse_about = document.querySelectorAll('.today');
const value_real_today = new Date();
let is_first_page = false;

function recruit_all(){ //전체 뺴고 다 바꾸기
   let all = document.querySelectorAll('.recruit_all');

   for(let i = 0;i<all.length;i++){
    all[i].style.display = 'flex';
   }
   let study = document.querySelectorAll('.recruit_study');

   console.log(all);
    for(let i = 0;i<study.length;i++){
        study[i].style.display = 'none';
    }
   let club = document.querySelectorAll('.recruit_club');

    for(let i = 0;i<club.length;i++){
        club[i].style.display = 'none';
    }
    let project = document.querySelectorAll('.recruit_project');

    for(let i = 0;i<project.length;i++){
        project[i].style.display = 'none';
    }
    let survey = document.querySelectorAll('.recruit_survey');

    for(let i = 0;i<survey.length;i++){
        survey[i].style.display = 'none';
    }
    let q = document.querySelectorAll('.recruit_q');


}

function recruit_club(){
   let all = document.querySelectorAll('.recruit_all');

   for(let i = 0;i<all.length;i++){
     all[i].style.display = 'none';
   }
   let study = document.querySelectorAll('.recruit_study');
    for(let i = 0;i<study.length;i++){
        study[i].style.display = 'none';
    }
   let club = document.querySelectorAll('.recruit_club');
    for(let i = 0;i<club.length;i++){
        club[i].style.display = 'flex';
    }
    let project = document.querySelectorAll('.recruit_project');

    for(let i = 0;i<project.length;i++){
        project[i].style.display = 'none';
    }
    let survey = document.querySelectorAll('.recruit_survey');

    for(let i = 0;i<survey.length;i++){
        survey[i].style.display = 'none';
    }
    let q = document.querySelectorAll('.recruit_q');

    for(let i = 0;i<q.length;i++){
        survey[i].style.display = 'none';
    }
}

function recruit_study(){
    let all = document.querySelectorAll('.recruit_all');

   for(let i = 0;i<all.length;i++){
     all[i].style.display = 'none';
   }
   let study = document.querySelectorAll('.recruit_study');
    for(let i = 0;i<study.length;i++){
        study[i].style.display = 'flex';
    }
   let club = document.querySelectorAll('.recruit_club');
    for(let i = 0;i<club.length;i++){
        club[i].style.display = 'none';
    }
    let project = document.querySelectorAll('.recruit_project');

    for(let i = 0;i<project.length;i++){
        project[i].style.display = 'none';
    }
    let survey = document.querySelectorAll('.recruit_survey');

    for(let i = 0;i<survey.length;i++){
        survey[i].style.display = 'none';
    }
    let q = document.querySelectorAll('.recruit_q');

    for(let i = 0;i<q.length;i++){
        survey[i].style.display = 'none';
    }
}

function recruit_project(){
    let all = document.querySelectorAll('.recruit_all');

   for(let i = 0;i<all.length;i++){
     all[i].style.display = 'none';
   }
   let study = document.querySelectorAll('.recruit_study');
    for(let i = 0;i<study.length;i++){
        study[i].style.display = 'none';
    }
   let club = document.querySelectorAll('.recruit_club');
    for(let i = 0;i<club.length;i++){
        club[i].style.display = 'none';
    }
    let project = document.querySelectorAll('.recruit_project');

    for(let i = 0;i<project.length;i++){
        project[i].style.display = 'flex';
    }
    let survey = document.querySelectorAll('.recruit_survey');

    for(let i = 0;i<survey.length;i++){
        survey[i].style.display = 'none';
    }

    let q = document.querySelectorAll('.recruit_q');

    for(let i = 0;i<q.length;i++){
        survey[i].style.display = 'none';
    }
}


function recruit_survey(){
    let all = document.querySelectorAll('.recruit_all');

   for(let i = 0;i<all.length;i++){
     all[i].style.display = 'none';
   }
   let study = document.querySelectorAll('.recruit_study');
    for(let i = 0;i<study.length;i++){
        study[i].style.display = 'none';
    }
   let club = document.querySelectorAll('.recruit_club');
    for(let i = 0;i<club.length;i++){
        club[i].style.display = 'none';
    }
    let project = document.querySelectorAll('.recruit_project');

    for(let i = 0;i<project.length;i++){
        project[i].style.display = 'none';
    }
    let survey = document.querySelectorAll('.recruit_survey');

    for(let i = 0;i<survey.length;i++){
        survey[i].style.display = 'flex';
    }

    let q = document.querySelectorAll('.recruit_q');

    for(let i = 0;i<q.length;i++){
        survey[i].style.display = 'none';
    }
}

function display_search(){
     let all = document.querySelectorAll('.recruit_all');

   for(let i = 0;i<all.length;i++){
     all[i].style.display = 'none';
   }
   let study = document.querySelectorAll('.recruit_study');
    for(let i = 0;i<study.length;i++){
        study[i].style.display = 'flex';
    }
   let club = document.querySelectorAll('.recruit_club');
    for(let i = 0;i<club.length;i++){
        club[i].style.display = 'flex';
    }
    let project = document.querySelectorAll('.recruit_project');

    for(let i = 0;i<project.length;i++){
        project[i].style.display = 'flex';
    }
    let survey = document.querySelectorAll('.recruit_survey');

    for(let i = 0;i<survey.length;i++){
        survey[i].style.display = 'flex';
    }



}

recruit_all();

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

    parse_about[i].innerHTML = 'D' + ' ' + '-' + ' ' +  Math.floor(getDiff);
}
}


let buttonRight = document.getElementById('slideRight');
  let buttonLeft = document.getElementById('slideLeft');

  buttonLeft.addEventListener('click', function(){
    document.getElementById('slider').scrollLeft -= 180
  });

  buttonRight.addEventListener('click', function(){
    document.getElementById('slider').scrollLeft += 180

  });

  $('.slider').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  dots: true,
  centerMode: true,
  focusOnSelect: true
});