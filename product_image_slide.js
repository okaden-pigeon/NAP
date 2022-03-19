var pics_src = new Array("pics/1.jpg","pics/2.jpg","pics/3.jpg"); //　ユーザが登録した写真に切り替える
var num = 0;

function go_forward(){
    if (num == 2) {
        num = 0;
    }
    else {
        num ++;
    }
    document.getElementById("mypic").src=pics_src[num];
}

function go_back(){
    if (num == 0) {
        num = 2;
    }
    else {
        num --;
    }
    document.getElementById("mypic").src=pics_src[num];
}