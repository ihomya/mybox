$.ajax({
url: url, //同文件夹下的json文件路径
type: "GET", //请求方式为get
dataType: "json", //返回数据格式为json
success: function(data) {//请求成功完成后要执行的方法
console.log(data);
//获取jsonTip的div
//var $jsontip = $("#jsonTip");
//存储数据的变量
var strHtml = "123";
//清空内容
$jsontip.empty();
//将获取到的json格式数据遍历到div中
$.each(data, function(infoIndex, info) {
strHtml = info
})
//显示处理后的数据
//$jsontip.html(strHtml);
console.log(strHtml)
}

})
