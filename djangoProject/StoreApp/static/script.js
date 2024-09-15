// OTP Modal Number Boxes
//      this code is used for auto changing boxes while user is filling the OTP modal
document.addEventListener("DOMContentLoaded", function (event) {
  function OTPInput() {
    const inputs = document.querySelectorAll("#otp > *[id]");
    for (let i = 0; i < inputs.length; i++) {
      inputs[i].addEventListener("keydown", function (event) {
        if (event.key === "Backspace") {
          inputs[i].value = "";
          if (i !== 0) inputs[i - 1].focus();
        } else {
          if (i === inputs.length - 1 && inputs[i].value !== "") {
            return true;
          } else if (event.keyCode > 47 && event.keyCode < 58) {
            inputs[i].value = event.key;
            if (i !== inputs.length - 1) inputs[i + 1].focus();
            event.preventDefault();
          } else if (event.keyCode > 64 && event.keyCode < 91) {
            inputs[i].value = String.fromCharCode(event.keyCode);
            if (i !== inputs.length - 1) inputs[i + 1].focus();
            event.preventDefault();
          }
        }
      });
    }
  }
  OTPInput();
});

// show and hide Descriptions tabs
function show_Descriptions() {
  var x = document.getElementById("product-Descriptions");
  var y = document.getElementById("Additional-Information");
  var z = document.getElementById("Customer-Reviews");

  x.style.display = "block";
  y.style.display = "none";
  z.style.display = "none";

  var lx = document.getElementById("liDescriptions");
  lx.style.borderBottom = "solid #1c4e8e";

  var ly = document.getElementById("liAdditionalInformation");
  ly.style.borderBottom = "none";

  var lz = document.getElementById("liShowCustomerReviews");
  lz.style.borderBottom = "none";

  var ax = document.getElementById("aDescriptions");
  var ay = document.getElementById("aAdditionalInformation");
  var az = document.getElementById("aShowCustomerReviews");

  ax.style.fontWeight = "700";
  ay.style.fontWeight = "500";
  az.style.fontWeight = "500";

  ax.style.color = "#1c4e8e";
  ay.style.color = "#000";
  az.style.color = "#000";

  ax.style.fontSize = "1.25rem";
  ay.style.fontSize = "1rem";
  az.style.fontSize = "1rem";
}

function show_Additional_Information() {
  var x = document.getElementById("product-Descriptions");
  var y = document.getElementById("Additional-Information");
  var z = document.getElementById("Customer-Reviews");

  x.style.display = "none";
  y.style.display = "block";
  z.style.display = "none";

  var lx = document.getElementById("liDescriptions");
  lx.style.borderBottom = "none";

  var ly = document.getElementById("liAdditionalInformation");
  ly.style.borderBottom = " solid #1c4e8e";

  var lz = document.getElementById("liShowCustomerReviews");
  lz.style.borderBottom = "none";

  var ax = document.getElementById("aDescriptions");
  var ay = document.getElementById("aAdditionalInformation");
  var az = document.getElementById("aShowCustomerReviews");

  ax.style.fontWeight = "500";
  ay.style.fontWeight = "700";
  az.style.fontWeight = "500";
  ax.style.color = "#000";
  ay.style.color = "#1c4e8e";
  az.style.color = "#000";

  ax.style.fontSize = "1rem";
  ay.style.fontSize = "1.25rem";
  az.style.fontSize = "1rem";
}

function show_Customer_Reviews() {
  var x = document.getElementById("product-Descriptions");
  var y = document.getElementById("Additional-Information");
  var z = document.getElementById("Customer-Reviews");

  x.style.display = "none";
  y.style.display = "none";
  z.style.display = "block";

  var lx = document.getElementById("liDescriptions");
  lx.style.borderBottom = "none";

  var ly = document.getElementById("liAdditionalInformation");
  ly.style.borderBottom = "none";

  var lz = document.getElementById("liShowCustomerReviews");
  lz.style.borderBottom = "solid #1c4e8e";

  var ax = document.getElementById("aDescriptions");
  var ay = document.getElementById("aAdditionalInformation");
  var az = document.getElementById("aShowCustomerReviews");

  ax.style.fontWeight = "500";
  ay.style.fontWeight = "500";
  az.style.fontWeight = "700";
  ax.style.color = "#000";
  ay.style.color = "#000";
  az.style.color = "#1c4e8e";

  ax.style.fontSize = "1rem";
  ay.style.fontSize = "1rem";
  az.style.fontSize = "1.25rem";
}

//add To Cart and increase cart number
function add_to_cart(productName, imageSrc, price) {
  var x = document.getElementById("cart_number");
  const inputElement = document.getElementById("input_number_of_product");
  const currentValue = parseInt(inputElement.value);

  x.innerText = parseInt(x.innerText) + currentValue;

  const htmlCode = `
    <div class="row" id="row_2">
        <div class="col-3 rounded-3 BG-Gray2 align-content-center text-center ">
            <img class="w-100" src="${imageSrc}" alt="">
        </div>
        <div class="col-7 align-content-center my-2">
            <h6 class="fw-normal my-auto ">${productName}</h6>
            <p class="fw-bold my-auto mt-2">$<span id="price_${price}">${price.toFixed(2)}</span></p>
            <p class="fw-normal my-auto mt-1"> QTY: 1</p>
        </div>
        <div class="col-2 align-content-end ">
            <button class="btn" onclick="delete_div_by_id('row_2}');change_number_to_fixed2_by_id('subtotal_number', -${price});"><i class="bi bi-trash3 red-trash-color fs-5"></i></button>
        </div>
        <hr class="mt-3">
    </div>
  `;

  // Create a new DOM element from the HTML string
  const newElement = document.createElement('div');
  newElement.innerHTML = htmlCode;

  // Get the target div element with id "ali"
  const targetDiv = document.getElementById('ali');

  // Append the new element to the target div
  targetDiv.appendChild(newElement);

}

// increase and decrease value of product
function increaseInputValue() {
  const inputElement = document.getElementById("input_number_of_product");
  const currentValue = parseInt(inputElement.value);
  const newValue = currentValue + 1;
  inputElement.value = newValue;
}

function decreaseInputValue() {
  const inputElement = document.getElementById("input_number_of_product");
  const currentValue = parseInt(inputElement.value);
  if (currentValue > 1) {
    const newValue = currentValue - 1;
    inputElement.value = newValue;
  }
}

// function to change number of span of cart with a numberic input

function change_number_of_cart(inputnumber) {
  var x = document.getElementById("cart_number");
  x.innerText = parseInt(x.innerText) + inputnumber;
}

function delete_div_by_id(inputID) {
  const divElement = document.getElementById(inputID);
  divElement.parentNode.removeChild(divElement);
  change_number_of_cart(-1);
  change_text_by_id("number_items_side_bar", -1);
}

// function to change text by id
function change_text_by_id(inputID, inputvalue) {
  const inputElement = document.getElementById(inputID);
  inputElement.innerText = parseInt(inputElement.innerText) + inputvalue;
}

function change_number_to_fixed2_by_id(inputID, inputvalue) {
  const inputElement = document.getElementById(inputID);
  inputElement.innerText = parseFloat(
    parseInt(inputElement.innerText) + inputvalue
  ).toFixed(2);
}

function change_price_of_product(inputID, price) {
  const inputElement = document.getElementById(inputID);
  inputElement.innerText = parseInt(price).toFixed(2);
}

// customer review
var customer_rate = null;

function rate_saver(number) {
  customer_rate = number;
}

function print_customer_review() {
  console.log(customer_rate);
}

function submit_review() {
  // info
  var customer_name;
  var customer_email;
  var customer_comment;

  const input = document.getElementById("inputName1");
  customer_name = input.value;
  const input2 = document.getElementById("inputEmailAddress");
  customer_email = input2.value;
  const input3 = document.getElementById("inputYourReview");
  customer_comment = input3.value;

  console.log("name : " + customer_name + " || rate : " + customer_rate);
}

function make_new_review() {
  // info
  var customer_name;
  var customer_email;
  var customer_comment;

  const input = document.getElementById("inputName1");
  name_customer = input.value;
  const input2 = document.getElementById("inputEmailAddress");
  customer_email = input2.value;
  const input3 = document.getElementById("inputYourReview");
  customer_comment = input3.value;
}

function alertError(errors) {
    for (const field in errors) {
        // Access error messages for each field
        const errorMessages = errors[field];

        // You can iterate through errorMessages if there are multiple errors per field
        for (const message of errorMessages) {
            alert(message);
        }
    }
}





// // new Cursor -----------------------------------------------------------

// // Get references to the cursor and cursor border elements from the DOM
// const cursor = document.getElementById("cursor");
// const cursorBorder = document.getElementById("cursor-border");

// // Initialize variables to track cursor position and border position
// let cursorX = 0,
//   cursorY = 0,
//   borderX = 0,
//   borderY = 0;

// // Variable to store the type of device (touch or mouse)
// let deviceType = "";

// // Function to check if it is a touch device
// const isTouchDevice = () => {
//   try {
//     document.createEvent("TouchEvent");
//     deviceType = "touch"; // Set deviceType to 'touch' if touch event creation is supported
//     return true;
//   } catch (e) {
//     deviceType = "mouse"; // Set deviceType to 'mouse' if touch event creation is not supported
//     return false;
//   }
// };

// // Function to move the cursor
// const move = (e) => {
//   // Determine cursor position based on whether it's a touch or mouse event
//   cursorX = !isTouchDevice() ? e.clientX : e.touches[0].clientX;
//   cursorY = !isTouchDevice() ? e.clientY : e.touches[0].clientY;

//   // Update cursor position in CSS
//   cursor.style.left = `${cursorX}px`;
//   cursor.style.top = `${cursorY}px`;
// };

// // Event listener for mousemove event
// document.addEventListener("mousemove", (e) => {
//   move(e); // Call move function to update cursor position
// });

// // Event listener for touchmove event
// document.addEventListener("touchmove", (e) => {
//   move(e); // Call move function to update cursor position
// });

// // Prevent default behavior on touchend to avoid unwanted scrolling or zooming
// document.addEventListener("touchend", (e) => {
//   e.preventDefault();
// });

// // Function to animate the border around the cursor
// const borderAnimation = () => {
//   const gapValue = 5; // Gap value determines the smoothness of animation

//   // Calculate new border position based on cursor position
//   borderX += (cursorX - borderX) / gapValue;
//   borderY += (cursorY - borderY) / gapValue;

//   // Update border position in CSS
//   cursorBorder.style.left = `${borderX}px`;
//   cursorBorder.style.top = `${borderY}px`;

//   // Request animation frame to continuously update border position
//   requestAnimationFrame(borderAnimation);
// };

// // Initiate border animation
// requestAnimationFrame(borderAnimation);
