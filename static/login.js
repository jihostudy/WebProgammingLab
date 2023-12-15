$(document).ready(function () {
    let id_input = $("#id");
    let password_input = $("#password");
    let login_button = $("#login");
    let register_button = $("#register");

    // #1. 로그인하기
    login_button.click(function (event) {        
        let username = id_input.val();
        let password = password_input.val();
        if(username && password){
        let data = { "username": username, "password": password };
            $.ajax({
                url: "/login",
                type: "post",
                data: data,
                // contentType: "application/x-www-form-urlencoded",                
                error: function (e) {
                    alert("로그인 실패");
                },
            });
        }
    });
    // #2. 등록하기
    register_button.click(function (event) {
        let username = id_input.val();
        let password = password_input.val();
        
        // 공백이 아닐때만
        if(username && password){
            let data = { "username": username, "password": password };
            $.ajax({
                url: "/register",
                type: "post",
                data: data,
                // contentType: "application/x-www-form-urlencoded",               
                error: function (e) {
                    alert("Register Failed!");
                },
            });
        }
        else {
            alert("공백입니다. 다시 입력해주세요");
        }
    });
});
