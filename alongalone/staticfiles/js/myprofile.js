// 포스트 내용 바뀌게

// 혼밥 (처음에 자동으로 화면에 뜨는 카테고리)
function setInnerHTML1() {
  var x='<br></br>\n<hr style="width: 1050px; text-align: center; margin-top: 0;">\n<div class="posts">\n<div class="post_row">\n<img class="post green" src="/static/img/chi.jpeg" alt="">\n<img class="post green" src="/static/img/jonmat.jpeg" alt="">\n<div class="post green">3</div>\n</div>\n<<br>\n<div class="post_row">\n<div class="post green">4</div>\n<div class="post green">5</div>\n<div class="post green">6</div>\n</div>\n</div><style>\n.bab.clicked{\ncolor:var(--mint);\n}\n</style>';
  
  const element = document.getElementById('category');
  element.innerHTML 
    =x;
} 

// 혼술
function setInnerHTML2() {
  var x='<br></br>\n<hr style="width: 1050px; text-align: center; margin-top: 0;">\n<div class="posts">\n<div class="post_row">\n<div class="post pink">1</div>\n<div class="post pink">2</div>\n<div class="post pink">3</div>\n</div>\n</br>\n<div class="post_row">\n<div class="post pink">4</div>\n<div class="post pink">5</div>\n<div class="post pink">6</div>\n</div>\n</div>';
  
  const element = document.getElementById('category');
  element.innerHTML 
    =x;
} 

// 혼카페
function setInnerHTML3() {
  var x='<br></br>\n<hr style="width: 1050px; text-align: center; margin-top: 0;">\n<div class="posts">\n<div class="post_row">\n<div class="post blue">1</div>\n<div class="post blue">2</div>\n<div class="post blue">3</div>\n</div>\n</br>\n<div class="post_row">\n<div class="post blue">4</div>\n<div class="post blue">5</div>\n<div class="post blue">6</div>\n</div>\n</div>';
  
  const element = document.getElementById('category');
  element.innerHTML 
    =x;
} 

// 전체보기
function setInnerHTML4() {
  var x='<br></br>\n<hr style="width: 1050px; text-align: center; margin-top: 0;">\n<div class="posts">\n<div class="post_row">\n<div class="post yellow">1</div>\n<div class="post yellow">2</div>\n<div class="post yellow">3</div>\n</div>\n</br>\n<div class="post_row">\n<div class="post yellow">4</div>\n<div class="post yellow">5</div>\n<div class="post yellow">6</div>\n</div>\n</div>';
  
  const element = document.getElementById('category');
  element.innerHTML 
    =x;
} 
