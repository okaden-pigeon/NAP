function product_name_str_len(){
  var len = document.getElementById("area1").value.length;
  document.getElementById("product_name_str_len").innerText = len + "/40文字";
}

function product_explanation_str_len(){
  var len = document.getElementById("area2").value.length;
  document.getElementById("strLen").innerText = len + "/500文字";
}

function nickname_str_len(){
  var len = document.getElementById("area3").value.length;
  document.getElementById("nickname_str_len").innerText = len + "/20文字";
}
