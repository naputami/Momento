function get_data(){
    //GET TWEET FROM BACKEND
    let  xhr = new XMLHttpRequest();
    let url = "http://127.0.0.1:5000/api/posts"; //ganti nama file sesuai nama file json kalian
    xhr.onreadystatechange = function(){
       if(this.readyState == 4 && this.status == 200){
           let tweets = JSON.parse(this.response)
           tweets["posts"].forEach(tweet => {
               const tweetSection = document.getElementById("section-tweets")
               const card = document.createElement("div")
               card.setAttribute("class", "card mt-3 mb-2")
               const cardHeader = document.createElement("div")
               cardHeader.setAttribute("class", "card-header")
               cardHeader.innerHTML = "Tweet from user " + tweet.username
               const cardBody  = document.createElement("div")
               cardBody.setAttribute("class", "card-body")
               const blockquote = document.createElement("blockquote")
               blockquote.setAttribute("class", "blockquote mb-2 mt-2")
               const p = document.createElement("p")
               p.innerHTML = tweet.content
               
               blockquote.append(p)
               cardBody.append(blockquote)
               card.append(cardHeader, cardBody)
               tweetSection.append(card)
            });
       }
   }
   xhr.open("GET", url, true);
   xhr.send();
}

window.onload = function(){
    // cek apakah access_token & 
    if(localStorage.getItem("access_token")   == null){
        const sectionForm = document.getElementById("section-form")
        sectionForm.classList.add("d-none")
    }
    if(localStorage.getItem('role') === 'user'){
      const adminPanel = document.getElementById('admin-panel')
      adminPanel.setAttribute('class', 'd-none')
    }
    get_data()
  }
  
setInterval(refresh_token(), 1000)
function refresh_token(){
  let  xhr = new XMLHttpRequest();
  let url = "http://127.0.0.1:5000/api/auth/refresh";
   //ganti nama file sesuai nama file json kalian
  xhr.open("POST", url, true)
  xhr.setRequestHeader("Authorization", `Bearer ${localStorage.getItem('refresh_token')}`);
  xhr.onreadystatechange = function(){
     if(this.readyState == 4 && this.status == 200){
       // console.log(this.response)
       data = JSON.parse(this.response)
       localStorage.setItem("access_token", data.accessToken)
      }
    }
    xhr.send()
    
}


//POST NEW TWEET
const formTweet = document.getElementById("form-tweet")
formTweet.addEventListener("submit", function(e){
    e.preventDefault()
    let xhr = new XMLHttpRequest();
    let url = "http://127.0.0.1:5000/api/posts";

  //get data from form
  content = document.getElementById("tweets").value;

  //validasi input
  if (content == "") return alert("Content tidak boleh kosong");

  let data = JSON.stringify({
    content: content
  });


  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=utf-8");
  xhr.setRequestHeader("Authorization", `Bearer ${localStorage.getItem('access_token')}`);
  xhr.onreadystatechange = function () {
    if (this.status == 200) {

        formTweet.reset()
        divEl.setAttribute("class", "alert alert-success");
        divEl.setAttribute("role", "alert");
        divEl.innerHTML = "Tweet berhasil ditambahkan !";
      }else{
      divEl.setAttribute("class", "alert alert-danger");
      divEl.setAttribute("role", "alert");
      divEl.innerHTML = JSON.parse(this.responseText);
    }
};
  xhr.send(data);

  //give feedback
  const alertLoc = document.getElementById("tweet-alert")
  const divEl = document.createElement("div");
  alertLoc.appendChild(divEl);

  
})

//UPLOAD FILES
//POST NEW TWEET
// const formUpload = document.getElementById("form-upload")
// formUpload.addEventListener("submit", function(e){
//     e.preventDefault()
//     let xhr = new XMLHttpRequest();
//     let url = "http://127.0.0.1:5000/api/uploads";
 
//     let formData = new FormData()

//     file = document.getElementById("formFile");
//     formData.append('file', file.files[0])
    
//     xhr.open("POST", url, true);
//     xhr.send(formData);
//     xhr.onreadystatechange = function () {
//       if (this.readyState == 4 && this.status == 200) {
//           divEl.innerHTML = this.responseText
//           formTweet.reset()
//       }
//     };

// //   //give feedback
//   const alertLoc = document.getElementById("tweet-alert")
//   const divEl = document.createElement("div");
//   divEl.setAttribute("class", "alert alert-success");
//   divEl.setAttribute("role", "alert");
 
//   alertLoc.appendChild(divEl);

  
// })

const logout = document.getElementById("logout")
logout.addEventListener("click", function(e){
    e.preventDefault()
    let xhr = new XMLHttpRequest();
    let url = "http://127.0.0.1:5000/api/auth/logout";

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Authorization", `Bearer ${localStorage.getItem('access_token')}`);
    xhr.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        localStorage.removeItem("access_token")
        localStorage.removeItem("refresh_token")
        localStorage.removeItem("role")
        window.location.href = "/login";
        }
  };
  xhr.send();
})


