const button = document.getElementById("search-doctor");

console.log(document.getElementById("gouvernerat").value);
button.addEventListener("click", () => {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/search/doctor/");
    xhr.setRequestHeader(
      "X-CSRFToken",
      document.querySelector("[name=csrfmiddlewaretoken]").value
    );
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = () => {
      if (xhr.status === 200) {
        console.log(xhr.responseText);
      }
    };
    const data = JSON.stringify({
      gouvernerat:document.getElementById('gouvernerat').value,
      city: document.getElementById('city').value
    });
    xhr.send(data);
  });
