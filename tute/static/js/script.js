
const dropArea = document.querySelector(".drag-area"),
dragText = dropArea.querySelector("header"),
button = dropArea.querySelector("button"),
input = dropArea.querySelector("input");
let file; 

button.onclick = ()=>{
  input.click(); 
}

input.addEventListener("change", function(){
   file = this.files[0];
  dropArea.classList.add("active");
  showFile(); 
});



dropArea.addEventListener("dragover", (event)=>{
  event.preventDefault(); 
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload File";
});


dropArea.addEventListener("dragleave", ()=>{
  dropArea.classList.remove("active");
  dragText.textContent = "Drag & Drop to Upload File";
});


dropArea.addEventListener("drop", (event)=>{
  event.preventDefault(); 
  file = event.dataTransfer.files[0];
  showFile(); //calling function
});

function showFile(){
  let fileType = file.type; //getting selected file type
  let validExtensions = ["image/jpeg", "image/jpg", "image/png"]; //adding some valid image extensions in array
  if(validExtensions.includes(fileType)){ //if user selected file is an image file
    let fileReader = new FileReader(); //creating new FileReader object
    fileReader.onload = ()=>{
      let fileURL = fileReader.result; //passing user file source in fileURL variable
      let imgTag = `<img src="${fileURL}" alt="image">`; //creating an img tag and passing user selected file source inside src attribute
      dropArea.innerHTML = imgTag; //adding that created img tag inside dropArea container
    }
    fileReader.readAsDataURL(file);
  }else{
    alert("This is not an Image File!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
  }
}