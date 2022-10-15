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

(function () {
    const slideList = document.querySelector('.slide_list');  // Slide parent dom
    const slideContents = document.querySelectorAll('.slide_content');  // each slide dom
    const slideBtnNext = document.querySelector('.slide_btn_next'); // next button
    const slideBtnPrev = document.querySelector('.slide_btn_prev'); // prev button
    const pagination = document.querySelector('.slide_pagination');
    const slideLen = slideContents.length;  // slide length
    const slideWidth = 1000; // slide width
    const slideSpeed = 300; // slide speed
    const startNum = 0; // initial slide index (0 ~ 4)
    
    slideList.style.width = slideWidth * (slideLen + 2) + "px";
    
    // Copy first and last slide
    let firstChild = slideList.firstElementChild;
    let lastChild = slideList.lastElementChild;
    let clonedFirst = firstChild.cloneNode(true);
    let clonedLast = lastChild.cloneNode(true);

    // Add copied Slides
    slideList.appendChild(clonedFirst);
    slideList.insertBefore(clonedLast, slideList.firstElementChild);

    // Add pagination dynamically
    let pageChild = '';
    for (var i = 0; i < slideLen; i++) {
      pageChild += '<li class="dot';
      pageChild += (i === startNum) ? ' dot_active' : '';
      pageChild += '" data-index="' + i + '"><a href="#"></a></li>';
    }
    pagination.innerHTML = pageChild;
    const pageDots = document.querySelectorAll('.dot'); // each dot from pagination

    slideList.style.transform = "translate3d(-" + (slideWidth * (startNum + 1)) + "px, 0px, 0px)";

    let curIndex = startNum; // current slide index (except copied slide)
    let curSlide = slideContents[curIndex]; // current slide dom
    curSlide.classList.add('slide_active');

    /** Next Button Event */
    slideBtnNext.addEventListener('click', function() {
      if (curIndex <= slideLen - 1) {
        slideList.style.transition = slideSpeed + "ms";
        slideList.style.transform = "translate3d(-" + (slideWidth * (curIndex + 2)) + "px, 0px, 0px)";
      }
      if (curIndex === slideLen - 1) {
        setTimeout(function() {
          slideList.style.transition = "0ms";
          slideList.style.transform = "translate3d(-" + slideWidth + "px, 0px, 0px)";
        }, slideSpeed);
        curIndex = -1;
      }
      curSlide.classList.remove('slide_active');
      pageDots[(curIndex === -1) ? slideLen - 1 : curIndex].classList.remove('dot_active');
      curSlide = slideContents[++curIndex];
      curSlide.classList.add('slide_active');
      pageDots[curIndex].classList.add('dot_active');
    });

    /** Prev Button Event */
    slideBtnPrev.addEventListener('click', function() {
      if (curIndex >= 0) {
        slideList.style.transition = slideSpeed + "ms";
        slideList.style.transform = "translate3d(-" + (slideWidth * curIndex) + "px, 0px, 0px)";
      }
      if (curIndex === 0) {
        setTimeout(function() {
          slideList.style.transition = "0ms";
          slideList.style.transform = "translate3d(-" + (slideWidth * slideLen) + "px, 0px, 0px)";
        }, slideSpeed);
        curIndex = slideLen;
      }
      curSlide.classList.remove('slide_active');
      pageDots[(curIndex === slideLen) ? 0 : curIndex].classList.remove('dot_active');
      curSlide = slideContents[--curIndex];
      curSlide.classList.add('slide_active');
      pageDots[curIndex].classList.add('dot_active');
    });

    /** Pagination Button Event */
    let curDot;
    Array.prototype.forEach.call(pageDots, function (dot, i) {
      dot.addEventListener('click', function (e) {
        e.preventDefault();
        curDot = document.querySelector('.dot_active');
        curDot.classList.remove('dot_active');
        
        curDot = this;
        this.classList.add('dot_active');

        curSlide.classList.remove('slide_active');
        curIndex = Number(this.getAttribute('data-index'));
        curSlide = slideContents[curIndex];
        curSlide.classList.add('slide_active');
        slideList.style.transition = slideSpeed + "ms";
        slideList.style.transform = "translate3d(-" + (slideWidth * (curIndex + 1)) + "px, 0px, 0px)";
      });
    });
  })();

