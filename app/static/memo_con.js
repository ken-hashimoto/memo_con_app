let arr = []; //メモした内容を格納する配列
let memo = document.getElementById("memo");
let target = document.getElementById("output");
let contents = ""
//webstorageに値が残っているなら復元
if(localStorage["memo"]){
  target.innerHTML = localStorage["memo"];
  arr = target.innerHTML.split("<br><br>");
}

memo.addEventListener('keypress', push);

function push(e) {
  if (e.keyCode == 13 && !e.shiftKey){
    //arrの先頭にメモした内容を追加
      arr.unshift(memo.value);
      contents = arr.join("<br><br>");
      target.innerHTML = contents;
      memo.value = "";
      localStorage["memo"] = contents;
      e.preventDefault();
  }
}
function delete_memo(){
  localStorage.removeItem("memo");
  target.innerHTML = "";
  arr = [];
  alert("削除されました");
}

function copy(){
  // reverse_arrはarrを逆順にしたもの
  reverse_arr = arr.slice().reverse();
  copy_text = reverse_arr.join("\n");
  copyToClipboard(copy_text);
  alert("コピー完了");
  memo.focus();
}

function delete_record(){
  let check_arr = [];
  let checkbtn=document.getElementsByName("del_check");
  for (let i = 0; i < checkbtn.length; i++) {
    if (checkbtn[i].checked) { 
      check_arr.push(checkbtn[i].value);
  }
}
  let check_str = check_arr.join(',');
  $.ajax('/mypage',
    {
      type: 'post',
      data:{
        del_num:check_str
      },
    })
    .done(function(response){
      if (response.result == '削除が完了しました'){
      alert('削除が完了しました');
      location.reload();
      }
      else{
        alert('ログインしてください');
        window.location.href('/login')
      }
    });
}
function copyToClipboard(text){
let tmp = document.createElement("textarea");
tmp.value = text;
document.body.appendChild(tmp);
tmp.select();
document.execCommand("copy");
tmp.parentElement.removeChild(tmp);
}


$(function(){
$('#save').on('click',function(){
  reverse_arr = arr.slice().reverse();
  copy_text = reverse_arr.join("\n");
  title = window.prompt("タイトルを入力してください\n(128文字以内)", "");
  if (title.length > 128){
    alert('タイトルが長すぎます。');
  }
  else{
  $.ajax('/',
  {
    type: 'post',
    data:{
      Text:copy_text,
      Title:title
    },
  })
  .done(function(response){
    if (response.result == '保存されました'){
    alert('保存できました');
    }
    else{
      alert('ログインしてください');
    }
  });
}
})
})
