buttons = document.querySelectorAll(".contact-doctor");
buttons.forEach((button) => {
  button.addEventListener("click", () => {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/contact/doctor/");
    
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
      doctor_id: button.dataset.id,
    });
    xhr.send(data);
  });
});
