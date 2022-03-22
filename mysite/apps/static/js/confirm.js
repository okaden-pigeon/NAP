function CheckEmail_1() {
    //IE対応の為変更
    //var mail = email_1.value; //メールフォームの値を取得
    //var mailConfirm = emailConfirm_1.value; //メール確認用フォームの値を取得
    var mail = document.getElementById("mail1").value; //メールフォームの値を取得
    var mailConfirm = document.getElementById("mail1_confirm").value; //メール確認用フォームの値を取得
    // パスワードの一致確認
    if (mail != mailConfirm){
      alert("メールアドレスと確認用メールアドレスが一致しません"); // 一致していなかったら、エラーメッセージを表示する
      return false;
    }else{
      return true;
    }
  };

  function CheckPassword_1() {
    var password = document.getElementById("inputPassword1").value; //メールフォームの値を取得
    var password_confirm = document.getElementById("inputPassword1_confirm").value; //メール確認用フォームの値を取得
    // パスワードの一致確認
    if (password != password_confirm){
      alert("パスワードと確認用パスワードが一致しません"); // 一致していなかったら、エラーメッセージを表示する
      return false;
    }else{
      return true;
    }
  };

  function CheckPassword_2() {
    var password = document.getElementById("inputPassword2").value; //メールフォームの値を取得
    var password_confirm = document.getElementById("inputPassword2_confirm").value; //メール確認用フォームの値を取得
    // パスワードの一致確認
    if (password != password_confirm){
      alert("パスワードと確認用パスワードが一致しません"); // 一致していなかったら、エラーメッセージを表示する
      return false;
    }else{
      return true;
    }
  };