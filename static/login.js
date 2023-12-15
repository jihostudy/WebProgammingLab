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
                contentType: "application/json",                
                error: function (e) {
                    alert("알맞은 아이디와 비밀번호를 확인하세요");
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
                success: function(e) {
                    alert("Successfully Registered!");
                }
                error: function (e) {
                    alert("Register Failed!");
                },
            });
        }
        else {
            alert("등록하고자 하는 아이디, 비밀번호를 입력하세요");
        }
    });
});
