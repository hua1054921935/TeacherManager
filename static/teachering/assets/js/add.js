// /**
//  * Created by python on 18-5-6.
//  */
// $(document).ready(function () {
//
//
//         // 获取参数
//         var name = $(".jidian_id").val();
//
//         }
//         $.ajax({
//             url:"/api/v1_0/users/name",
//             type:"PUT",
//             data: JSON.stringify({name: name}),
//             contentType: "application/json",
//             dataType: "json",
//             headers:{
//                 "X-CSRFToken":getCookie("csrf_token")
//             },
//             success: function (data) {
//                 if (data.errno == 0) {
//                     $(".error-msg").hide();
//                     showSuccessMsg();
//                 } else if (data.errno == 4001) {
//                     $(".error-msg").show();
//                 } else if (data.errno == 4101) {
//                     location.href = "/login.html";
//                 }
//             }
//         });
//     })
// })